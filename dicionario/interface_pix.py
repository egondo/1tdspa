import streamlit as st

st.subheader("Cadastro de chaves pix")

if not "banco_pix" in st.session_state:
    st.session_state.banco_pix = []

nome = st.text_input("Nome: ")
(col1, col2) = st.columns(2) 
with col1:
    chave = st.text_input("Chave pix: ")
    banco = st.text_input("Banco: ")
    
with col2:
    tipo = st.selectbox("Tipo chave", ['', 'telefone', 'email', 'cpf', 'cnpj'])
    agencia = st.text_input("Agencia: ")
    numero = st.text_input("Conta: ")

if st.button("Cadastra"):
    dado = {"chave": chave, "tipo": tipo, "nome": nome, "banco": banco, "agencia": agencia, "numero": numero}
    st.session_state.banco_pix.append(dado)

    st.write(st.session_state.banco_pix)