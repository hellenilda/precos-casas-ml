import numpy as np
import pandas as pd

# Definir a semente para reprodutibilidade
np.random.seed(42)

# Gerar tamanhos de casas (em m²) entre 50 e 300
tamanhos = np.random.randint(50, 300, size=100)

# Gerar preços com base no tamanho + ruído aleatório
precos = 50000 + tamanhos * 1500 + np.random.randint(-20000, 20000, size=100)

# Criar DataFrame
df = pd.DataFrame({"Tamanho (m²)": tamanhos, "Preço (R$)": precos})

# Salvar como CSV
df.to_csv("dataset_casas.csv", index=False)

# Exibir as primeiras linhas
print(df.head())
