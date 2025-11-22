"""
Gestor de Base de Datos SQLite - Sistema de Predicciones Deportivas
"""

import sqlite3
from datetime import datetime, date
from typing import List, Dict, Optional

class GestorDB:
    def __init__(self, db_path="predicciones_deportivas.db"):
        """Inicializa el gestor con la ruta de la base de datos"""
        self.db_path = db_path
    
    def _conectar(self):
        """Crea una conexión a la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para obtener resultados como diccionarios
        return conn
    
    # ==================== TEMPORADAS ====================
    
    def insertar_temporada(self, nombre: str, fecha_inicio: str, 
                          fecha_fin: str, estado: str = 'activa') -> int:
        """
        Inserta una nueva temporada
        
        Ejemplo:
            id = db.insertar_temporada("2024-2025", "2024-08-15", "2025-05-30")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO temporada (nombre, fecha_inicio, fecha_fin, estado)
            VALUES (?, ?, ?, ?)
        """, (nombre, fecha_inicio, fecha_fin, estado))
        
        id_temporada = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Temporada '{nombre}' creada con ID: {id_temporada}")
        return id_temporada
    
    def obtener_temporadas(self) -> List[Dict]:
        """Obtiene todas las temporadas"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM temporada ORDER BY fecha_inicio DESC")
        temporadas = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return temporadas
    
    # ==================== CLUBES ====================
    
    def insertar_club(self, nombre: str, ciudad: str = None, 
                     estadio: str = None, año_fundacion: int = None) -> int:
        """
        Inserta un nuevo club
        
        Ejemplo:
            id = db.insertar_club("Real Madrid", "Madrid", "Santiago Bernabéu", 1902)
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO club_deportivo (nombre, ciudad, estadio, año_fundacion)
            VALUES (?, ?, ?, ?)
        """, (nombre, ciudad, estadio, año_fundacion))
        
        id_club = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Club '{nombre}' creado con ID: {id_club}")
        return id_club
    
    def obtener_clubes(self) -> List[Dict]:
        """Obtiene todos los clubes"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM club_deportivo ORDER BY nombre")
        clubes = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return clubes
    
    # ==================== JUGADORES ====================
    
    def insertar_jugador(self, nombre: str, apellidos: str, fecha_nacimiento: str,
                        posicion_principal: str = None, peso_influencia: float = 1.00,
                        pie_dominante: str = None) -> int:
        """
        Inserta un nuevo jugador
        
        Ejemplo:
            id = db.insertar_jugador("Lionel", "Messi", "1987-06-24", "Delantero", 1.5, "izquierdo")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO jugador (nombre, apellidos, fecha_nacimiento, posicion_principal, 
                               peso_influencia, pie_dominante)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, apellidos, fecha_nacimiento, posicion_principal, peso_influencia, pie_dominante))
        
        id_jugador = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Jugador '{nombre} {apellidos}' creado con ID: {id_jugador}")
        return id_jugador
    
    def obtener_jugadores(self) -> List[Dict]:
        """Obtiene todos los jugadores"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM jugador ORDER BY apellidos, nombre")
        jugadores = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return jugadores
    
    # ==================== ENTRENADORES ====================
    
    def insertar_entrenador(self, nombre: str, apellidos: str, 
                           fecha_nacimiento: str, peso_influencia: float = 1.00) -> int:
        """
        Inserta un nuevo entrenador
        
        Ejemplo:
            id = db.insertar_entrenador("Pep", "Guardiola", "1971-01-18", 1.3)
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO entrenador (nombre, apellidos, fecha_nacimiento, peso_influencia)
            VALUES (?, ?, ?, ?)
        """, (nombre, apellidos, fecha_nacimiento, peso_influencia))
        
        id_entrenador = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Entrenador '{nombre} {apellidos}' creado con ID: {id_entrenador}")
        return id_entrenador
    
    # ==================== ÁRBITROS ====================
    
    def insertar_arbitro(self, nombre: str, apellidos: str, fecha_nacimiento: str,
                        rol: str = 'principal', peso_influencia: float = 1.00) -> int:
        """
        Inserta un nuevo árbitro
        
        Ejemplo:
            id = db.insertar_arbitro("Mateu", "Lahoz", "1977-03-12", "principal", 1.1)
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO arbitro (nombre, apellidos, fecha_nacimiento, peso_influencia, rol)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellidos, fecha_nacimiento, peso_influencia, rol))
        
        id_arbitro = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Árbitro '{nombre} {apellidos}' creado con ID: {id_arbitro}")
        return id_arbitro
    
    # ==================== EQUIPOS ====================
    
    def insertar_equipo(self, id_club: int, nombre_equipo: str, 
                       categoria: str = 'Primera División') -> int:
        """
        Inserta un nuevo equipo
        
        Ejemplo:
            id = db.insertar_equipo(1, "Real Madrid", "Primera División")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO equipo (id_club, nombre_equipo, categoria)
            VALUES (?, ?, ?)
        """, (id_club, nombre_equipo, categoria))
        
        id_equipo = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Equipo '{nombre_equipo}' creado con ID: {id_equipo}")
        return id_equipo
    
    def obtener_equipos(self) -> List[Dict]:
        """Obtiene todos los equipos con información del club"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT e.*, c.nombre as nombre_club, c.ciudad
            FROM equipo e
            JOIN club_deportivo c ON e.id_club = c.id_club
            ORDER BY c.nombre, e.nombre_equipo
        """)
        equipos = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return equipos
    
    # ==================== JORNADAS ====================
    
    def insertar_jornada(self, id_temporada: int, numero_jornada: int, 
                        fecha: str, estado: str = 'programada') -> int:
        """
        Inserta una nueva jornada
        
        Ejemplo:
            id = db.insertar_jornada(1, 1, "2024-08-20")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO jornada (id_temporada, numero_jornada, fecha, estado)
            VALUES (?, ?, ?, ?)
        """, (id_temporada, numero_jornada, fecha, estado))
        
        id_jornada = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Jornada {numero_jornada} creada con ID: {id_jornada}")
        return id_jornada
    
    def obtener_jornadas(self, id_temporada: int) -> List[Dict]:
        """Obtiene todas las jornadas de una temporada"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT j.*, t.nombre as nombre_temporada
            FROM jornada j
            JOIN temporada t ON j.id_temporada = t.id_temporada
            WHERE j.id_temporada = ?
            ORDER BY j.numero_jornada
        """, (id_temporada,))
        jornadas = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return jornadas
    
    # ==================== ENCUENTROS ====================
    
    def insertar_encuentro(self, id_jornada: int, id_equipo_local: int, 
                          id_equipo_visitante: int, fecha_hora: str,
                          resultado_local: int = None, resultado_visitante: int = None) -> int:
        """
        Inserta un nuevo encuentro
        
        Ejemplo:
            id = db.insertar_encuentro(1, 1, 2, "2024-08-20 20:00:00")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO encuentro (id_jornada, id_equipo_local, id_equipo_visitante, 
                                 fecha_hora, resultado_local, resultado_visitante)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_jornada, id_equipo_local, id_equipo_visitante, fecha_hora, 
              resultado_local, resultado_visitante))
        
        id_encuentro = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Encuentro creado con ID: {id_encuentro}")
        return id_encuentro
    
    def obtener_encuentros_jornada(self, id_jornada: int) -> List[Dict]:
        """Obtiene todos los encuentros de una jornada"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                e.*,
                el.nombre_equipo as equipo_local,
                ev.nombre_equipo as equipo_visitante,
                j.numero_jornada
            FROM encuentro e
            JOIN equipo el ON e.id_equipo_local = el.id_equipo
            JOIN equipo ev ON e.id_equipo_visitante = ev.id_equipo
            JOIN jornada j ON e.id_jornada = j.id_jornada
            WHERE e.id_jornada = ?
            ORDER BY e.fecha_hora
        """, (id_jornada,))
        encuentros = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return encuentros
    
    # ==================== PLANTILLA ====================
    
    def insertar_plantilla(self, id_equipo: int, id_jugador: int, id_temporada: int,
                          dorsal: int = None, activo: bool = True) -> int:
        """
        Inserta un jugador en la plantilla de un equipo
        
        Ejemplo:
            id = db.insertar_plantilla(1, 1, 1, dorsal=10)
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO plantilla (id_equipo, id_jugador, id_temporada, dorsal, activo)
            VALUES (?, ?, ?, ?, ?)
        """, (id_equipo, id_jugador, id_temporada, dorsal, 1 if activo else 0))
        
        id_plantilla = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Jugador añadido a plantilla con ID: {id_plantilla}")
        return id_plantilla
    
    def obtener_plantilla_equipo(self, id_equipo: int, id_temporada: int) -> List[Dict]:
        """Obtiene la plantilla de un equipo en una temporada"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                p.*,
                j.nombre || ' ' || j.apellidos as nombre_completo,
                j.posicion_principal,
                j.peso_influencia,
                e.nombre_equipo
            FROM plantilla p
            JOIN jugador j ON p.id_jugador = j.id_jugador
            JOIN equipo e ON p.id_equipo = e.id_equipo
            WHERE p.id_equipo = ? AND p.id_temporada = ? AND p.activo = 1
            ORDER BY p.dorsal
        """, (id_equipo, id_temporada))
        plantilla = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return plantilla
    
    # ==================== ESTADO JUGADOR (BIORRITMOS) ====================
    
    def insertar_estado_jugador(self, id_jugador: int, id_encuentro: int,
                               estado_fisico: float, estado_emocional: float,
                               estado_intelectual: float, observaciones: str = None) -> int:
        """
        Inserta el estado biorítmico de un jugador para un encuentro
        
        Ejemplo:
            id = db.insertar_estado_jugador(1, 1, 85.5, 92.3, 78.9, "Excelente forma")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO estado_jugador (id_jugador, id_encuentro, estado_fisico, 
                                       estado_emocional, estado_intelectual, observaciones)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_jugador, id_encuentro, estado_fisico, estado_emocional, 
              estado_intelectual, observaciones))
        
        id_estado = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Estado de jugador registrado con ID: {id_estado}")
        return id_estado
    
    # ==================== PREDICCIONES ====================
    
    def insertar_prediccion(self, id_encuentro: int, probabilidad_local: float,
                           probabilidad_empate: float, probabilidad_visitante: float,
                           pronostico_final: str) -> int:
        """
        Inserta una predicción para un encuentro
        
        Ejemplo:
            id = db.insertar_prediccion(1, 45.5, 25.0, 29.5, "1")
        """
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO prediccion_encuentro (id_encuentro, probabilidad_local, 
                                             probabilidad_empate, probabilidad_visitante, 
                                             pronostico_final)
            VALUES (?, ?, ?, ?, ?)
        """, (id_encuentro, probabilidad_local, probabilidad_empate, 
              probabilidad_visitante, pronostico_final))
        
        id_prediccion = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ Predicción registrada con ID: {id_prediccion}")
        return id_prediccion
    
    def obtener_predicciones_jornada(self, id_jornada: int) -> List[Dict]:
        """Obtiene las predicciones de todos los encuentros de una jornada"""
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                p.*,
                el.nombre_equipo as equipo_local,
                ev.nombre_equipo as equipo_visitante,
                e.fecha_hora
            FROM prediccion_encuentro p
            JOIN encuentro e ON p.id_encuentro = e.id_encuentro
            JOIN equipo el ON e.id_equipo_local = el.id_equipo
            JOIN equipo ev ON e.id_equipo_visitante = ev.id_equipo
            WHERE e.id_jornada = ?
            ORDER BY e.fecha_hora
        """, (id_jornada,))
        predicciones = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return predicciones
    
    # ==================== UTILIDADES ====================
    
    def mostrar_tabla(self, datos: List[Dict], titulo: str = "Resultados"):
        """Muestra los datos en formato tabla legible"""
        if not datos:
            print(f"\n📊 {titulo}: Sin registros\n")
            return
        
        print(f"\n{'='*80}")
        print(f"📊 {titulo} ({len(datos)} registros)")
        print('='*80)
        
        for i, registro in enumerate(datos, 1):
            print(f"\n▶ Registro {i}:")
            for clave, valor in registro.items():
                print(f"  {clave}: {valor}")
            print('-'*80)
        print()