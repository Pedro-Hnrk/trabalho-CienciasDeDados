# Reimportar bibliotecas após reset de ambiente
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file_path = "startup_data.csv"
df = pd.read_csv(file_path)

# Filtrar startups não lucrativas
nao_lucrativas = df[df['Profitable'] == 0]

# Identificar outliers (receita acima do percentil 90)
p90_nao_lucrativas = nao_lucrativas['Revenue (M USD)'].quantile(0.90)
outliers = nao_lucrativas[nao_lucrativas['Revenue (M USD)'] > p90_nao_lucrativas]

# Plotar
plt.figure(figsize=(10,6))
sns.scatterplot(data=nao_lucrativas, x=nao_lucrativas.index, y='Revenue (M USD)', label='Não lucrativas', color='blue')
sns.scatterplot(data=outliers, x=outliers.index, y='Revenue (M USD)', label='Outliers', color='red', s=100, marker='X')

plt.axhline(p90_nao_lucrativas, color='gray', linestyle='--', label='Percentil 90')
plt.title('Outliers de Receita entre Startups Não Lucrativas')
plt.xlabel('Índice da Startup')
plt.ylabel('Receita (milhões USD)')
plt.legend()
plt.tight_layout()
plt.show()
