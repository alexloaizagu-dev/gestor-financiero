# 💰 Mis Finanzas - Gestor Financiero Profesional

---

# 📌 1. Descripción del Proyecto

**Mis Finanzas** es una solución tecnológica desarrollada para la gestión, control y análisis detallado de finanzas personales.

La aplicación permite registrar y categorizar movimientos financieros con el objetivo de identificar hábitos de consumo, evaluar el estado financiero mensual en tiempo real y promover buenas prácticas en la administración del dinero.

Este proyecto representa la evolución completa de un producto de software, iniciando desde un algoritmo lógico en consola hasta convertirse en una aplicación web modular, visual e interactiva con almacenamiento relacional robusto.

---

# 🎯 2. Objetivos del Proyecto

## ✅ Objetivo General

Desarrollar una aplicación interactiva que permita centralizar el registro de ingresos y egresos, procesar la información de forma dinámica y presentar análisis visuales para apoyar la toma de decisiones financieras personales.

## ✅ Objetivos Específicos

* Diseñar un motor lógico inicial basado en Programación Orientada a Objetos (POO) utilizando Google Colab.
* Implementar estructuras dinámicas como listas enlazadas simples.
* Migrar el prototipo de consola hacia una interfaz gráfica web moderna utilizando Streamlit.
* Garantizar persistencia de datos mediante SQLite3.
* Facilitar exportación de información financiera en formato Excel.
* Implementar validaciones y controles de errores para mejorar la integridad de los datos.

---

# 🧠 3. Propuesta de Solución y Arquitectura

El proyecto se estructuró bajo una arquitectura modular desarrollada en Visual Studio Code, separando responsabilidades para mejorar escalabilidad, mantenimiento y organización del código.

## 📄 Capa de Interfaz — `app.py`

Construida con Streamlit.

### Responsabilidades

* Formularios interactivos
* Pestañas dinámicas
* Captura de datos
* Validaciones visuales
* Navegación del usuario
* Integración entre módulos

---

## 🗃️ Capa de Persistencia — `database.py`

Módulo encargado de la gestión de datos utilizando SQLite3.

### Funciones principales

* Creación de tablas
* Inserción de movimientos
* Actualización de registros
* Eliminación de registros
* Administración de categorías
* Gestión de presupuesto mensual

---

## 📊 Capa Analítica — `dashboard.py`

Procesa la información mediante Pandas para generar:

* KPIs financieros
* Métricas automáticas
* Gráficas interactivas
* Resúmenes mensuales

---

## 📁 Capa de Exportación — `exportaciones.py`

Permite generar archivos Excel descargables con la información filtrada del historial financiero.

---

# 📦 4. Estructura del Repositorio

```text
mis-finanzas-app/
│
├── 📁 .streamlit/
│   └── config.toml
│
├── 📁 docs/
│   └── Presentacion_Mis_Finanzas.pdf
│
├── 📁 notebooks/
│   └── Programa_contabilidad.ipynb
│
├── 📄 app.py
├── 📄 database.py
├── 📄 dashboard.py
├── 📄 exportaciones.py
├── 📄 styles.py
├── 📄 utils.py
│
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore
```

---

# ⚙️ 5. Funcionalidades Principales

## 💵 Gestión Inteligente de Movimientos

* Registro dinámico de ingresos y egresos.
* Carga automática de categorías según el tipo seleccionado.
* Validaciones estrictas para evitar:

  * Montos negativos
  * Campos vacíos
  * Datos inválidos

---

## 📋 Historial Administrativo (CRUD Completo)

El sistema permite:

* Buscar movimientos
* Filtrar información
* Editar múltiples registros
* Eliminar movimientos
* Actualizar información en tiempo real

Utilizando:

* `st.data_editor`
* SQLite3
* DataFrames de Pandas

---

## 📥 Exportación de Reportes

* Descarga automática del historial financiero en formato Excel (`.xlsx`).
* Exportación filtrada según la información visualizada.

---

## 📊 Dashboard Financiero

Visualización automática de:

* Total de ingresos
* Total de egresos
* Balance neto
* Resumen mensual
* Gráficas financieras

---

## ⚙️ Panel de Configuración

* Gestión de presupuesto mensual.
* Creación dinámica de categorías.
* Eliminación de categorías personalizadas.

---

# 🧪 6. Pruebas del Sistema

## ✅ Prueba de Validación de Formularios

Verificación de restricciones para impedir:

* Valores vacíos
* Montos menores o iguales a cero
* Selecciones inválidas

---

## ✅ Prueba de Persistencia Concurrente

Validación de escritura y lectura correcta en SQLite3 utilizando:

```python
check_same_thread=False
```

Esto evita bloqueos concurrentes en la aplicación web.

---

## ✅ Prueba de Reactividad

Confirmación de actualización inmediata en:

* Dashboard
* Historial
* Filtros
* Métricas
* Gráficas

---

# 🚀 7. Mejoras Implementadas Durante el Desarrollo

## 🔄 Transición Estructural

El proyecto evolucionó desde:

* Listas dinámicas en memoria
* Archivos planos `.txt`

Hacia:

* SQLite3
* Persistencia relacional
* IDs únicos
* Arquitectura modular

---

## 🎨 Interfaz Profesional

Se reemplazó el entorno de consola por:

* Interfaz web interactiva
* Diseño moderno
* Experiencia visual amigable
* Navegación dinámica

---

## ⚡ Optimización Analítica

Integración de:

* Pandas
* Procesamiento de datos
* Métricas automáticas
* Resúmenes financieros rápidos

---

# 📈 8. Proyecciones a Futuro

## 🚨 A. Gestión de Deudas y Recordatorios

Implementar:

* Control de cuentas por pagar
* Recordatorios automáticos
* Alertas visuales
* Fechas de vencimiento

---

## 🌐 B. Infraestructura en la Nube

Migrar SQLite3 hacia Supabase para:

* Evitar pérdida de información
* Tener persistencia en la nube
* Permitir acceso desde internet

---

## 👥 C. Sistema Multiusuario

Implementar:

* Inicio de sesión
* Autenticación segura
* Seguridad por usuario
* Políticas Row-Level Security (RLS)

---

## 💳 D. Modelo SaaS Freemium

Posible implementación de:

* Plan gratuito con anuncios
* Suscripción premium
* Funciones avanzadas
* Reportes automáticos
* Integraciones financieras

---

# 🎓 9. Conclusiones

## ✅ Evolución del Software

El proyecto demuestra cómo una solución lógica desarrollada inicialmente en consola puede evolucionar hacia una aplicación web moderna, profesional y modular.

---

## ✅ Aplicación de Conocimientos

Durante el desarrollo se aplicaron conocimientos de:

* Programación Orientada a Objetos
* Manejo de excepciones
* Arquitectura modular
* Persistencia de datos
* Desarrollo web
* Visualización de información
* Bases de datos relacionales

---

## ✅ Escalabilidad

La separación modular del sistema permite agregar nuevas funcionalidades sin afectar el funcionamiento actual de la aplicación.

---

# 🛠️ 10. Tecnologías Utilizadas

* Python
* Streamlit
* SQLite3
* Pandas
* OpenPyXL
* Visual Studio Code
* Google Colab

---

# ▶️ 11. Ejecución del Proyecto

## 1️⃣ Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Ejecutar aplicación

```bash
streamlit run app.py
```

---

# 📦 12. requirements.txt

```txt
streamlit
pandas
openpyxl
plotly
```

---

# 🚫 13. Archivo .gitignore

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
.env
venv/
```

---

# 👨‍💻 14. Autor

**Alexander Loaiza Guapacha**

---

# ⭐ 15. Resultado Final

El proyecto final incluye:

* Aplicación web funcional
* Persistencia de datos
* Dashboard financiero
* Exportación Excel
* Arquitectura modular
* Interfaz moderna
* Validaciones robustas
* Base académica sólida
* Escalabilidad futura

---

# 🙌 Gracias por revisar el proyecto
