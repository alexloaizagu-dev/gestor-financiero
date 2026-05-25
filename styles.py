import streamlit as st


# ==========================================
# ESTILOS PERSONALIZADOS
# ==========================================

def aplicar_estilos():

    st.markdown("""

    <style>

    /* ==========================================
    FONDO GENERAL
    ========================================== */

    .stApp {

        background-color: #0e1117;
        color: white;
    }

    /* ==========================================
    SIDEBAR
    ========================================== */

    section[data-testid="stSidebar"] {

        background-color: #161b22;
    }

    /* ==========================================
    INPUTS
    ========================================== */

    .stTextInput input,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {

        background-color: #1f2937;
        color: white;
        border-radius: 10px;
    }

    /* ==========================================
    BOTONES
    ========================================== */

    .stButton button {

        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }

    .stButton button:hover {

        background-color: #1d4ed8;
        color: white;
    }

    /* ==========================================
    MÉTRICAS
    ========================================== */

    div[data-testid="metric-container"] {

        background-color: #1e293b;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #334155;
    }

    /* ==========================================
    TABS
    ========================================== */

    button[data-baseweb="tab"] {

        font-size: 16px;
        font-weight: bold;
    }

    /* ==========================================
    DATAFRAME
    ========================================== */

    .stDataFrame {

        border-radius: 10px;
    }

    /* ==========================================
    TÍTULOS
    ========================================== */

    h1, h2, h3 {

        color: white;
    }

    </style>

    """,

    unsafe_allow_html=True
    )