# 💰 Mis Finanzas - Gestor Financiero Profesional

## 📌 1. Descripción del Proyecto
**"Mis Finanzas"** es una solución tecnológica diseñada para la gestión, control y análisis detallado de finanzas personales. La aplicación permite registrar y categorizar movimientos de dinero con el objetivo de identificar hábitos de consumo, evaluar el estado financiero mensual en tiempo real y promover buenas prácticas en la administración del capital.

Este proyecto representa la evolución completa de un producto de software, partiendo desde un algoritmo lógico conceptual en consola hasta convertirse en una herramienta interactiva modular con interfaz gráfica web y almacenamiento relacional robusto.

---

## 🎯 2. Objetivos del Proyecto

* **Objetivo General:** Desarrollar una aplicación interactiva que permita centralizar el registro de ingresos y egresos, procesar la información de forma dinámica y presentar análisis visuales para la toma de decisiones financieras personales.
* **Objetivos Específicos:**
    * Diseñar un motor lógico inicial basado en Programación Orientada a Objetos (POO) en **Google Colab** usando estructuras dinámicas como la **Lista Enlazada Simple**.
    * Migrar el prototipo de consola hacia una interfaz gráfica de usuario (GUI) web moderna utilizando **Streamlit**.
    * Garantizar la persistencia de la información mediante un sistema de almacenamiento relacional local con **SQLite3**.
    * Facilitar la exportación de datos para análisis externos en formato de hoja de cálculo Excel.

---

## 🧠 3. Propuesta de Solución y Arquitectura Lógica

El proyecto se estructuró bajo una arquitectura modular limpia en **Visual Studio Code**, separando las responsabilidades del sistema:
* **Capa de Interfaz (`app.py`):** Construida con **Streamlit**, maneja la experiencia de usuario mediante pestañas (*Tabs*), formularios de captura e inyección de estilos ejecutivos.
* **Capa de Persistencia (`database.py`):** Controla la conectividad a **SQLite3**, administrando las tablas de la base de datos local (`finanzas.db`).
* **Capa Analítica (`dashboard.py`):** Procesa la información mediante **Pandas** para renderizar métricas clave y gráficos interactivos.
* **Capa de Salida (`exportaciones.py`):** Automatiza la generación de reportes descargables a **Excel**.

---

## 📦 4. Estructura del Repositorio

```text
mis-finanzas-app/
├── 📁 .streamlit/
│   └── config.toml                # Configuración de la paleta de colores y entorno web
├── 📁 docs/
│   └── Presentacion_Mis_Finanzas.pdf # Diápositivas ejecutivas del proyecto (Objetivos y Pruebas)
├── 📁 notebooks/
│   └── Programa_contabilidad.ipynb  # Código fuente del prototipo inicial de consola (Colab)
├── 📄 app.py                      # Interfaz gráfica principal y flujos del usuario (Streamlit)
├── 📄 database.py                 # Conectividad SQL, inicialización de tablas y operaciones CRUD
├── 📄 dashboard.py                # Lógica de procesamiento de gráficos y métricas analíticas
├── 📄 exportaciones.py            # Motor de exportación de reportes a formato XLSX
├── 📄 styles.py                   # Estilos visuales personalizados para la interfaz
└── 📄 requirements.txt            # Archivo de dependencias del proyecto

5. Características y Funcionalidades de la App
Gestión Inteligente de Movimientos: Formulario dinámico con carga automática de categorías según el tipo seleccionado (Ingreso/Egreso). Cuenta con validaciones estrictas en tiempo real que impiden registrar montos negativos o dejar descripciones vacías.

Historial Administrativo con Edición en Lote (CRUD Completo): * Permite buscar, filtrar y modificar múltiples registros simultáneamente gracias a la grilla interactiva st.data_editor, guardando los cambios directamente en la base de datos.

Control de eliminación selectiva de registros mediante su identificador único (ID).

Descarga de Reportes: Botón interactivo para exportar instantáneamente el historial filtrado a un archivo organizado de Excel.

Dashboard de Analítica Financiera: Despliegue automatizado de KPIs (Total Ingresos, Total Gastos, Balance Neto) y gráficos interactivos del resumen mensual del consumo del usuario.

Panel de Configuración: Control de presupuesto mensual tope e interfaz dinámica para añadir o eliminar categorías personalizadas.

🧪 6. Pruebas del Sistema
Prueba de Consistencia en Formularios: Verificación del bloqueo de inserciones incorrectas (valores vacíos o montos menores o iguales a cero).

Prueba de Persistencia Concurrente: Validación de la correcta escritura en la base de datos finanzas.db sin bloquear los hilos de la aplicación web (check_same_thread=False).

Prueba de Reactividad: Confirmación de que los filtros del historial y los gráficos del dashboard se actualizan de forma inmediata al interactuar con la aplicación.

🚀 7. Algunas Mejoras e Ideas Implementadas
Durante el desarrollo desde Google Colab a Visual Studio Code se incluyeron mejoras críticas de rendimiento y diseño:

Transición Estructural: Se pasó de almacenar la información en listas dinámicas en memoria volatil y archivos planos de texto, a un motor relacional en SQLite3 indexado por IDs únicos.

Interfaz Profesional: Se reemplazó el menú de texto en consola por un entorno web interactivo con diseño responsivo, limpio y de estilo ejecutivo.

Optimización Analítica: Integración de la librería Pandas para agrupar, procesar y estructurar grandes volúmenes de movimientos financieros en milisegundos.

📈 8. Proyecciones a Futuro (Hacia un Modelo SaaS)
La aplicación está diseñada con una arquitectura modular lista para escalar hacia las siguientes metas comerciales y técnicas:

A. Módulo de Gestión de Deudas y Recordatorios 🚨 (Próxima Implementación)
Apartado de Deudas: Creación de una nueva pestaña dedicada exclusivamente al control de cuentas por pagar y cuentas por cobrar.

Sistema de Alertas: Integración de notificaciones automáticas y recordatorios visuales en la interfaz que le avisen al usuario los días previos a la fecha de vencimiento de un compromiso financiero para evitar recargos.

B. Infraestructura en la Nube y Multi-Usuario (Multi-Tenant) 🌐
Base de Datos Distribuida: Migrar el archivo local de SQLite3 hacia Supabase en la nube, evitando que los datos sean efímeros o se pierdan al reiniciar el servidor.

Acceso Multi-Usuario Seguro: Implementación de autenticación de usuarios y políticas de seguridad a nivel de fila (Row-Level Security - RLS) para garantizar que múltiples personas puedan usar la aplicación en internet simultáneamente y que cada quien vea estrictamente su propia información (Muro Invisible).

C. Modelo de Negocio SaaS Freemium 💳
Monetización: Acceso gratuito financiado con banners publicitarios discretos (Google AdSense) y una suscripción Premium mensual económica para desbloquear funciones avanzadas (como la eliminación de anuncios y la futura conciliación bancaria automática).

🎓 9. Conclusiones
Evolución del Software: Se demostró la viabilidad de transformar un algoritmo conceptual puro basado en estructuras de datos de consola hacia un Producto Mínimo Viable (PMV) de nivel profesional, visual y altamente funcional.

Salud Financiera Basada en Datos: La combinación de programación e interfaces interactivas permite transformar registros cotidianos en información de valor estratégico para el control de gastos y hábitos de consumo.

Escalabilidad Arquitectural: Diseñar de forma modular separa la lógica de negocio de la interfaz, lo que permite añadir nuevas funciones (como el módulo de deudas o bases de datos en la nube) de forma rápida y sin romper el código existente.