"""
Script para crear la base de datos SQLite con todas las tablas
"""

import sqlite3

def crear_base_datos():
    """Crea la base de datos y todas las tablas"""
    
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect('predicciones_deportivas.db')
    cursor = conn.cursor()
    
    print("📦 Creando base de datos...")
    
    # 1. Tabla Temporadas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temporada (
            id_temporada INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            estado TEXT DEFAULT 'activa' CHECK (estado IN ('activa', 'finalizada', 'suspendida'))
        )
    """)
    print("✅ Tabla 'temporada' creada")
    
    # 2. Tabla Clubes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS club_deportivo (
            id_club INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            ciudad TEXT,
            estadio TEXT,
            año_fundacion INTEGER
        )
    """)
    print("✅ Tabla 'club_deportivo' creada")
    
    # 3. Tabla Jugadores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugador (
            id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            posicion_principal TEXT,
            peso_influencia REAL DEFAULT 1.00,
            pie_dominante TEXT
        )
    """)
    print("✅ Tabla 'jugador' creada")
    
    # 4. Tabla Entrenadores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entrenador (
            id_entrenador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            peso_influencia REAL DEFAULT 1.00
        )
    """)
    print("✅ Tabla 'entrenador' creada")
    
    # 5. Tabla Árbitros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arbitro (
            id_arbitro INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            peso_influencia REAL DEFAULT 1.00,
            rol TEXT CHECK (rol IN ('principal', 'asistente', 'auxiliar'))
        )
    """)
    print("✅ Tabla 'arbitro' creada")
    
    # 6. Tabla Jornadas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jornada (
            id_jornada INTEGER PRIMARY KEY AUTOINCREMENT,
            id_temporada INTEGER NOT NULL,
            numero_jornada INTEGER NOT NULL,
            fecha DATE NOT NULL,
            estado TEXT DEFAULT 'programada',
            FOREIGN KEY (id_temporada) REFERENCES temporada(id_temporada)
        )
    """)
    print("✅ Tabla 'jornada' creada")
    
    # 7. Tabla Equipos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipo (
            id_equipo INTEGER PRIMARY KEY AUTOINCREMENT,
            id_club INTEGER NOT NULL,
            nombre_equipo TEXT NOT NULL,
            categoria TEXT DEFAULT 'Primera División',
            FOREIGN KEY (id_club) REFERENCES club_deportivo(id_club)
        )
    """)
    print("✅ Tabla 'equipo' creada")
    
    # 8. Tabla Quinielas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiniela (
            id_quiniela INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jornada INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            fecha_cierre TIMESTAMP NOT NULL,
            FOREIGN KEY (id_jornada) REFERENCES jornada(id_jornada)
        )
    """)
    print("✅ Tabla 'quiniela' creada")
    
    # 9. Tabla Encuentros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encuentro (
            id_encuentro INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jornada INTEGER NOT NULL,
            id_equipo_local INTEGER NOT NULL,
            id_equipo_visitante INTEGER NOT NULL,
            fecha_hora TIMESTAMP NOT NULL,
            resultado_local INTEGER,
            resultado_visitante INTEGER,
            FOREIGN KEY (id_jornada) REFERENCES jornada(id_jornada),
            FOREIGN KEY (id_equipo_local) REFERENCES equipo(id_equipo),
            FOREIGN KEY (id_equipo_visitante) REFERENCES equipo(id_equipo)
        )
    """)
    print("✅ Tabla 'encuentro' creada")
    
    # 10. Tabla Encuentros Quiniela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encuentro_quiniela (
            id_encuentro_quiniela INTEGER PRIMARY KEY AUTOINCREMENT,
            id_quiniela INTEGER NOT NULL,
            id_encuentro INTEGER NOT NULL,
            numero_orden INTEGER NOT NULL CHECK (numero_orden BETWEEN 1 AND 15),
            FOREIGN KEY (id_quiniela) REFERENCES quiniela(id_quiniela),
            FOREIGN KEY (id_encuentro) REFERENCES encuentro(id_encuentro)
        )
    """)
    print("✅ Tabla 'encuentro_quiniela' creada")
    
    # 11. Tabla Plantilla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plantilla (
            id_plantilla INTEGER PRIMARY KEY AUTOINCREMENT,
            id_equipo INTEGER NOT NULL,
            id_jugador INTEGER NOT NULL,
            id_temporada INTEGER NOT NULL,
            dorsal INTEGER,
            activo INTEGER DEFAULT 1,
            FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo),
            FOREIGN KEY (id_jugador) REFERENCES jugador(id_jugador),
            FOREIGN KEY (id_temporada) REFERENCES temporada(id_temporada)
        )
    """)
    print("✅ Tabla 'plantilla' creada")
    
    # 12. Tabla Estado Jugador (Biorritmos)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estado_jugador (
            id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jugador INTEGER NOT NULL,
            id_encuentro INTEGER NOT NULL,
            estado_fisico REAL,
            estado_emocional REAL,
            estado_intelectual REAL,
            observaciones TEXT,
            FOREIGN KEY (id_jugador) REFERENCES jugador(id_jugador),
            FOREIGN KEY (id_encuentro) REFERENCES encuentro(id_encuentro)
        )
    """)
    print("✅ Tabla 'estado_jugador' creada")
    
    # 13. Tabla Predicciones
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediccion_encuentro (
            id_prediccion INTEGER PRIMARY KEY AUTOINCREMENT,
            id_encuentro INTEGER NOT NULL,
            probabilidad_local REAL,
            probabilidad_empate REAL,
            probabilidad_visitante REAL,
            pronostico_final TEXT,
            FOREIGN KEY (id_encuentro) REFERENCES encuentro(id_encuentro)
        )
    """)
    print("✅ Tabla 'prediccion_encuentro' creada")
    
    # Guardar cambios
    conn.commit()
    conn.close()
    
    print("\n🎉 ¡Base de datos creada exitosamente!")
    print("📁 Archivo: predicciones_deportivas.db")

if __name__ == "__main__":
    crear_base_datos()