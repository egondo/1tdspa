import streamlit as st

#para resolver o problema da inicializacao temos o session_state
#ele armazena os objetos na sessão do usuário (parecido com cookies)
#veja abaixo a solução

if not "turmas" in st.session_state:
    st.session_state.turmas = {}

rm = st.number_input("RM: ")
cp1 = st.number_input("CP1")
cp2 = st.number_input("CP2")
cp3 = st.number_input("CP3")
sp1 = st.number_input("Sprint 1")
sp2 = st.number_input("Sprint 2")
gs = st.number_input("Global")

if st.button("inclui"):
    aluno = {
        "rm": rm, "cp1": cp1, "cp2": cp2, "cp3": cp3, "sprint1": sp1, "sprint2": sp2,
        "global": gs    
    }
    st.session_state.turmas[rm] = aluno
    st.write(st.session_state.turmas)