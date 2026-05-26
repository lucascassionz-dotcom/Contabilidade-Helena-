import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (Para ficar bonito no celular) ---
st.set_page_config(
    page_title="Oráculo Helena & Lidiane", 
    page_icon="🪡", 
    layout="centered"
)

# --- ESTILIZAÇÃO CSS PARA CORES ---
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS (Custos Fixos) ---
CUSTOS_FIXOS = {
    "Pró-Labore (Dona Helena)": 4400.00,
    "Salário (Lidiane)": 1540.00,
    "Energia Elétrica": 500.00,
    "Água": 200.00,
    "Internet": 160.00,
    "Honorários Contador": 120.00,
    "Guia do MEI": 80.00,
    "Aluguel Máquina Sunrise": 220.00,
    "IPTU Proporcional": 23.33,
}
