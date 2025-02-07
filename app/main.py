import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Título
st.title("Previsão de Preços de Casas")

# Entrada do usuário
st.sidebar.header("Configurações")
numDados = st.sidebar.slider("Número de Dados", 50, 500, 100)

# Criação de dados fictícios (tamanho da casa vs preço)
np.random.seed(42)
X = 2 * np.random.rand(numDados, 1)  # Tamanho da casa (m²)
y = 4 + 3 * X + np.random.randn(numDados, 1)

# Divisão dos dados entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazendo previsões
y_pred = modelo.predict(X_test)

# Exibir coeficientes
st.write(f"Coeficiente angular (inclinação): {modelo.coef_[0][0]:.2f}")
st.write(f"Intercepto: {modelo.intercept_[0]:.2f}")

# Criar gráfico
fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color="blue", label="Dados reais")
ax.plot(X_test, y_pred, color="red", linewidth=2, label="Previsões")
ax.set_xlabel("Tamanho da casa (m²)")
ax.set_ylabel("Preço")
ax.legend()

# Exibir gráfico através do Streamlit
st.pyplot(fig)