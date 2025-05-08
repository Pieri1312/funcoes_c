import streamlit as st
from streamlit_sortables import sort_items
import random

# Funções e explicações
funcoes = [
    ["int soma(int a, int b) {", "    int resultado = a + b;", "    return resultado;", "}"],
    ["void imprimeMensagem() {", '    printf("Olá, mundo!\\n");', "}"],
    ["int fatorial(int n) {", "    if(n <= 1) return 1;", "    else return n * fatorial(n - 1);", "}"],
    ["float media(float x, float y) {", "    return (x + y) / 2;", "}"],
    ["int max(int a, int b) {", "    return (a > b) ? a : b;", "}"],
    ["void troca(int *a, int *b) {", "    int temp = *a;", "    *a = *b;", "    *b = temp;", "}"],
    ["void limpaTela() {", '    system("clear");', "}"],
    ["int quadrado(int n) {", "    return n * n;", "}"],
    ["void saudacao(char nome[]) {", '    printf("Olá, %s!\\n", nome);', "}"],
    ["int ehPar(int x) {", "    return x % 2 == 0;", "}"],
]

explicacoes = {
    0: "Retorna a soma de dois números inteiros.",
    1: "Imprime uma mensagem simples na tela.",
    2: "Calcula o fatorial de um número de forma recursiva.",
    3: "Retorna a média entre dois números reais.",
    4: "Retorna o maior valor entre dois inteiros.",
    5: "Troca o valor de dois inteiros usando ponteiros.",
    6: "Limpa a tela do terminal (comando system).",
    7: "Retorna o quadrado de um número.",
    8: "Imprime uma saudação personalizada com nome.",
    9: "Retorna verdadeiro se o número for par.",
}

# Estado
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0
    st.session_state.embaralhada = []

st.title("🧩 Organize a função em C (arraste para ordenar)")

indice = st.session_state.indice

if indice >= len(funcoes):
    st.success(f"Fim do jogo! ✅ Acertos: {st.session_state.acertos} | ❌ Erros: {st.session_state.erros}")
    if st.button("Jogar novamente"):
        st.session_state.indice = 0
        st.session_state.acertos = 0
        st.session_state.erros = 0
        st.session_state.embaralhada = []
    st.stop()

correta = funcoes[indice]

# Só embaralha uma vez
if not st.session_state.embaralhada:
    embaralhada = correta.copy()
    random.shuffle(embaralhada)
    st.session_state.embaralhada = embaralhada
else:
    embaralhada = st.session_state.embaralhada

st.subheader(f"Função {indice + 1}")
st.write("🖱️ Arraste as linhas para colocá-las na ordem correta:")

ordenado = sort_items(embaralhada, direction="vertical")

if st.button("Verificar"):
    if ordenado == correta:
        st.success("✅ Correto!")
        st.session_state.acertos += 1
    else:
        st.error("❌ Errado!")
        st.markdown("**Resposta correta:**")
        for linha in correta:
            st.code(linha, language="c")
        st.session_state.erros += 1

    # Explicação breve
    st.markdown(f"🔎 **Explicação:** {explicacoes[indice]}")
    
    # Avança
    st.session_state.indice += 1
    st.session_state.embaralhada = []
    st.stop()  # pausa para exibir a explicação antes do rerun
