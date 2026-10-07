"""Gera o gráfico de linhas a partir de dados_linhas.csv."""
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mostrar', action='store_true', help='Abre o gráfico após salvar.')
    args = parser.parse_args()
    pasta = Path(__file__).resolve().parent
    dados = pd.read_csv(pasta / 'dados' / 'dados_linhas.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    dados['data'] = pd.to_datetime(dados['data'], format='%Y-%m-%d')
    dados = dados.sort_values('data')
    fig, ax = plt.subplots(figsize=(11, 6))
    sns.lineplot(data=dados, x='data', y='vendas', hue='loja', marker='o',
                 markersize=4, errorbar=None, palette='Set2', ax=ax)
    ax.set(title='Evolução das vendas por loja', xlabel='Data', ylabel='Vendas')
    localizador = mdates.AutoDateLocator(minticks=5, maxticks=9)
    ax.xaxis.set_major_locator(localizador)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.tick_params(axis='x', rotation=30)
    ax.legend(title='Loja')
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_linhas.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
