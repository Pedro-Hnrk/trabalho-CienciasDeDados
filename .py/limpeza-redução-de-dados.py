import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('startup_data.csv')  # Substitua pelo caminho do seu arquivo

# Verificar valores nulos em cada coluna
print(df.isnull().sum())
print(df.duplicated().sum())

