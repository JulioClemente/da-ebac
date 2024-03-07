import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tabela = pd.read_csv('gasolina.csv')
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=tabela, x='dia', y='venda')
  grafico.set(title='Vendas de gasolina',ylabel = 'Dias do mês',xlabel = 'Vendas do mês')
  plt.savefig("gasolina.png")# código de geração do gráfico