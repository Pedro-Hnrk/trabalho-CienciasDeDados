import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# Calcular estatísticas por região
region_groups = df.groupby('Region')
region_stats = region_groups['Valuation (M USD)'].agg(['mean', 'std', 'count'])
region_stats['p90'] = region_groups['Valuation (M USD)'].quantile(0.9)

# Marcar outliers (valores acima do 90º percentil por região)
df['Outlier'] = df.apply(
    lambda row: row['Valuation (M USD)'] > region_stats.loc[row['Region'], 'p90'],
    axis=1
)

# Calcular médias com e sem outliers
mean_with_outliers = df.groupby('Region')['Valuation (M USD)'].mean()
mean_without_outliers = df[~df['Outlier']].groupby('Region')['Valuation (M USD)'].mean()

# Preparar DataFrame para gráfico
impact_df = pd.DataFrame({
    'Com Outliers': mean_with_outliers,
    'Sem Outliers': mean_without_outliers
}).reset_index().melt(id_vars='Region', var_name='Tipo', value_name='Valuation Médio')

# Plotar gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=impact_df, x='Valuation Médio', y='Region', hue='Tipo', palette='Set2')
plt.title('Impacto dos Outliers na Média de Valuation por Região')
plt.xlabel('Valuation Médio (Milhões USD)')
plt.ylabel('Região')
plt.grid(True, axis='x')
plt.tight_layout()
plt.show()