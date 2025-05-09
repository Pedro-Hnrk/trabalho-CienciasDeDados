import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados
file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# 2. Estatísticas por região
grouped = df.groupby('Region')['Valuation (M USD)']

stats = pd.DataFrame({
    'Média': grouped.mean(),
    'Mediana': grouped.median(),
    'Desvio Padrão': grouped.std(),
    'P25': grouped.quantile(0.25),
    'P75': grouped.quantile(0.75),
    'P90': grouped.quantile(0.90)
})

print("📊 Estatísticas por Região:")
print(stats)

# 3. Destacar regiões
maior_media = stats['Média'].idxmax()
menor_dp = stats['Desvio Padrão'].idxmin()

print(f"\n🌍 Região com maior média de valuation: {maior_media} ({stats.loc[maior_media, 'Média']:.2f} M USD)")
print(f"📉 Região com menor dispersão (menor desvio padrão): {menor_dp} ({stats.loc[menor_dp, 'Desvio Padrão']:.2f} M USD)")

# 4. Outliers por região (valores acima do percentil 90 regional)
outliers = []
for region in df['Region'].unique():
    limite_90 = df[df['Region'] == region]['Valuation (M USD)'].quantile(0.9)
    region_outliers = df[(df['Region'] == region) & (df['Valuation (M USD)'] > limite_90)]
    outliers.append(region_outliers)

outliers_df = pd.concat(outliers)
print(f"\n🚨 Total de outliers encontrados: {len(outliers_df)}")
print(outliers_df[['Region', 'Valuation (M USD)']])

# Contagem de startups por região
contagem = df['Region'].value_counts()
stats['Startup Count'] = stats.index.map(contagem)


# Gráfico de barras horizontal com Seaborn (usando a média de valuation por região)
plt.figure(figsize=(10, 6))
sns.barplot(data=stats.reset_index(), y='Region', x='Média', palette='viridis')

plt.title('Valuation Médio por Região (Startups)')
plt.xlabel('Valuation Médio (Milhões USD)')
plt.ylabel('Região')
plt.grid(axis='x')
plt.tight_layout()
plt.show()
