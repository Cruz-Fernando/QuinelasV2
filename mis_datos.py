"""
Archivo para meter TUS propios datos
Edita las secciones según tus necesidades
"""

from gestor_db import GestorDB

# ==================== CONFIGURACIÓN ====================
db = GestorDB()

def menu_principal():
    """Menú interactivo para gestionar la base de datos"""
    
    while True:
        print("\n" + "="*60)
        print("🏆 SISTEMA DE PREDICCIONES DEPORTIVAS")
        print("="*60)
        print("\n📋 MENÚ PRINCIPAL:")
        print("  1️⃣  - Insertar Temporada")
        print("  2️⃣  - Insertar Club")
        print("  3️⃣  - Insertar Equipo")
        print("  4️⃣  - Insertar Jugador")
        print("  5️⃣  - Insertar Entrenador")
        print("  6️⃣  - Insertar Árbitro")
        print("  7️⃣  - Insertar Jornada")
        print("  8️⃣  - Insertar Encuentro")
        print("  9️⃣  - Añadir Jugador a Plantilla")
        print("  🔟 - Insertar Estado Jugador (Biorritmos)")
        print("  1️⃣1️⃣ - Insertar Predicción")
        print("\n📊 CONSULTAS:")
        print("  12 - Ver todas las Temporadas")
        print("  13 - Ver todos los Clubes")
        print("  14 - Ver todos los Equipos")
        print("  15 - Ver todos los Jugadores")
        print("  16 - Ver Plantilla de un Equipo")
        print("  17 - Ver Encuentros de una Jornada")
        print("  18 - Ver Predicciones de una Jornada")
        print("\n  0️⃣  - Salir")
        print("="*60)
        
        opcion = input("\n👉 Elige una opción: ").strip()
        
        if opcion == "0":
            print("\n👋 ¡Hasta luego!\n")
            break
        elif opcion == "1":
            insertar_temporada()
        elif opcion == "2":
            insertar_club()
        elif opcion == "3":
            insertar_equipo()
        elif opcion == "4":
            insertar_jugador()
        elif opcion == "5":
            insertar_entrenador()
        elif opcion == "6":
            insertar_arbitro()
        elif opcion == "7":
            insertar_jornada()
        elif opcion == "8":
            insertar_encuentro()
        elif opcion == "9":
            insertar_plantilla()
        elif opcion == "10":
            insertar_estado_jugador()
        elif opcion == "11":
            insertar_prediccion()
        elif opcion == "12":
            ver_temporadas()
        elif opcion == "13":
            ver_clubes()
        elif opcion == "14":
            ver_equipos()
        elif opcion == "15":
            ver_jugadores()
        elif opcion == "16":
            ver_plantilla()
        elif opcion == "17":
            ver_encuentros()
        elif opcion == "18":
            ver_predicciones()
        else:
            print("\n❌ Opción no válida")

# ==================== FUNCIONES DE INSERCIÓN ====================

def insertar_temporada():
    """Insertar una nueva temporada"""
    print("\n📅 INSERTAR TEMPORADA")
    print("-" * 60)
    nombre = input("Nombre (ej: 2024-2025): ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    estado = input("Estado (activa/finalizada/suspendida) [activa]: ") or "activa"
    
    db.insertar_temporada(nombre, fecha_inicio, fecha_fin, estado)
    input("\n✅ Presiona Enter para continuar...")

def insertar_club():
    """Insertar un nuevo club"""
    print("\n🏟️  INSERTAR CLUB")
    print("-" * 60)
    nombre = input("Nombre del club: ")
    ciudad = input("Ciudad (opcional): ") or None
    estadio = input("Estadio (opcional): ") or None
    año = input("Año fundación (opcional): ")
    año_fundacion = int(año) if año else None
    
    db.insertar_club(nombre, ciudad, estadio, año_fundacion)
    input("\n✅ Presiona Enter para continuar...")

def insertar_equipo():
    """Insertar un nuevo equipo"""
    print("\n⚽ INSERTAR EQUIPO")
    print("-" * 60)
    
    # Mostrar clubes disponibles
    clubes = db.obtener_clubes()
    print("\n📋 Clubes disponibles:")
    for club in clubes:
        print(f"  ID {club['id_club']}: {club['nombre']}")
    
    id_club = int(input("\nID del club: "))
    nombre_equipo = input("Nombre del equipo: ")
    categoria = input("Categoría [Primera División]: ") or "Primera División"
    
    db.insertar_equipo(id_club, nombre_equipo, categoria)
    input("\n✅ Presiona Enter para continuar...")

def insertar_jugador():
    """Insertar un nuevo jugador"""
    print("\n👤 INSERTAR JUGADOR")
    print("-" * 60)
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha nacimiento (YYYY-MM-DD): ")
    posicion = input("Posición (opcional): ") or None
    peso = input("Peso influencia [1.00]: ")
    peso_influencia = float(peso) if peso else 1.00
    pie = input("Pie dominante (derecho/izquierdo/ambos) (opcional): ") or None
    
    db.insertar_jugador(nombre, apellidos, fecha_nacimiento, posicion, 
                       peso_influencia, pie)
    input("\n✅ Presiona Enter para continuar...")

def insertar_entrenador():
    """Insertar un nuevo entrenador"""
    print("\n🎓 INSERTAR ENTRENADOR")
    print("-" * 60)
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha nacimiento (YYYY-MM-DD): ")
    peso = input("Peso influencia [1.00]: ")
    peso_influencia = float(peso) if peso else 1.00
    
    db.insertar_entrenador(nombre, apellidos, fecha_nacimiento, peso_influencia)
    input("\n✅ Presiona Enter para continuar...")

def insertar_arbitro():
    """Insertar un nuevo árbitro"""
    print("\n🔵 INSERTAR ÁRBITRO")
    print("-" * 60)
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha nacimiento (YYYY-MM-DD): ")
    rol = input("Rol (principal/asistente/auxiliar) [principal]: ") or "principal"
    peso = input("Peso influencia [1.00]: ")
    peso_influencia = float(peso) if peso else 1.00
    
    db.insertar_arbitro(nombre, apellidos, fecha_nacimiento, rol, peso_influencia)
    input("\n✅ Presiona Enter para continuar...")

def insertar_jornada():
    """Insertar una nueva jornada"""
    print("\n📆 INSERTAR JORNADA")
    print("-" * 60)
    
    # Mostrar temporadas disponibles
    temporadas = db.obtener_temporadas()
    print("\n📋 Temporadas disponibles:")
    for temp in temporadas:
        print(f"  ID {temp['id_temporada']}: {temp['nombre']}")
    
    id_temporada = int(input("\nID de la temporada: "))
    numero_jornada = int(input("Número de jornada: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    estado = input("Estado [programada]: ") or "programada"
    
    db.insertar_jornada(id_temporada, numero_jornada, fecha, estado)
    input("\n✅ Presiona Enter para continuar...")

def insertar_encuentro():
    """Insertar un nuevo encuentro"""
    print("\n⚔️  INSERTAR ENCUENTRO")
    print("-" * 60)
    
    # Mostrar jornadas disponibles
    temporadas = db.obtener_temporadas()
    if temporadas:
        id_temp = int(input("ID de temporada para ver jornadas: "))
        jornadas = db.obtener_jornadas(id_temp)
        print("\n📋 Jornadas disponibles:")
        for jor in jornadas:
            print(f"  ID {jor['id_jornada']}: Jornada {jor['numero_jornada']} - {jor['fecha']}")
    
    id_jornada = int(input("\nID de la jornada: "))
    
    # Mostrar equipos disponibles
    equipos = db.obtener_equipos()
    print("\n📋 Equipos disponibles:")
    for eq in equipos:
        print(f"  ID {eq['id_equipo']}: {eq['nombre_equipo']}")
    
    id_equipo_local = int(input("\nID equipo LOCAL: "))
    id_equipo_visitante = int(input("ID equipo VISITANTE: "))
    fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM:SS): ")
    
    res_local = input("Resultado local (dejar vacío si no ha jugado): ")
    res_visitante = input("Resultado visitante (dejar vacío si no ha jugado): ")
    
    resultado_local = int(res_local) if res_local else None
    resultado_visitante = int(res_visitante) if res_visitante else None
    
    db.insertar_encuentro(id_jornada, id_equipo_local, id_equipo_visitante, 
                         fecha_hora, resultado_local, resultado_visitante)
    input("\n✅ Presiona Enter para continuar...")

def insertar_plantilla():
    """Añadir jugador a plantilla"""
    print("\n📋 AÑADIR JUGADOR A PLANTILLA")
    print("-" * 60)
    
    # Mostrar equipos
    equipos = db.obtener_equipos()
    print("\n📋 Equipos disponibles:")
    for eq in equipos:
        print(f"  ID {eq['id_equipo']}: {eq['nombre_equipo']}")
    
    id_equipo = int(input("\nID del equipo: "))
    
    # Mostrar jugadores
    jugadores = db.obtener_jugadores()
    print("\n📋 Jugadores disponibles:")
    for jug in jugadores:
        print(f"  ID {jug['id_jugador']}: {jug['nombre']} {jug['apellidos']}")
    
    id_jugador = int(input("\nID del jugador: "))
    
    # Mostrar temporadas
    temporadas = db.obtener_temporadas()
    print("\n📋 Temporadas disponibles:")
    for temp in temporadas:
        print(f"  ID {temp['id_temporada']}: {temp['nombre']}")
    
    id_temporada = int(input("\nID de la temporada: "))
    dorsal = input("Dorsal (opcional): ")
    dorsal_num = int(dorsal) if dorsal else None
    
    db.insertar_plantilla(id_equipo, id_jugador, id_temporada, dorsal_num)
    input("\n✅ Presiona Enter para continuar...")

def insertar_estado_jugador():
    """Insertar estado de jugador (biorritmos)"""
    print("\n💪 INSERTAR ESTADO JUGADOR (BIORRITMOS)")
    print("-" * 60)
    
    # Mostrar jugadores
    jugadores = db.obtener_jugadores()
    print("\n📋 Jugadores disponibles:")
    for jug in jugadores:
        print(f"  ID {jug['id_jugador']}: {jug['nombre']} {jug['apellidos']}")
    
    id_jugador = int(input("\nID del jugador: "))
    id_encuentro = int(input("ID del encuentro: "))
    
    estado_fisico = float(input("Estado físico (0-100): "))
    estado_emocional = float(input("Estado emocional (0-100): "))
    estado_intelectual = float(input("Estado intelectual (0-100): "))
    observaciones = input("Observaciones (opcional): ") or None
    
    db.insertar_estado_jugador(id_jugador, id_encuentro, estado_fisico,
                              estado_emocional, estado_intelectual, observaciones)
    input("\n✅ Presiona Enter para continuar...")

def insertar_prediccion():
    """Insertar predicción para un encuentro"""
    print("\n🔮 INSERTAR PREDICCIÓN")
    print("-" * 60)
    
    id_encuentro = int(input("ID del encuentro: "))
    prob_local = float(input("Probabilidad local (%): "))
    prob_empate = float(input("Probabilidad empate (%): "))
    prob_visitante = float(input("Probabilidad visitante (%): "))
    pronostico = input("Pronóstico final (1/X/2): ")
    
    db.insertar_prediccion(id_encuentro, prob_local, prob_empate, 
                          prob_visitante, pronostico)
    input("\n✅ Presiona Enter para continuar...")

# ==================== FUNCIONES DE CONSULTA ====================

def ver_temporadas():
    """Ver todas las temporadas"""
    temporadas = db.obtener_temporadas()
    db.mostrar_tabla(temporadas, "Temporadas")
    input("\n📊 Presiona Enter para continuar...")

def ver_clubes():
    """Ver todos los clubes"""
    clubes = db.obtener_clubes()
    db.mostrar_tabla(clubes, "Clubes Deportivos")
    input("\n📊 Presiona Enter para continuar...")

def ver_equipos():
    """Ver todos los equipos"""
    equipos = db.obtener_equipos()
    db.mostrar_tabla(equipos, "Equipos")
    input("\n📊 Presiona Enter para continuar...")

def ver_jugadores():
    """Ver todos los jugadores"""
    jugadores = db.obtener_jugadores()
    db.mostrar_tabla(jugadores, "Jugadores")
    input("\n📊 Presiona Enter para continuar...")

def ver_plantilla():
    """Ver plantilla de un equipo"""
    equipos = db.obtener_equipos()
    print("\n📋 Equipos disponibles:")
    for eq in equipos:
        print(f"  ID {eq['id_equipo']}: {eq['nombre_equipo']}")
    
    id_equipo = int(input("\nID del equipo: "))
    
    temporadas = db.obtener_temporadas()
    print("\n📋 Temporadas disponibles:")
    for temp in temporadas:
        print(f"  ID {temp['id_temporada']}: {temp['nombre']}")
    
    id_temporada = int(input("\nID de la temporada: "))
    
    plantilla = db.obtener_plantilla_equipo(id_equipo, id_temporada)
    db.mostrar_tabla(plantilla, "Plantilla del Equipo")
    input("\n📊 Presiona Enter para continuar...")

def ver_encuentros():
    """Ver encuentros de una jornada"""
    temporadas = db.obtener_temporadas()
    if temporadas:
        id_temp = int(input("ID de temporada: "))
        jornadas = db.obtener_jornadas(id_temp)
        print("\n📋 Jornadas disponibles:")
        for jor in jornadas:
            print(f"  ID {jor['id_jornada']}: Jornada {jor['numero_jornada']}")
    
    id_jornada = int(input("\nID de la jornada: "))
    encuentros = db.obtener_encuentros_jornada(id_jornada)
    db.mostrar_tabla(encuentros, "Encuentros de la Jornada")
    input("\n📊 Presiona Enter para continuar...")

def ver_predicciones():
    """Ver predicciones de una jornada"""
    id_jornada = int(input("ID de la jornada: "))
    predicciones = db.obtener_predicciones_jornada(id_jornada)
    db.mostrar_tabla(predicciones, "Predicciones de la Jornada")
    input("\n📊 Presiona Enter para continuar...")

# ==================== EJECUTAR ====================

if __name__ == "__main__":
    menu_principal()