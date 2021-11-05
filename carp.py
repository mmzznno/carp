
import pandas as pd
import numpy as np
 
#driver = webdriver.Chrome(ChromeDriverManager().install()) 
def chuushutu():
    
    #NTBからカープのデータを抽出
    url = 'https://npb.jp/bis/teams/yearly_c.html'
    #https://npb.jp/bis/teams/yearly_c.html

    tables = pd.read_html(url)

    #テーブルの中を抜き出す
    #print(len(tables))
    df = tables[2]

    #ゴミデータを削除
    df = df.drop(df.index[[11, 22, 33, 44, 55, 66, 77]])
    df = df.reset_index(drop=True)
    
    df.to_csv("carp_seiseki.csv",encoding='utf_8_sig')
    #carp_seiseki.csv 1行目を削除してcarp_seiseki_mas.csvとして保存

 
chuushutu()