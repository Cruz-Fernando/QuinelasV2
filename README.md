# ⚽ Sistema de Predicciones Deportivas (QuinelasV2)

Bienvenido al **Sistema de Predicciones Deportivas**, una aplicación completa para gestionar datos de fútbol y realizar predicciones. Este proyecto cuenta con una interfaz gráfica moderna y herramientas de línea de comandos para una gestión eficiente.

## 🚀 Características Principales

### 🖥️ Interfaz Gráfica (`interfaz_visual.py`)
La joya del proyecto. Una interfaz visual construida con `tkinter` que ofrece:
- **Diseño Moderno**: Tema claro/oscuro con una paleta de colores profesional.
- **Pestañas Funcionales**:
    - **➕ Insertar Datos**: Formularios intuitivos para registrar Temporadas, Clubes, Equipos, Jugadores, Entrenadores, Árbitros, Jornadas, Encuentros, Plantillas, Estados de Jugadores y Predicciones.
    - **📊 Consultar Datos**: Botones de acceso rápido para visualizar la información almacenada en la base de datos.
- **Búsqueda Integrada**: Herramienta para buscar jugadores por ID directamente desde la interfaz.

### 🔍 Herramienta de Búsqueda CLI (`buscar_jugador.py`)
Un script de línea de comandos ligero y rápido para:
- Buscar detalles de un jugador específico por su ID.
- Listar los primeros 20 jugadores registrados para una referencia rápida.

### 💾 Gestión de Datos (`gestor_db.py`)
El motor del sistema. Maneja todas las interacciones con la base de datos SQLite `predicciones_deportivas.db`, asegurando la integridad y persistencia de los datos.

---

## 📂 Estructura del Proyecto

### ✅ Archivos Esenciales
- **`interfaz_visual.py`**: El punto de entrada principal. Ejecuta esto para usar la aplicación completa.
- **`buscar_jugador.py`**: Utilidad rápida para consultas de jugadores.
- **`gestor_db.py`**: Lógica de base de datos (Backend).
- **`predicciones_deportivas.db`**: Archivo de base de datos SQLite (se crea automáticamente o se usa el existente).

### 🔧 Utilidades
- **`crear_base_datos.py`**: Script de inicialización para crear las tablas necesarias.
- **`llenar_datos_completos.py`**: Script para poblar la base de datos con datos de prueba/iniciales.

---

## �️ Instalación y Uso

### Prerrequisitos
Asegúrate de tener Python instalado. Este proyecto utiliza librerías estándar, por lo que no deberías necesitar instalar paquetes externos complejos, pero asegúrate de tener `tkinter` y `sqlite3` disponibles (usualmente vienen con Python).

### 1. Ejecutar la Interfaz Gráfica
Para acceder a todas las funcionalidades:
```bash
python interfaz_visual.py
```

### 2. Usar el Buscador de Jugadores
Para una búsqueda rápida desde la terminal:
```bash
python buscar_jugador.py
```
Sigue las instrucciones en pantalla para buscar por ID o ver la lista.

### 3. Ver/Editar la Base de Datos Manualmente
Si necesitas inspeccionar los datos crudos:
1. Descarga [DB Browser for SQLite](https://sqlitebrowser.org/dl/).
2. Abre el archivo `predicciones_deportivas.db`.

---

## 📊 Estado del Proyecto
El sistema es completamente funcional y permite:
- ✅ Gestión completa de entidades deportivas (Clubes, Jugadores, etc.).
- ✅ Registro de encuentros y resultados.
- ✅ Creación de predicciones basadas en probabilidades.
- ✅ Seguimiento del estado físico/emocional de los jugadores (Biorritmos).

---
*Desarrollado para el Proyecto de Bases de Datos - QuinelasV2*
