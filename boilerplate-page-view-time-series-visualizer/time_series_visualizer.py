import matplotlib.pyplot as plt
import matplotlib.patches as mpl
import pandas as pd
import seaborn as sns
import calendar
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
# Limpar os dados removendo dias em que o número de visualizações está abaixo do 2,5% ou acima do 97,5% do valor total
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Definir título e rótulos dos eixos
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('graphics/line_plot.png')
    return fig

def draw_bar_plot():
    # Agrupando por ano e mês e calculando a média
    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean()

    # Draw bar plot
    years = [2016, 2017, 2018, 2019]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    # em x, fica definido um array do numpy = [0, 1, 2, 3]
    x = np.arange(len(years))
    # em width, define a largura das barras
    width = 0.4 / 12
    
    # plotando o gráfico com o matplot lib
    fig, ax = plt.subplots(figsize=(10,8))
    
    # esse for coloca em month_values os valores correspondentes para cada ano e mês
    for i, m in enumerate(months):
        month_values = []
        for year in years:
            try:
                month_values.append(df_bar.loc[(year, m)])
            except KeyError:
                month_values.append(0)
        ax.bar(x + i*width, month_values, width=width, label=calendar.month_name[m])
    
    # Definir os rótulos do eixo X
    xticks_pos = x + width*(len(months)-1)/2
    ax.set_xticks(xticks_pos)
    
    ax.set_xticklabels([str(y) for y in years], rotation=90)
    
    # definição dos nomes do eixo X e do eixo Y
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    ax.legend(title="Months", loc="upper left", bbox_to_anchor=(0, 1))

    # Save image and return fig (don't change this part)
    fig.savefig('graphics/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

    # Primeiro gráfico de caixa por ano
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    
    ax1.set_title("Year-wise Box Plot (Trend)")
    
    # Definimos o rótulo do eixo x
    ax1.set_xlabel("Year")
    
    # Definimos o rótulo do eixo y
    ax1.set_ylabel("Page Views")
    
    # Segundo gráfico de caixa por mês
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Plotamos o segundo gráfico de caixa
    sns.boxplot(x='month', y='value', order=month_order, data=df_box, ax=ax2)
    
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    
    # Definimos o rótulo do eixo x
    ax2.set_xlabel("Month")
    
    # Definimos o rótulo do eixo y
    ax2.set_ylabel("Page Views")
    
    # Rotacionamos os rótulos do eixo x para melhor legibilidade
    ax2.tick_params(axis='x', rotation=45)
    
    # Ajustamos o layout para evitar sobreposição
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('graphics/box_plot.png')
    return fig