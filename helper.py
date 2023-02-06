import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# def perfis_de_medias_num(var,  df_, num_quebras=4):
#     var_cat = pd.qcut(df_[var], num_quebras, duplicates='drop')
#     fig, ax = plt.subplots(1, 1)
#     ax = sns.pointplot(x = var_cat, y = 'survived', data=df_)
#     st.pyplot(fig)

def perfis_de_medias_quali(df_,  y_, var_):
    sns.set(style="whitegrid", color_codes=True)

    fig, ax2 = plt.subplots(1, 1)
    ax=ax2.twinx()
    
    freq = df_[var_].value_counts(normalize=True).sort_index()
    pal = sns.color_palette("Greens_d", 50)
    pal2 = sns.color_palette("Blues_d", 50)
    
    rank = freq.argsort()
#     sns.barplot(x=freq.index, y=freq, palette=np.array(pal)[:freq.shape[0]])

    sns.barplot(x=freq.index, y=freq, palette=np.array(pal)[:freq.shape[0]], ax=ax2)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    ax2.grid(False)
    ax2.set_ylabel('Distribuição (%)', color=pal[30], fontsize=14)
    ax2.set_ylim([0, 1])
    ax2.spines['left'].set_color(pal[10])
    ax2.tick_params(axis='y', colors=pal[35])
    ax2.set_xticklabels(labels = freq.index, rotation=30)
    
    sns.pointplot(x = var_, y = y_, data=df_, ax=ax, order=freq.index)
    ax.yaxis.tick_left()
    ax.yaxis.set_label_position("left")
    ax.grid(False)
    ax.set_ylabel(f'Média de {y_}', color=pal2[32], fontsize=14)
    ax.spines['left'].set_color(pal[10])
    ax.spines['right'].set_color(pal2[35])
    ax.tick_params(axis='y', colors=pal2[30])
    ax.set_xticklabels(labels = freq.index, rotation=30)
    
    return fig

    
def perfis_de_medias_num(df_,  y_, var_, num_quebras=4):
    sns.set(style="whitegrid", color_codes=True)

    var_cat = pd.qcut(df_[var_], num_quebras, duplicates='drop')
    fig, ax2 = plt.subplots(1, 1)
    ax=ax2.twinx()
    
    freq = var_cat.value_counts(normalize=True)
    pal = sns.color_palette("Greens_d", 50)
    pal2 = sns.color_palette("Blues_d", 50)
    rank = freq.argsort()
    
    sns.barplot(x=freq.index, y=freq, palette=np.array(pal)[:freq.shape[0]], ax=ax2)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    ax2.grid(False)
    ax2.set_ylabel('Distribuição (%)', color=pal[30], fontsize=14)
    ax2.set_ylim([0, 1])
    ax2.spines['left'].set_color(pal[10])
    ax2.tick_params(axis='y', colors=pal[35])
    ax2.set_xticklabels(labels = freq.index, rotation=30)
    
    # ax2.set_ylim([freq.index.min(), freq.index.max()])
    sns.pointplot(x = var_cat, y = y_, data=df_, color=pal2[35], ax=ax)
    ax.yaxis.tick_left()
    ax.yaxis.set_label_position("left")
    ax.grid(False)
    ax.set_ylabel(f'Média de {y_}', color=pal2[32], fontsize=14)
    ax.spines['left'].set_color(pal[10])
    ax.spines['right'].set_color(pal2[35])
    ax.tick_params(axis='y', colors=pal2[30])
    ax.set_xticklabels(labels = freq.index, rotation=30)

    
    
    return fig
