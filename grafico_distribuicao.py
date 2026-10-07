"""Gera o gráfico de distribuicao a partir de dados_distribuicao.csv."""
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import seaborn as sns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mostrar', action='store_true', help='Abre o gráfico após salvar.')
    args = parser.parse_args()
    pasta = Path(__file__).resolve().parent
    dados = pd.read_csv(pasta / 'dados' / 'dados_distribuicao.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.histplot(data=dados, x='idade', binwidth=5, color='#3b82b5', edgecolor='white', ax=ax)
    ax.set(title='Distribuição das idades dos clientes', xlabel='Idade (anos)', ylabel='Quantidade de clientes')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_distribuicao.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
