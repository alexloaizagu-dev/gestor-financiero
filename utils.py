import pandas as pd


# ==========================================
# FORMATO MONEDA
# ==========================================

def formato_moneda(valor):

    return f"${valor:,.0f}"


# ==========================================
# VALIDAR TEXTO
# ==========================================

def validar_texto(texto):

    if texto.strip() == "":

        return False

    return True


# ==========================================
# VALIDAR MONTO
# ==========================================

def validar_monto(valor):

    if valor <= 0:

        return False

    return True


# ==========================================
# FILTRAR MOVIMIENTOS
# ==========================================

def filtrar_movimientos(

    df,
    tipo,
    categoria,
    busqueda,
    fecha_inicio,
    fecha_fin
):

    df_filtrado = df.copy()

    # ==========================================
    # FILTRO TIPO
    # ==========================================

    if tipo != "Todos":

        df_filtrado = df_filtrado[
            df_filtrado["Tipo"] == tipo
        ]

    # ==========================================
    # FILTRO CATEGORÍA
    # ==========================================

    if categoria != "Todas":

        df_filtrado = df_filtrado[
            df_filtrado["Categoría"]
            == categoria
        ]

    # ==========================================
    # FILTRO BÚSQUEDA
    # ==========================================

    if busqueda:

        df_filtrado = df_filtrado[
            df_filtrado["Descripción"]
            .str.contains(
                busqueda,
                case=False,
                na=False
            )
        ]

    # ==========================================
    # FILTRO FECHAS
    # ==========================================

    df_filtrado = df_filtrado[

        (
            df_filtrado["Fecha"].dt.date
            >= fecha_inicio
        )

        &

        (
            df_filtrado["Fecha"].dt.date
            <= fecha_fin
        )
    ]

    return df_filtrado


# ==========================================
# RESUMEN FINANCIERO
# ==========================================

def resumen_financiero(df):

    ingresos = df[
        df["Tipo"] == "Ingreso"
    ]["Monto"].sum()

    egresos = df[
        df["Tipo"] == "Egreso"
    ]["Monto"].sum()

    balance = ingresos - egresos

    return {

        "ingresos": ingresos,
        "egresos": egresos,
        "balance": balance
    }