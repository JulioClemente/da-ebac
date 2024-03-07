import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv('gasolina.csv')
grafico = sns.lineplot(data=tabela, x='dia', y='venda')