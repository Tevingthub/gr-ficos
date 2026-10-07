"""Gera o gráfico de dispersao a partir de dados_dispersao.csv."""
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
    dados = pd.read_csv(pasta / 'dados' / 'dados_dispersao.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(data=dados, x='altura_cm', y='peso_kg', hue='sexo', style='sexo',
                    s=65, alpha=0.8, palette='Set2', ax=ax)
    ax.set(title='Relação entre altura e peso', xlabel='Altura (cm)', ylabel='Peso (kg)')
    ax.legend(title='Sexo')
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_dispersao.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
