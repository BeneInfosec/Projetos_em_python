import pandas as pd
import json

# Carregar dados do arquivo JSON
with open('paises.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Criar um DataFrame
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo Excel
df.to_excel("paises.xlsx", index=False, engine='openpyxl')

print("Arquivo Excel criado com sucesso.")
