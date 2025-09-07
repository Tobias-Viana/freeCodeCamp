import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("boilerplate-medical-data-visualizer\medical_examination.csv")

# Calcula o IMC e cria uma nova coluna com 0 e 1 de acordo com a condição
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100) ** 2) > 25, 1, 0)

# Normaliza as variáveis de acordo com a condição de ter ou não a doença entre 0 e 1
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# Função para plotar o gráfico de barras
def draw_cat_plot():
    
    # Ajusta variáveis
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 8
    t = sns.catplot(
        x='variable',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='count'
    )
    
    # Set ylabel to 'total'
    t.set_ylabels('total')
    
    # Save the figure
    t.fig.savefig('catplot.png')
    return t.fig



# Função para plotar o gráfico de calor
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &  # pressão diastólica <= sistólica
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &  
    (df['weight'] >= df['weight'].quantile(0.025)) &  
    (df['weight'] <= df['weight'].quantile(0.975))    
]

    # 12
    corr = df_heat.corr()
    
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15
    sns.heatmap(
    corr,
    mask=mask,
    annot=True,      
    fmt=".1f",      
    center=0,         
    cmap='coolwarm',  
    square=True,      
    linewidths=0.5,  
    cbar_kws={'shrink': 0.5},
    ax=ax
    )

    # 16
    fig.savefig('heatmap.png')
    return fig