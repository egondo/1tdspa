import streamlit as st

def transforma_palavra(palavra: str, descoberto: list) -> str:
    resposta = ''
    i = 0
    while i < len(palavra):
        if descoberto[i]:
            resposta = resposta + palavra[i] + ' '
        else:
            resposta = resposta + '_ '
        i = i + 1 #i += 1
    return resposta

def busca_letra(palavra: str, letra: str, descoberto: list) -> bool:
    i = 0
    encontrou = False
    while i < len(palavra):
        if letra == palavra[i]:
            descoberto[i] = True
            encontrou = True
        i = i + 1
    return encontrou

def descobriu_palavra(descoberto: list) -> bool:
    for valor in descoberto:
        if valor == False:
            return False
    
    return True


if not "palavra" in st.session_state:
    st.session_state.palavra = 'abacaxi'
    qtd = len(st.session_state.palavra)
    st.session_state.descoberto = [False] * qtd
    st.session_state.erros = 0

st.header("Jogo da Forca")
st.image(f"{st.session_state.erros}.png")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    letra = st.text_input("Letra: ", max_chars=1)
    if not busca_letra(st.session_state.palavra, letra, st.session_state.descoberto):
        st.session_state.erros = st.session_state.erros + 1
        
tracejado = transforma_palavra(st.session_state.palavra, st.session_state.descoberto)
st.code(tracejado)

if st.session_state.erros > 6:
    st.write(f"Você perdeu, a palavra era {st.session_state.palavra}")

if descobriu_palavra(st.session_state.descoberto):
    st.write(f"Parabéns, vc acertou e errou {st.session_state.erros} vezes")







