import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('startup_data.csv')  

print(df['Region'].value_counts())
print(df['Industry'].value_counts())
print(df['Exit Status'].value_counts())






















