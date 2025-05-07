import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# Separe os grupos
lucrativas = df[df['Profitable'] == 1]
nao_lucrativas = df[df['Profitable'] == 0]

# 1. Estatísticas para cada grupo
def estatisticas(grupo, nome):
    media = grupo['Revenue (M USD)'].mean()
    mediana = grupo['Revenue (M USD)'].median()
    std = grupo['Revenue (M USD)'].std()
    p25 = grupo['Revenue (M USD)'].quantile(0.25)
    p75 = grupo['Revenue (M USD)'].quantile(0.75)
    print(f"\nEstatísticas - {nome}")
    print(f"Média: {media:.2f} milhões")
    print(f"Mediana: {mediana:.2f} milhões")
    print(f"Desvio padrão: {std:.2f}")
    print(f"Percentil 25%: {p25:.2f}")
    print(f"Percentil 75%: {p75:.2f}")

estatisticas(lucrativas, "Lucrativas")
estatisticas(nao_lucrativas, "Não Lucrativas")

# 2. Comparação direta entre os grupos
media_lucrativas = lucrativas['Revenue (M USD)'].mean()
media_nao_lucrativas = nao_lucrativas['Revenue (M USD)'].mean()
print(f"\n📊 Comparação:")
print(f"A receita média das startups lucrativas é {media_lucrativas:.2f}M, enquanto das não lucrativas é {media_nao_lucrativas:.2f}M.")

# 3. Identificação de outliers em não lucrativas (acima do percentil 90%)
p90_nao_lucrativas = nao_lucrativas['Revenue (M USD)'].quantile(0.90)
outliers = nao_lucrativas[nao_lucrativas['Revenue (M USD)'] > p90_nao_lucrativas]

print(f"\n🚨 Outliers: Startups NÃO lucrativas com receita acima do percentil 90% ({p90_nao_lucrativas:.2f}M):")
print(outliers[['Revenue (M USD)']])

# Histograma com KDE
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Revenue (M USD)', hue='Profitable', kde=True, bins=30, palette=['#FF0000', '#00FF00'], element='step')
plt.title('Distribuição de Receita entre Startups Lucrativas e Não Lucrativas')
plt.xlabel('Receita (milhões USD)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()