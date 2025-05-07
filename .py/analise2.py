import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# 1. Moda do 'Exit Status' por lucratividade
moda_lucrativas = df[df['Profitable'] == 1]['Exit Status'].mode()[0]
moda_nao_lucrativas = df[df['Profitable'] == 0]['Exit Status'].mode()[0]

print("Moda - Startups Lucrativas:", moda_lucrativas)
print("Moda - Startups Não Lucrativas:", moda_nao_lucrativas)

# 2. Média (proporção) de startups lucrativas por Exit Status
proporcao_lucrativas = df.groupby('Exit Status')['Profitable'].mean()

# Contagem absoluta de cada Exit Status
contagem_status = df['Exit Status'].value_counts()

print("\nProporção de lucratividade por Exit Status:\n", proporcao_lucrativas)
print("\nContagem absoluta por Exit Status:\n", contagem_status)

# 3. Percentis de lucratividade por Exit Status
percentis_por_status = df.groupby('Exit Status')['Profitable'].quantile([0.25, 0.5, 0.75]).unstack()

print("\nPercentis (25%, 50%, 75%) de lucratividade por Exit Status:\n", percentis_por_status)

# 4. Gráfico de barras com proporção de startups lucrativas por Exit Status
plt.figure(figsize=(8,6))
sns.barplot(x=proporcao_lucrativas.index, y=proporcao_lucrativas.values, palette="Set2")
plt.title('Proporção de Startups Lucrativas por Exit Status')
plt.ylabel('Proporção Lucrativas')
plt.xlabel('Exit Status')
plt.ylim(0, 1.05)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
