import pandas as pd

data = pd.read_excel("data/VendaCarros.xlsx")
#listar toda a tabela
print(data)
#listar primeiros registros
print(data.head())
#lista os ultimos registros
print(data.tail())
#contagem por valor da coluna Fabricante
print(data["Fabricante"].value_counts())