import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Carregar os dados
df = pd.read_csv("startup_data.csv")

# Filtrar startups fundadas após 2010
filtered_df = df[df['Year Founded'] > 2010].copy()

# Converter Valuation para bilhões de USD
filtered_df['Valuation (B USD)'] = filtered_df['Valuation (M USD)'] / 1000

# Estatísticas descritivas
statistics = {
    'Employees': {
        'mean': filtered_df['Employees'].mean(),
        'median': filtered_df['Employees'].median(),
        'mode': filtered_df['Employees'].mode().iloc[0],
        'std': filtered_df['Employees'].std(),
        '25%': filtered_df['Employees'].quantile(0.25),
        '50%': filtered_df['Employees'].quantile(0.50),
        '75%': filtered_df['Employees'].quantile(0.75),
        '90%': filtered_df['Employees'].quantile(0.90),
    },
    'Valuation (B USD)': {
        'mean': filtered_df['Valuation (B USD)'].mean(),
        'median': filtered_df['Valuation (B USD)'].median(),
        'mode': filtered_df['Valuation (B USD)'].mode().iloc[0],
        'std': filtered_df['Valuation (B USD)'].std(),
        '25%': filtered_df['Valuation (B USD)'].quantile(0.25),
        '50%': filtered_df['Valuation (B USD)'].quantile(0.50),
        '75%': filtered_df['Valuation (B USD)'].quantile(0.75),
        '90%': filtered_df['Valuation (B USD)'].quantile(0.90),
    }
}

# Scatter plot com linha de tendência
plt.figure(figsize=(10, 6))
sns.regplot(data=filtered_df, x='Employees', y='Valuation (B USD)', scatter_kws={}, line_kws={"color": "red"})
plt.title("Relação entre Número de Funcionários e Valuation (Startups fundadas após 2010)")
plt.xlabel("Número de Funcionários")
plt.ylabel("Valuation (Bilhões USD)")
plt.grid(True)
plt.tight_layout()
plt.show()