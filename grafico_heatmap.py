"""Gera o gráfico de heatmap a partir de dados_heatmap.csv."""
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
    dados = pd.read_csv(pasta / 'dados' / 'dados_heatmap.csv')
    sns.set_theme(style='whitegrid', context='notebook')
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    matriz = dados.pivot(index='dia_semana', columns='horario', values='movimento_clientes')
    matriz = matriz.reindex(index=dias, columns=sorted(matriz.columns))
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(matriz, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=0.5,
                cbar_kws={'label': 'Quantidade de clientes'}, ax=ax)
    ax.set(title='Movimento de clientes por dia e horário', xlabel='Horário', ylabel='Dia da semana')
    ax.tick_params(axis='y', rotation=0)
    fig.tight_layout()
    saida = pasta / 'graficos' / 'grafico_heatmap.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=180, bbox_inches='tight')
    print(f'Gráfico salvo: {saida}')
    if args.mostrar:
        plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
