"""Gera o gráfico de boxplot a partir de dados_boxplot.csv."""
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
    dados = pd.read_csv(pasta / 'dados' / 'dados_boxplot.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.boxplot(data=dados, x='departamento', y='salario', color='#7eb6d9', ax=ax)
    ax.set(title='Distribuição dos salários por departamento', xlabel='Departamento', ylabel='Salário (R$)')
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_boxplot.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
