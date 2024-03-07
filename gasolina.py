%%writefile gasolina.csv
dia,venda
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

#importação de bibliotecas
import seaborn as sns
import pandas as pd

df_venda= pd.read_csv('/content/gasolina.csv')
grafico = sns.lineplot(data=df_venda, x = 'dia',y= 'venda')
