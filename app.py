import streamlit as st
import pandas as pd
from exportaciones import exportar_excel

from database import (

    crear_tablas,

    insertar_movimiento,
    obtener_movimientos,
    actualizar_movimiento,
    eliminar_movimiento,

    obtener_categorias,
    agregar_categoria,
    eliminar_categoria,

    guardar_presupuesto,
    obtener_presupuesto
)

from dashboard import (

    mostrar_metricas,
    mostrar_dashboard,
    mostrar_resumen_mensual
)

from exportaciones import exportar_excel

from styles import aplicar_estilos


# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(

    page_title="Gestor Financiero",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS
# ==========================================

aplicar_estilos()

# ==========================================
# CREAR TABLAS
# ==========================================

crear_tablas()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("💰 Finanzas")

    st.markdown("---")

    st.info(
        """
        Aplicación profesional
        para gestión financiera.
        """
    )

# ==========================================
# TÍTULO
# ==========================================

st.title("💰 Gestor Financiero Profesional")

# ==========================================
# TABS
# ==========================================

tab1, tab2, tab3, tab4 = st.tabs([

    "➕ Movimientos",
    "📋 Historial",
    "📊 Dashboard",
    "⚙️ Configuración"
])

# =====================================================
# TAB 1
# =====================================================

# =====================================================
# TAB 1
# =====================================================

with tab1:

    if "mensaje_guardado" not in st.session_state:
        st.session_state.mensaje_guardado = False

    if st.session_state.mensaje_guardado:

        st.success(
            "Movimiento guardado correctamente"
        )

        st.session_state.mensaje_guardado = False

    st.header("Agregar Movimiento")

    # ==========================================
    # FORMULARIO
    # ==========================================

    with st.form(
        "form_movimiento",
        clear_on_submit=True
    ):

        # ==========================================
        # TIPO
        # ==========================================

        tipo = st.selectbox(
            "Tipo",
            [
                "Seleccione",
                "Ingreso",
                "Egreso"
            ]
        )

        # ==========================================
        # CATEGORÍAS DINÁMICAS
        # ==========================================

        categorias = []

        if tipo != "Seleccione":

            categorias = obtener_categorias(tipo)

        # ==========================================
        # COLUMNAS
        # ==========================================

        col1, col2 = st.columns(2)

        with col1:

            monto = st.number_input(
                "Monto",
                min_value=0.0,
                step=1000.0,
                value=0.0
            )

            fecha = st.date_input(
                "Fecha"
            )

        with col2:

            categoria = st.selectbox(
                "Categoría",
                ["Seleccione"] + categorias
            )

            descripcion = st.text_input(
                "Descripción"
            )

        # ==========================================
        # BOTÓN
        # ==========================================

        guardar = st.form_submit_button(
            "Guardar Movimiento"
        )

        # ==========================================
        # VALIDACIONES
        # ==========================================

        if guardar:

            if tipo == "Seleccione":

                st.warning(
                    "Debes seleccionar un tipo"
                )

            elif categoria == "Seleccione":

                st.warning(
                    "Debes seleccionar una categoría"
                )

            elif monto <= 0:

                st.warning(
                    "El monto debe ser mayor a cero"
                )

            elif descripcion.strip() == "":

                st.warning(
                    "Debes ingresar una descripción"
                )

            else:

                insertar_movimiento(
                    tipo,
                    monto,
                    categoria,
                    descripcion,
                    str(fecha)
                )

                st.session_state.mensaje_guardado = True

                st.rerun()

# =====================================================
# OBTENER DATOS
# =====================================================

datos = obtener_movimientos()

if len(datos) > 0:

    df = pd.DataFrame(

        datos,

        columns=[
            "ID",
            "Tipo",
            "Monto",
            "Categoría",
            "Descripción",
            "Fecha"
        ]
    )

    df["Fecha"] = pd.to_datetime(
        df["Fecha"],
        format="mixed"
    )

else:

    df = pd.DataFrame(
        columns=[
            "ID",
            "Tipo",
            "Monto",
            "Categoría",
            "Descripción",
            "Fecha"
        ]
    )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    st.subheader("Historial de Movimientos")

    if len(df) > 0:

        # ==========================================
        # FILTROS
        # ==========================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            filtro_tipo = st.selectbox(
                "Tipo",
                [
                    "Todos",
                    "Ingreso",
                    "Egreso"
                ]
            )

        with col2:

            filtro_categoria = st.selectbox(
                "Categoría",
                [
                    "Todas"
                ] + list(
                    df["Categoría"].unique()
                )
            )

        with col3:

            fecha_inicio = st.date_input(
                "Fecha inicial",
                value=df["Fecha"].min().date()
            )

        with col4:

            fecha_fin = st.date_input(
                "Fecha final",
                value=df["Fecha"].max().date()
            )

        busqueda = st.text_input(
            "Buscar descripción"
        )

        # ==========================================
        # FILTRAR
        # ==========================================

        df_filtrado = df.copy()

        if filtro_tipo != "Todos":

            df_filtrado = df_filtrado[
                df_filtrado["Tipo"]
                == filtro_tipo
            ]

        if filtro_categoria != "Todas":

            df_filtrado = df_filtrado[
                df_filtrado["Categoría"]
                == filtro_categoria
            ]

        if busqueda:

            df_filtrado = df_filtrado[
                df_filtrado["Descripción"]
                .str.contains(
                    busqueda,
                    case=False,
                    na=False
                )
            ]

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

        # ==========================================
        # TABLA
        # ==========================================

        tabla = st.data_editor(

            df_filtrado,

            use_container_width=True,

            hide_index=True,

            disabled=[
                "ID",
                "Fecha"
            ]
        )

        # ==========================================
        # BOTONES
        # ==========================================

        col1, col2 = st.columns(2)

        with col1:

            if st.button("💾 Guardar cambios"):

                for _, fila in tabla.iterrows():

                    actualizar_movimiento(

                        fila["ID"],
                        fila["Tipo"],
                        fila["Monto"],
                        fila["Categoría"],
                        fila["Descripción"]
                    )

                st.success(
                    "Cambios guardados"
                )

                st.rerun()

        with col2:

            excel = exportar_excel(
                df_filtrado
            )

            st.download_button(

                label="⬇️ Descargar Excel",

                data=excel,

                file_name="movimientos.xlsx",

                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        # ==========================================
        # ELIMINAR
        # ==========================================

        st.subheader("🗑️ Eliminar Movimiento")

        opciones = ["Seleccionar"] + list(
            df_filtrado["ID"]
        )

        movimiento = st.selectbox(
            "Movimiento",
            opciones
        )

        if st.button("Eliminar movimiento"):

            if movimiento == "Seleccionar":

                st.warning(
                    "Debes seleccionar un movimiento"
                )

            else:

                eliminar_movimiento(
                    movimiento
                )

                st.success(
                    "Movimiento eliminado"
                )

                st.rerun()

    else:

        st.info(
            "No hay movimientos registrados"
        )

# =====================================================
# TAB 3
# =====================================================

with tab3:

    st.subheader("Dashboard Financiero")

    if len(df) > 0:

        mostrar_metricas(df)

        mostrar_resumen_mensual(df)

        mostrar_dashboard(df)

    else:

        st.info(
            "No existen datos"
        )

# =====================================================
# TAB 4
# =====================================================

with tab4:

    st.subheader("⚙️ Configuración")

    # ==========================================
    # PRESUPUESTO
    # ==========================================

    st.markdown("## 💵 Presupuesto Mensual")

    presupuesto = st.number_input(

        "Definir presupuesto mensual",

        min_value=0.0,

        step=100000.0
    )

    if st.button("Guardar presupuesto"):

        guardar_presupuesto(
            presupuesto
        )

        st.success(
            "Presupuesto guardado"
        )

    presupuesto_actual = obtener_presupuesto()

    st.info(
        f"Presupuesto actual: ${presupuesto_actual:,.0f}"
    )

    # ==========================================
    # CATEGORÍAS
    # ==========================================

    st.markdown("---")

    st.markdown("## 🗂️ Categorías")

    tipo_categoria = st.selectbox(

        "Tipo categoría",

        [
            "Ingreso",
            "Egreso"
        ]
    )

    nueva_categoria = st.text_input(
        "Nueva categoría"
    )

    if st.button("Agregar categoría"):

        if nueva_categoria.strip() == "":

            st.warning(
                "Debes ingresar un nombre"
            )

        else:

            agregar_categoria(
                nueva_categoria,
                tipo_categoria
            )

            st.success(
                "Categoría agregada"
            )

            st.rerun()

    categorias = obtener_categorias(
        tipo_categoria
    )

    categoria_eliminar = st.selectbox(

        "Eliminar categoría",

        categorias
    )

    if st.button("Eliminar categoría"):

        eliminar_categoria(
            categoria_eliminar
        )

        st.success(
            "Categoría eliminada"
        )

        st.rerun()