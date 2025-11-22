"""
Ejemplo de uso del gestor de base de datos
Aquí puedes meter datos de prueba y hacer consultas
"""

from gestor_db import GestorDB

def ejemplo_completo():
    """Ejemplo completo: crea una temporada, clubes, equipos, jugadores y un partido"""
    
    # Crear instancia del gestor
    db = GestorDB()
    
    print("\n" + "="*80)
    print("🏆 EJEMPLO DE USO - Sistema de Predicciones Deportivas")
    print("="*80 + "\n")
    
    # ==================== 1. CREAR TEMPORADA ====================
    print("📅 1. Creando temporada...")
    id_temporada = db.insertar_temporada(
        nombre="2024-2025",
        fecha_inicio="2024-08-15",
        fecha_fin="2025-05-30",
        estado="activa"
    )
    
    # ==================== 2. CREAR CLUBES ====================
    print("\n🏟️  2. Creando clubes...")
    id_real_madrid = db.insertar_club(
        nombre="Real Madrid",
        ciudad="Madrid",
        estadio="Santiago Bernabéu",
        año_fundacion=1902
    )
    
    id_barcelona = db.insertar_club(
        nombre="FC Barcelona",
        ciudad="Barcelona",
        estadio="Camp Nou",
        año_fundacion=1899
    )
    
    id_atletico = db.insertar_club(
        nombre="Atlético Madrid",
        ciudad="Madrid",
        estadio="Cívitas Metropolitano",
        año_fundacion=1903
    )
    
    # ==================== 3. CREAR EQUIPOS ====================
    print("\n⚽ 3. Creando equipos...")
    id_equipo_rm = db.insertar_equipo(
        id_club=id_real_madrid,
        nombre_equipo="Real Madrid",
        categoria="Primera División"
    )
    
    id_equipo_fcb = db.insertar_equipo(
        id_club=id_barcelona,
        nombre_equipo="FC Barcelona",
        categoria="Primera División"
    )
    
    id_equipo_atm = db.insertar_equipo(
        id_club=id_atletico,
        nombre_equipo="Atlético Madrid",
        categoria="Primera División"
    )
    
    # ==================== 4. CREAR JUGADORES ====================
    print("\n👤 4. Creando jugadores...")
    id_vinicius = db.insertar_jugador(
        nombre="Vinicius",
        apellidos="Junior",
        fecha_nacimiento="2000-07-12",
        posicion_principal="Extremo",
        peso_influencia=1.4,
        pie_dominante="derecho"
    )
    
    id_bellingham = db.insertar_jugador(
        nombre="Jude",
        apellidos="Bellingham",
        fecha_nacimiento="2003-06-29",
        posicion_principal="Centrocampista",
        peso_influencia=1.3,
        pie_dominante="derecho"
    )
    
    id_lewandowski = db.insertar_jugador(
        nombre="Robert",
        apellidos="Lewandowski",
        fecha_nacimiento="1988-08-21",
        posicion_principal="Delantero",
        peso_influencia=1.5,
        pie_dominante="derecho"
    )
    
    id_griezmann = db.insertar_jugador(
        nombre="Antoine",
        apellidos="Griezmann",
        fecha_nacimiento="1991-03-21",
        posicion_principal="Delantero",
        peso_influencia=1.3,
        pie_dominante="izquierdo"
    )
    
    # ==================== 5. AÑADIR A PLANTILLAS ====================
    print("\n📋 5. Añadiendo jugadores a plantillas...")
    db.insertar_plantilla(id_equipo_rm, id_vinicius, id_temporada, dorsal=7)
    db.insertar_plantilla(id_equipo_rm, id_bellingham, id_temporada, dorsal=5)
    db.insertar_plantilla(id_equipo_fcb, id_lewandowski, id_temporada, dorsal=9)
    db.insertar_plantilla(id_equipo_atm, id_griezmann, id_temporada, dorsal=7)
    
    # ==================== 6. CREAR ENTRENADOR ====================
    print("\n🎓 6. Creando entrenador...")
    id_ancelotti = db.insertar_entrenador(
        nombre="Carlo",
        apellidos="Ancelotti",
        fecha_nacimiento="1959-06-10",
        peso_influencia=1.2
    )
    
    # ==================== 7. CREAR ÁRBITRO ====================
    print("\n🔵 7. Creando árbitro...")
    id_arbitro = db.insertar_arbitro(
        nombre="Mateu",
        apellidos="Lahoz",
        fecha_nacimiento="1977-03-12",
        rol="principal",
        peso_influencia=1.1
    )
    
    # ==================== 8. CREAR JORNADA ====================
    print("\n📆 8. Creando jornada...")
    id_jornada = db.insertar_jornada(
        id_temporada=id_temporada,
        numero_jornada=1,
        fecha="2024-08-20",
        estado="programada"
    )
    
    # ==================== 9. CREAR ENCUENTROS ====================
    print("\n⚔️  9. Creando encuentros...")
    id_encuentro1 = db.insertar_encuentro(
        id_jornada=id_jornada,
        id_equipo_local=id_equipo_rm,
        id_equipo_visitante=id_equipo_fcb,
        fecha_hora="2024-08-20 21:00:00"
    )
    
    id_encuentro2 = db.insertar_encuentro(
        id_jornada=id_jornada,
        id_equipo_local=id_equipo_atm,
        id_equipo_visitante=id_equipo_rm,
        fecha_hora="2024-08-21 19:00:00"
    )
    
    # ==================== 10. ESTADO JUGADOR (BIORRITMOS) ====================
    print("\n💪 10. Registrando estados de jugadores (biorritmos)...")
    db.insertar_estado_jugador(
        id_jugador=id_vinicius,
        id_encuentro=id_encuentro1,
        estado_fisico=88.5,
        estado_emocional=92.3,
        estado_intelectual=85.7,
        observaciones="Excelente estado de forma"
    )
    
    db.insertar_estado_jugador(
        id_jugador=id_lewandowski,
        id_encuentro=id_encuentro1,
        estado_fisico=82.0,
        estado_emocional=78.5,
        estado_intelectual=90.2,
        observaciones="Buen estado general"
    )
    
    # ==================== 11. PREDICCIONES ====================
    print("\n🔮 11. Creando predicciones...")
    db.insertar_prediccion(
        id_encuentro=id_encuentro1,
        probabilidad_local=48.5,
        probabilidad_empate=26.0,
        probabilidad_visitante=25.5,
        pronostico_final="1"
    )
    
    db.insertar_prediccion(
        id_encuentro=id_encuentro2,
        probabilidad_local=35.0,
        probabilidad_empate=30.0,
        probabilidad_visitante=35.0,
        pronostico_final="X"
    )
    
    # ==================== 12. CONSULTAR DATOS ====================
    print("\n" + "="*80)
    print("📊 CONSULTANDO DATOS INSERTADOS")
    print("="*80)
    
    # Mostrar temporadas
    temporadas = db.obtener_temporadas()
    db.mostrar_tabla(temporadas, "Temporadas")
    
    # Mostrar clubes
    clubes = db.obtener_clubes()
    db.mostrar_tabla(clubes, "Clubes Deportivos")
    
    # Mostrar equipos
    equipos = db.obtener_equipos()
    db.mostrar_tabla(equipos, "Equipos")
    
    # Mostrar jugadores
    jugadores = db.obtener_jugadores()
    db.mostrar_tabla(jugadores, "Jugadores")
    
    # Mostrar plantilla del Real Madrid
    plantilla_rm = db.obtener_plantilla_equipo(id_equipo_rm, id_temporada)
    db.mostrar_tabla(plantilla_rm, "Plantilla Real Madrid 2024-2025")
    
    # Mostrar encuentros de la jornada
    encuentros = db.obtener_encuentros_jornada(id_jornada)
    db.mostrar_tabla(encuentros, "Encuentros Jornada 1")
    
    # Mostrar predicciones
    predicciones = db.obtener_predicciones_jornada(id_jornada)
    db.mostrar_tabla(predicciones, "Predicciones Jornada 1")
    
    print("\n✅ ¡Ejemplo completado exitosamente!")
    print("💾 Todos los datos están guardados en: predicciones_deportivas.db\n")


def ejemplo_simple():
    """Ejemplo más simple para empezar"""
    
    db = GestorDB()
    
    print("\n🎯 Ejemplo Simple: Insertando datos básicos\n")
    
    # Crear temporada
    id_temp = db.insertar_temporada("2024-2025", "2024-08-01", "2025-05-31")
    
    # Crear club
    id_club = db.insertar_club("Real Madrid", "Madrid")
    
    # Crear equipo
    id_equipo = db.insertar_equipo(id_club, "Real Madrid")
    
    # Crear jugador
    id_jugador = db.insertar_jugador("Lionel", "Messi", "1987-06-24", "Delantero")
    
    # Añadir a plantilla
    db.insertar_plantilla(id_equipo, id_jugador, id_temp, dorsal=10)
    
    print("\n✅ Datos insertados correctamente!")
    
    # Consultar
    print("\n📋 Jugadores en la base de datos:")
    jugadores = db.obtener_jugadores()
    db.mostrar_tabla(jugadores, "Jugadores")


if __name__ == "__main__":
    # Descomentar la función que quieras ejecutar:
    
    ejemplo_completo()  # Ejemplo completo con muchos datos
    # ejemplo_simple()    # Ejemplo simple con pocos datos