import streamlit as st
import pandas as pd
import plotly.express as px

from database import obtener_presupuesto


# ==========================================
# MÉTRICAS
# ==========================================

def mostrar_metricas(df):

    ingresos = df[
        df["Tipo"] == "Ingreso"
    ]["Monto"].sum()

    egresos = df[
        df["Tipo"] == "Egreso"
    ]["Monto"].sum()

    balance = ingresos - egresos

    presupuesto = obtener_presupuesto()

    porcentaje = 0

    if presupuesto > 0:

        porcentaje = (
            egresos / presupuesto
        ) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Ingresos",
        f"${ingresos:,.0f}"
    )

    col2.metric(
        "💸 Egresos",
        f"${egresos:,.0f}"
    )

    col3.metric(
        "🏦 Balance",
        f"${balance:,.0f}"
    )

    col4.metric(
        "📊 Uso presupuesto",
        f"{porcentaje:.1f}%"
    )


# ==========================================
# RESUMEN MENSUAL
# ==========================================

def mostrar_resumen_mensual(df):

    st.subheader(
        "📅 Resumen Mensual"
    )

    fecha_actual = pd.Timestamp.now()

    df_mes = df[
        (
            df["Fecha"].dt.month
            == fecha_actual.month
        )

        &

        (
            df["Fecha"].dt.year
            == fecha_actual.year
        )
    ]

    ingresos_mes = df_mes[
        df_mes["Tipo"] == "Ingreso"
    ]["Monto"].sum()

    egresos_mes = df_mes[
        df_mes["Tipo"] == "Egreso"
    ]["Monto"].sum()

    balance_mes = (
        ingresos_mes - egresos_mes
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "💰 Ingresos del mes",
        f"${ingresos_mes:,.0f}"
    )

    col2.metric(
        "💸 Egresos del mes",
        f"${egresos_mes:,.0f}"
    )

    col3.metric(
        "🏦 Balance del mes",
        f"${balance_mes:,.0f}"
    )


# ==========================================
# DASHBOARD
# ==========================================

def mostrar_dashboard(df):

    st.subheader(
        "📊 Dashboard Financiero"
    )

    col1, col2 = st.columns(2)

    # ==========================================
    # GRÁFICO CATEGORÍAS
    # ==========================================

    with col1:

        df_egresos = df[
            df["Tipo"] == "Egreso"
        ]

        if len(df_egresos) > 0:

            grafico_categoria = px.pie(

                df_egresos,

                names="Categoría",

                values="Monto",

                title="Distribución de gastos",

                hole=0.4,

                color_discrete_sequence=[
                    "#ff6b6b",
                    "#4ecdc4",
                    "#ffe66d",
                    "#1a535c",
                    "#ff9f1c",
                    "#5f27cd"
                ]
            )

            grafico_categoria.update_layout(
                template="plotly_dark"
            )

            st.plotly_chart(
                grafico_categoria,
                use_container_width=True
            )

    # ==========================================
    # INGRESOS VS EGRESOS
    # ==========================================

    with col2:

        resumen = df.groupby(
            "Tipo"
        )["Monto"].sum().reset_index()

        grafico_tipo = px.bar(

            resumen,

            x="Tipo",

            y="Monto",

            color="Tipo",

            title="Ingresos vs Egresos",

            text_auto=True,

            color_discrete_map={

                "Ingreso": "#2ecc71",

                "Egreso": "#e74c3c"
            }
        )

        grafico_tipo.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(
            grafico_tipo,
            use_container_width=True
        )

    # ==========================================
    # EVOLUCIÓN
    # ==========================================

    st.subheader(
        "📈 Evolución Financiera"
    )

    df_ordenado = df.sort_values(
        "Fecha"
    )

    evolucion = df_ordenado.groupby(
        "Fecha"
    )["Monto"].sum().reset_index()

    grafico_linea = px.line(

        evolucion,

        x="Fecha",

        y="Monto",

        markers=True,

        title="Movimientos por fecha"
    )

    grafico_linea.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        grafico_linea,
        use_container_width=True
    )