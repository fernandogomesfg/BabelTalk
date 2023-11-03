import streamlit as st
import requests
from googletrans import Translator

# Variável global para armazenar a frase actual
frase_atual = ""

# Função para obter uma frase motivacional
def obter_frase():
    url = "https://api.quotable.io/random"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        frase = resposta.json()["content"]
        autor = resposta.json()["author"]
        
        return f"{frase} - {autor}"
    else:
        print("Erro ao buscar a frase")
        return None

# Função para traduzir o texto
def traduzir_texto(texto, idioma_destino):
    tradutor = Translator(service_urls=["translate.google.com"])
    traducao = tradutor.translate(texto, src='en', dest=idioma_destino)
    texto_traduzido = traducao.text
    return texto_traduzido

# Configurações gerais do Streamlit
st.set_page_config(
    page_title="BabelTalk - Frases Motivacionais",
    page_icon="🌍",
    layout="wide",  # Largura total da página
)

# Título do site centralizado
st.markdown("<h1 style='text-align: center;'>😃 BabelTalk 🌍</h1>", unsafe_allow_html=True)

# Sidebar para botões
st.sidebar.header("Opções")
idioma_selecionado = st.sidebar.selectbox("Selecione o Idioma de Tradução:", ["Inglês (en)", "Espanhol (es)", "Francês (fr)", "Português (pt)"])

# Botões no sidebar
if st.sidebar.button("Obter Nova Frase"):
    frase_traduzida = obter_frase()
    if "Espanhol" in idioma_selecionado:
        frase_traduzida = traduzir_texto(frase_traduzida, 'es')
    elif "Francês" in idioma_selecionado:
        frase_traduzida = traduzir_texto(frase_traduzida, 'fr')
    elif "Português" in idioma_selecionado:
        frase_traduzida = traduzir_texto(frase_traduzida, 'pt')
    frase_atual = frase_traduzida  # Armazena a frase atual

# Frase à direita
st.subheader("Frase do Dia:")
if frase_atual:
    st.write(frase_atual)