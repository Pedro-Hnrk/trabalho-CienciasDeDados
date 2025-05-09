import pandas as pd
import plotly.express as px

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


# Coordenadas aproximadas para cada região (centros geográficos)
region_coords = {
    'North America': {'lat': 54.5260, 'lon': -105.2551},
    'South America': {'lat': -8.7832, 'lon': -55.4915},
    'Europe': {'lat': 54.5260, 'lon': 15.2551},
    'Asia': {'lat': 34.0479, 'lon': 100.6197},
    'Australia': {'lat': -25.2744, 'lon': 133.7751},
    'Africa': {'lat': -8.7832, 'lon': 34.5085}
}

# Inserir as coordenadas no dataframe
stats['lat'] = stats.index.map(lambda x: region_coords[x]['lat'])
stats['lon'] = stats.index.map(lambda x: region_coords[x]['lon'])

# Criar mapa de dispersão
fig = px.scatter_geo(
    stats,
    lat='lat',
    lon='lon',
    hover_name=stats.index,
    size='Startup Count',
    color='Média',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='Média de Valuation (M USD) vs Quantidade de Startups por Região',
    size_max=50
)
fig.update_layout(legend_title_text='Nº de Startups')
fig.show()