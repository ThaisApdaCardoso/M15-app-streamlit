# Código para seu app Streamlit
import streamlit as st
import pandas as pd
import numpy as np
import time

# Título do App
st.title("Meu Primeiro Projeto no Streamlit")

# Descrição
st.write("Este é meu primeiro app criado com Streamlit Cloud!")

# Tabela interativa
data = pd.DataFrame({
    'Nomes': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Idades': [25, 30, 35, 40],
    'Pontuações': [90, 85, 78, 92]
})
st.write("Aqui está uma tabela de exemplo:")
st.dataframe(data)

# Slider interativo
idade_minima = st.slider("Filtrar pela idade mínima:", 20, 50, 25)
st.write(f"Idade mínima selecionada: {idade_minima}")
st.write("Tabela filtrada:")
st.dataframe(data[data['Idades'] >= idade_minima])

# Gráfico simples
grafico_data = np.random.randn(50, 2)
st.write("Gráfico gerado aleatoriamente:")
st.line_chart(grafico_data)

# Função de Upload de Arquivo
uploaded_file = st.file_uploader("input_M15_SINASC_RO_2019.csv", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# Exibir Imagem
image = st.file_uploader("good-luck.png", type=["jpg", "png", "jpeg"])
if image is not None:
    st.image(image, caption='Imagem carregada com sucesso!', use_column_width=True)

# Filtro de Tabela
idade_filtro = st.selectbox("Escolha a faixa etária:", options=["Todos", "20-30", "31-40"])
if idade_filtro == "20-30":
    st.write(data[data["Idades"].between(20, 30)])
elif idade_filtro == "31-40":
    st.write(data[data["Idades"].between(31, 40)])
else:
    st.write(data)

# Exibir Box de Texto
texto_usuario = st.text_input("Digite seu nome:")
st.write(f"Olá, {texto_usuario}!")

# Exibir Botão de Confirmar
if st.button('Confirmar'):
    st.write('Você clicou no botão de confirmar!')

# Exibir Barra de Progresso
st.write("Progresso:")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.1)

# Exibir Seleção de Data
data_selecionada = st.date_input("Escolha uma data:")
st.write(f"Data selecionada: {data_selecionada}")

# Exibir Entrada de Número
numero_usuario = st.number_input("Escolha um número:", min_value=0, max_value=100, step=1)
st.write(f"O número selecionado é: {numero_usuario}")

# Exibir Caixa de Seleção
opcoes = st.multiselect("Escolha suas frutas favoritas:", ["Maçã", "Banana", "Laranja", "Morango", "Uva"])
st.write(f"Você escolheu: {opcoes}")

# Exibir Código
codigo = '''import streamlit as st
import pandas as pd
data = pd.read_csv('meu_arquivo.csv')
st.write(data)'''
st.code(codigo, language='python')

# Exibir um Gráfico Interativo
st.write("Gráfico Interativo:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Exibir Notificação
if idade_minima > 30:
    st.success("Idade acima de 30 anos!")
else:
    st.warning("Idade abaixo de 30 anos!")

# Função para Exibir Texto Estilizado
st.markdown("### Texto com markdown estilizado")
st.markdown("Aqui é possível adicionar **negrito**, *itálico*, e outros elementos de formatação.")

# Caixa de Seleção para Múltiplas Opções
opcoes_multiselect = st.multiselect("Escolha suas opções:", ["Opção 1", "Opção 2", "Opção 3", "Opção 4"])
st.write(f"Você escolheu as opções: {opcoes_multiselect}")

# Exibir Tabela Estilizada com Pandas
st.write("Tabela estilizada com Pandas:")
st.dataframe(data.style.highlight_max(axis=0))
