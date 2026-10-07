"""Gera o gráfico de pizza a partir de dados_pizza.csv."""
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mostrar', action='store_true', help='Abre o gráfico após salvar.')
    args = parser.parse_args()
    pasta = Path(__file__).resolve().parent
    dados = pd.read_csv(pasta / 'dados' / 'dados_pizza.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.pie(dados['faturamento'], labels=dados['canal_venda'], autopct='%1.1f%%',
           startangle=90, colors=sns.color_palette('Set2', len(dados)),
           wedgeprops={'edgecolor': 'white', 'linewidth': 2}, pctdistance=0.72)
    ax.set_title('Participação dos canais no faturamento', pad=20)
    ax.axis('equal')
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_pizza.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
