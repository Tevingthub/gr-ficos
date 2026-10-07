"""Gera o gráfico de regressao a partir de dados_regressao.csv."""
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mostrar', action='store_true', help='Abre o gráfico após salvar.')
    args = parser.parse_args()
    pasta = Path(__file__).resolve().parent
    dados = pd.read_csv(pasta / 'dados' / 'dados_regressao.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.regplot(data=dados, x='renda_mensal', y='gasto_mensal', ci=None,
                scatter_kws={'alpha': 0.65, 's': 40}, line_kws={'color': '#b83b46'}, ax=ax)
    coeficiente, intercepto = np.polyfit(dados['renda_mensal'], dados['gasto_mensal'], 1)
    previsto = coeficiente * dados['renda_mensal'] + intercepto
    r2 = 1 - ((dados['gasto_mensal'] - previsto) ** 2).sum() / ((dados['gasto_mensal'] - dados['gasto_mensal'].mean()) ** 2).sum()
    ax.text(0.04, 0.96, f'y = {coeficiente:.3f}x {intercepto:+.2f}\nR² = {r2:.3f}',
            transform=ax.transAxes, va='top', bbox={'facecolor': 'white', 'alpha': 0.85, 'edgecolor': '#cccccc'})
    ax.set(title='Regressão linear: renda e gasto mensal', xlabel='Renda mensal (R$)', ylabel='Gasto mensal (R$)')
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_regressao.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
