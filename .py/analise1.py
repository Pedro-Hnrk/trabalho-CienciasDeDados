import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o dataset
file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# Filtrando startups fundadas após 2010
df_filtered = df[df["Year Founded"] > 2010]

# Selecionando as colunas de interesse
df_filtered = df_filtered[["Employees", "Valuation (M USD)"]].copy()

# Convertendo valuation de milhões para bilhões
df_filtered["Valuation (B USD)"] = df_filtered["Valuation (M USD)"] / 1000

# Estatísticas descritivas
stats_summary = {
    "Média": df_filtered.mean(),
    "Mediana": df_filtered.median(),
    "Moda": df_filtered.mode().iloc[0],
    "Desvio Padrão": df_filtered.std(),
    "Percentil 25%": df_filtered.quantile(0.25),
    "Percentil 50%": df_filtered.quantile(0.50),
    "Percentil 75%": df_filtered.quantile(0.75),
    "Percentil 90%": df_filtered.quantile(0.90),
}

# 3. Estatísticas descritivas para 'Employees' e 'Valuation (M USD)'
for col in ['Employees', 'Valuation (M USD)']:
    print(f"\nEstatísticas para: {col}")
    print(f"Média: {df_filtered[col].mean():.2f}")
    print(f"Mediana: {df_filtered[col].median():.2f}")
    print(f"Moda: {df_filtered[col].mode().iloc[0]:.2f}")
    print(f"Desvio padrão: {df_filtered[col].std():.2f}")
    print(f"Percentil 25%: {df_filtered[col].quantile(0.25):.2f}")
    print(f"Percentil 50% (mediana): {df_filtered[col].quantile(0.50):.2f}")
    print(f"Percentil 75%: {df_filtered[col].quantile(0.75):.2f}")
    print(f"Percentil 90%: {df_filtered[col].quantile(0.90):.2f}")
    
# Transformando em DataFrame para melhor visualização
stats_df = pd.DataFrame(stats_summary)

# Criando o scatter plot com linha de tendência
plt.figure(figsize=(10, 6))
sns.regplot(data=df_filtered, x="Employees", y="Valuation (B USD)", scatter_kws={"s": 60, "alpha": 0.7}, line_kws={"color": "red"})
plt.title("Relação entre Número de Funcionários e Valuation (em bilhões USD)")
plt.xlabel("Número de Funcionários")
plt.ylabel("Valuation (Bilhões USD)")
plt.grid(True)
plt.tight_layout()

stats_df, plt.show()