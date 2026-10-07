"""Gera o gráfico de frequencia a partir de dados_frequencia.csv."""
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
    dados = pd.read_csv(pasta / 'dados' / 'dados_frequencia.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    frequencias = dados['tipo_atendimento'].value_counts()
    fig, ax = plt.subplots(figsize=(9, 6))
    barras = ax.bar(frequencias.index, frequencias.values, color='#3b82b5')
    ax.bar_label(barras, padding=4)
    ax.set(title='Frequência dos tipos de atendimento', xlabel='Tipo de atendimento', ylabel='Quantidade de chamados')
    ax.set_ylim(0, frequencias.max() * 1.15)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_frequencia.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
