import sqlite3


# ==========================================
# CONEXIÓN
# ==========================================

def conectar():

    conexion = sqlite3.connect(

        "finanzas.db",

        check_same_thread=False
    )

    return conexion


# ==========================================
# CREAR TABLAS
# ==========================================

def crear_tablas():

    conexion = conectar()

    cursor = conexion.cursor()

    # ==========================================
    # TABLA CATEGORÍAS
    # ==========================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS categorias (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        tipo TEXT NOT NULL
    )

    """)

    # ==========================================
    # TABLA MOVIMIENTOS
    # ==========================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS movimientos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        tipo TEXT NOT NULL,

        monto REAL NOT NULL,

        categoria TEXT NOT NULL,

        descripcion TEXT NOT NULL,

        fecha TEXT NOT NULL
    )

    """)

    # ==========================================
    # TABLA PRESUPUESTO
    # ==========================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS presupuesto (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        valor REAL NOT NULL
    )

    """)

    conexion.commit()

    # ==========================================
    # INSERTAR CATEGORÍAS
    # ==========================================

    cursor.execute(
        "SELECT COUNT(*) FROM categorias"
    )

    total = cursor.fetchone()[0]

    if total == 0:

        categorias_iniciales = [

            ("Salario", "Ingreso"),
            ("Freelance", "Ingreso"),
            ("Inversiones", "Ingreso"),
            ("Ventas", "Ingreso"),

            ("Arriendo", "Egreso"),
            ("Mercado", "Egreso"),
            ("Transporte", "Egreso"),
            ("Salud", "Egreso"),
            ("Entretenimiento", "Egreso"),
            ("Educación", "Egreso")
        ]

        cursor.executemany("""

        INSERT INTO categorias
        (nombre, tipo)

        VALUES (?, ?)

        """, categorias_iniciales)

        conexion.commit()

    conexion.close()


# ==========================================
# OBTENER CATEGORÍAS
# ==========================================

def obtener_categorias(tipo):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT nombre

    FROM categorias

    WHERE tipo = ?

    ORDER BY nombre

    """, (tipo,))

    datos = cursor.fetchall()

    conexion.close()

    return [x[0] for x in datos]


# ==========================================
# AGREGAR CATEGORÍA
# ==========================================

def agregar_categoria(nombre, tipo):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    INSERT INTO categorias
    (nombre, tipo)

    VALUES (?, ?)

    """, (nombre, tipo))

    conexion.commit()

    conexion.close()


# ==========================================
# ELIMINAR CATEGORÍA
# ==========================================

def eliminar_categoria(nombre):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    DELETE FROM categorias

    WHERE nombre = ?

    """, (nombre,))

    conexion.commit()

    conexion.close()


# ==========================================
# INSERTAR MOVIMIENTO
# ==========================================

def insertar_movimiento(

    tipo,
    monto,
    categoria,
    descripcion,
    fecha
):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    INSERT INTO movimientos (

        tipo,
        monto,
        categoria,
        descripcion,
        fecha
    )

    VALUES (?, ?, ?, ?, ?)

    """, (

        tipo,
        monto,
        categoria,
        descripcion,
        fecha
    ))

    conexion.commit()

    conexion.close()


# ==========================================
# OBTENER MOVIMIENTOS
# ==========================================

def obtener_movimientos():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT *

    FROM movimientos

    ORDER BY fecha DESC

    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


# ==========================================
# ACTUALIZAR MOVIMIENTO
# ==========================================

def actualizar_movimiento(

    id_movimiento,
    tipo,
    monto,
    categoria,
    descripcion
):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    UPDATE movimientos

    SET

        tipo = ?,
        monto = ?,
        categoria = ?,
        descripcion = ?

    WHERE id = ?

    """, (

        tipo,
        monto,
        categoria,
        descripcion,
        id_movimiento
    ))

    conexion.commit()

    conexion.close()


# ==========================================
# ELIMINAR MOVIMIENTO
# ==========================================

def eliminar_movimiento(id_movimiento):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    DELETE FROM movimientos

    WHERE id = ?

    """, (id_movimiento,))

    conexion.commit()

    conexion.close()


# ==========================================
# PRESUPUESTO
# ==========================================

def guardar_presupuesto(valor):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM presupuesto"
    )

    cursor.execute("""

    INSERT INTO presupuesto
    (valor)

    VALUES (?)

    """, (valor,))

    conexion.commit()

    conexion.close()


def obtener_presupuesto():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT valor

    FROM presupuesto

    LIMIT 1

    """)

    dato = cursor.fetchone()

    conexion.close()

    if dato:

        return dato[0]

    return 0