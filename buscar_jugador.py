"""
Buscador de Jugadores por ID
Script independiente para buscar jugadores sin modificar interfaz_visual.py
"""

from gestor_db import GestorDB

def buscar_jugador():
    db = GestorDB()
    
    print("=" * 70)
    print("🔍 BUSCADOR DE JUGADORES POR ID")
    print("=" * 70)
    
    while True:
        print("\nOpciones:")
        print("  1. Buscar jugador por ID")
        print("  2. Ver todos los jugadores (primeros 20)")
        print("  3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == "3":
            print("\n¡Hasta luego! 👋")
            break
        elif opcion == "2":
            jugadores = db.obtener_jugadores()
            jugadores_ordenados = sorted(jugadores, key=lambda x: x['id_jugador'])[:20]
            
            print("\n📋 PRIMEROS 20 JUGADORES:")
            print("-" * 70)
            for j in jugadores_ordenados:
                print(f"ID {j['id_jugador']:3d}: {j['nombre']} {j['apellidos']} - {j['posicion_principal'] or 'N/A'}")
            print(f"\n... Total: {len(jugadores)} jugadores en la base de datos")
            
        elif opcion == "1":
            try:
                id_buscar = input("\nIngresa el ID del jugador: ").strip()
                
                if not id_buscar:
                    print("❌ Por favor ingresa un ID")
                    continue
                
                id_buscar = int(id_buscar)
                
                jugadores = db.obtener_jugadores()
                jugador = next((j for j in jugadores if j['id_jugador'] == id_buscar), None)
                
                if not jugador:
                    print(f"\n❌ No se encontró ningún jugador con ID: {id_buscar}")
                    print("   Verifica que el ID sea correcto e intenta nuevamente.")
                else:
                    print("\n" + "=" * 70)
                    print("✅ JUGADOR ENCONTRADO")
                    print("=" * 70)
                    print(f"\n🆔 ID: {jugador['id_jugador']}")
                    print(f"👤 Nombre Completo: {jugador['nombre']} {jugador['apellidos']}")
                    print(f"📅 Fecha Nacimiento: {jugador['fecha_nacimiento']}")
                    print(f"⚽ Posición: {jugador['posicion_principal'] or 'N/A'}")
                    print(f"🦶 Pie Dominante: {jugador['pie_dominante'] or 'N/A'}")
                    print(f"⭐ Peso Influencia: {jugador['peso_influencia']}")
                    print("=" * 70)
                    
            except ValueError:
                print("❌ Error: El ID debe ser un número entero")
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    buscar_jugador()
