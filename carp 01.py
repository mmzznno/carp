
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
def read():
    
    #加工したデータを読み込み(順位と打率と防御率)
    df = pd.read_csv("carp_seiseki_mas.csv").loc[:,["rank","ave","er_ave"]]
    #df = pd.read_csv("carp_seiseki_mas.csv").loc[:,["rank","er_ave"]]

    #型の変換
    df["rank"].astype(int)
    df["ave"].astype(float)
    df["er_ave"].astype(float)

    #順位と打率と防御率の相関
    
    df = df.corr(method='kendall')
    print(df)
    sns.heatmap(df, vmax=1, vmin=-1, center=0)
    plt.savefig('carp_heatmap_corr.png')

read()