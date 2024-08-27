import pandas as pd
import numpy as np

# Gerar dados simulados
np.random.seed(0)
n_samples = 100
renda = np.random.normal(loc=50000, scale=15000, size=n_samples)
compras = np.random.normal(loc=10, scale=5, size=n_samples)

# Criar DataFrame
df = pd.DataFrame({
    'Renda': renda,
    'Número de Compras': compras
})

# Salvar DataFrame em um arquivo CSV
df.to_csv('clientes.csv', index=False)
