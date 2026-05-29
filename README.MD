# 💰 Mis Finanzas - Gestor Financiero Profesional

Aplicación web interactiva desarrollada en **Python** para la gestión, control y análisis de finanzas personales. Este proyecto nació como un prototipo lógico de consola en Google Colab y evolucionó hacia una solución modular con interfaz gráfica moderna utilizando **Streamlit** y almacenamiento relacional con **SQLite3**.

---

## 🚀 Evolución del Proyecto

El desarrollo se estructuró en tres fases secuenciales:
1. **Fase 1 (Prototipo Lógico):** Creación del núcleo del programa en **Google Colab** utilizando Programación Orientada a Objetos (POO), colecciones dinámicas y lógica de persistencia en archivos de texto.
2. **Fase 2 (Diseño y Arquitectura):** Modelado del negocio, objetivos de control de gastos y proyecciones de escalabilidad (SaaS) presentados de forma ejecutiva.
3. **Fase 3 (Producto Final):** Migración del motor lógico a una interfaz web dinámica con **Streamlit**, base de datos relacional robusta en local y dashboards analíticos visuales.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Interfaz de Usuario:** Streamlit (Layout Wide customizado)
* **Base de Datos:** SQLite3 (Persistencia relacional con hilos habilitados)
* **Análisis de Datos:** Pandas (Tratamiento de dataframes y parseo de fechas)
* **Exportación:** Openpyxl / xlsxwriter (Generación de reportes limpios a Excel)

---

## 📦 Estructura de Archivos del Proyecto

El repositorio está organizado bajo una arquitectura modular limpia:

```text
mis-finanzas-app/
├── 📁 .streamlit/
│   └── config.toml                # Configuración visual y paleta de colores de la app
├── 📁 docs/
│   └── Presentacion_Mis_Finanzas.pdf # Diápositivas del proyecto con objetivos y pruebas
├── 📁 notebooks/
│   └── Programa_contabilidad.ipynb  # Código del prototipo inicial de consola en Colab
├── 📄 app.py                      # Interfaz web principal, manejo de pestañas (Tabs) y formularios
├── 📄 database.py                 # Capa de datos, consultas SQL, inicialización de tablas y CRUD
├── 📄 dashboard.py                # Componentes visuales de métricas, gráficos e histórico mensual
├── 📄 exportaciones.py            # Lógica de descarga de reportes en formato Excel
├── 📄 styles.py                   # Inyección de estilos CSS personalizados para look executive
└── 📄 requirements.txt            # Lista de dependencias del entorno de ejecución