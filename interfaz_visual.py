"""
Interfaz Gráfica con Tkinter para el Sistema de Predicciones Deportivas
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from gestor_db import GestorDB

class InterfazPredicciones:
    def __init__(self, root):
        self.root = root
        self.root.title("⚽ Sistema de Predicciones Deportivas")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        self.db = GestorDB()
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear las pestañas
        self.crear_tab_insertar()
        self.crear_tab_consultar()
        
        # Estilo
        self.configurar_estilo()
    
    def configurar_estilo(self):
        """Configura el estilo de los widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TFrame', background='#ffffff')
        style.configure('TLabel', background='#ffffff', font=('Arial', 10))
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'), foreground='#2c3e50')
        style.configure('TButton', font=('Arial', 10, 'bold'))
    
    # ==================== TAB INSERTAR ====================
    
    def crear_tab_insertar(self):
        """Crea la pestaña de inserción de datos"""
        tab_insertar = ttk.Frame(self.notebook)
        self.notebook.add(tab_insertar, text="➕ Insertar Datos")
        
        # Frame principal con scroll
        canvas = tk.Canvas(tab_insertar, bg='#ffffff')
        scrollbar = ttk.Scrollbar(tab_insertar, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Botones para cada tipo de inserción
        opciones = [
            ("📅 Temporada", self.ventana_temporada),
            ("🏟️ Club", self.ventana_club),
            ("⚽ Equipo", self.ventana_equipo),
            ("👤 Jugador", self.ventana_jugador),
            ("🎓 Entrenador", self.ventana_entrenador),
            ("🔵 Árbitro", self.ventana_arbitro),
            ("📆 Jornada", self.ventana_jornada),
            ("⚔️ Encuentro", self.ventana_encuentro),
            ("📋 Plantilla", self.ventana_plantilla),
            ("💪 Estado Jugador", self.ventana_estado_jugador),
            ("🔮 Predicción", self.ventana_prediccion),
        ]
        
        ttk.Label(scrollable_frame, text="Selecciona qué deseas insertar:", 
                 style='Title.TLabel').pack(pady=20)
        
        for texto, comando in opciones:
            btn = tk.Button(scrollable_frame, text=texto, command=comando,
                          font=('Arial', 12, 'bold'), bg='#3498db', fg='white',
                          width=30, height=2, cursor='hand2', relief='raised')
            btn.pack(pady=5, padx=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    # ==================== TAB CONSULTAR ====================
    
    def crear_tab_consultar(self):
        """Crea la pestaña de consultas"""
        tab_consultar = ttk.Frame(self.notebook)
        self.notebook.add(tab_consultar, text="📊 Consultar Datos")
        
        # Frame para botones
        frame_botones = ttk.Frame(tab_consultar)
        frame_botones.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame_botones, text="Selecciona qué consultar:", 
                 style='Title.TLabel').pack(pady=10)
        
        consultas = [
            ("📅 Ver Temporadas", self.ver_temporadas),
            ("🏟️ Ver Clubes", self.ver_clubes),
            ("⚽ Ver Equipos", self.ver_equipos),
            ("👤 Ver Jugadores", self.ver_jugadores),
            ("📋 Ver Plantilla", self.ver_plantilla),
            ("⚔️ Ver Encuentros", self.ver_encuentros),
            ("🔮 Ver Predicciones", self.ver_predicciones),
        ]
        
        for texto, comando in consultas:
            btn = tk.Button(frame_botones, text=texto, command=comando,
                          font=('Arial', 11), bg='#2ecc71', fg='white',
                          width=25, height=1, cursor='hand2')
            btn.pack(pady=3)
        
        # Área de resultados
        ttk.Label(tab_consultar, text="Resultados:", style='Title.TLabel').pack(pady=5)
        
        self.texto_resultados = scrolledtext.ScrolledText(tab_consultar, 
                                                          wrap=tk.WORD, 
                                                          width=100, 
                                                          height=25,
                                                          font=('Courier', 10))
        self.texto_resultados.pack(padx=10, pady=5, fill='both', expand=True)
    
    # ==================== VENTANAS DE INSERCIÓN ====================
    
    def ventana_temporada(self):
        """Ventana para insertar temporada"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Temporada")
        ventana.geometry("400x300")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nueva Temporada", style='Title.TLabel').pack(pady=10)
        
        # Campos
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="Nombre (ej: 2024-2025):").grid(row=0, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha Inicio (YYYY-MM-DD):").grid(row=1, column=0, sticky='w', pady=5)
        entry_inicio = ttk.Entry(frame, width=30)
        entry_inicio.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha Fin (YYYY-MM-DD):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fin = ttk.Entry(frame, width=30)
        entry_fin.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Estado:").grid(row=3, column=0, sticky='w', pady=5)
        combo_estado = ttk.Combobox(frame, values=['activa', 'finalizada', 'suspendida'], width=28)
        combo_estado.set('activa')
        combo_estado.grid(row=3, column=1, pady=5)
        
        def guardar():
            try:
                self.db.insertar_temporada(
                    entry_nombre.get(),
                    entry_inicio.get(),
                    entry_fin.get(),
                    combo_estado.get()
                )
                messagebox.showinfo("Éxito", "Temporada insertada correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar, 
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_club(self):
        """Ventana para insertar club"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Club")
        ventana.geometry("400x350")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Club", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Ciudad:").grid(row=1, column=0, sticky='w', pady=5)
        entry_ciudad = ttk.Entry(frame, width=30)
        entry_ciudad.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Estadio:").grid(row=2, column=0, sticky='w', pady=5)
        entry_estadio = ttk.Entry(frame, width=30)
        entry_estadio.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Año Fundación:").grid(row=3, column=0, sticky='w', pady=5)
        entry_año = ttk.Entry(frame, width=30)
        entry_año.grid(row=3, column=1, pady=5)
        
        def guardar():
            try:
                año = int(entry_año.get()) if entry_año.get() else None
                self.db.insertar_club(
                    entry_nombre.get(),
                    entry_ciudad.get() or None,
                    entry_estadio.get() or None,
                    año
                )
                messagebox.showinfo("Éxito", "Club insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_plantilla(self):
        """Ventana para añadir jugador a plantilla"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Añadir Jugador a Plantilla")
        ventana.geometry("500x400")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Añadir Jugador a Plantilla", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        # Obtener equipos
        equipos = self.db.obtener_equipos()
        if not equipos:
            messagebox.showwarning("Advertencia", "Primero debes crear equipos")
            ventana.destroy()
            return
        
        eq_dict = {f"{e['id_equipo']} - {e['nombre_equipo']}": e['id_equipo'] for e in equipos}
        
        ttk.Label(frame, text="Equipo:").grid(row=0, column=0, sticky='w', pady=5)
        combo_equipo = ttk.Combobox(frame, values=list(eq_dict.keys()), width=40)
        combo_equipo.grid(row=0, column=1, pady=5)
        
        # Obtener jugadores
        jugadores = self.db.obtener_jugadores()
        if not jugadores:
            messagebox.showwarning("Advertencia", "Primero debes crear jugadores")
            ventana.destroy()
            return
        
        jug_dict = {f"{j['id_jugador']} - {j['nombre']} {j['apellidos']}": j['id_jugador'] for j in jugadores}
        
        ttk.Label(frame, text="Jugador:").grid(row=1, column=0, sticky='w', pady=5)
        combo_jugador = ttk.Combobox(frame, values=list(jug_dict.keys()), width=40)
        combo_jugador.grid(row=1, column=1, pady=5)
        
        # Obtener temporadas
        temporadas = self.db.obtener_temporadas()
        if not temporadas:
            messagebox.showwarning("Advertencia", "Primero debes crear una temporada")
            ventana.destroy()
            return
        
        temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
        
        ttk.Label(frame, text="Temporada:").grid(row=2, column=0, sticky='w', pady=5)
        combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=40)
        combo_temp.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Dorsal:").grid(row=3, column=0, sticky='w', pady=5)
        entry_dorsal = ttk.Entry(frame, width=42)
        entry_dorsal.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Activo:").grid(row=4, column=0, sticky='w', pady=5)
        combo_activo = ttk.Combobox(frame, values=['Sí', 'No'], width=40)
        combo_activo.set('Sí')
        combo_activo.grid(row=4, column=1, pady=5)
        
        def guardar():
            try:
                id_equipo = eq_dict[combo_equipo.get()]
                id_jugador = jug_dict[combo_jugador.get()]
                id_temp = temp_dict[combo_temp.get()]
                dorsal = int(entry_dorsal.get()) if entry_dorsal.get() else None
                activo = True if combo_activo.get() == 'Sí' else False
                
                self.db.insertar_plantilla(id_equipo, id_jugador, id_temp, dorsal, activo)
                messagebox.showinfo("Éxito", "Jugador añadido a plantilla correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_estado_jugador(self):
        """Ventana para insertar estado jugador (biorritmos)"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Estado Jugador (Biorritmos)")
        ventana.geometry("500x500")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Estado Jugador - Biorritmos", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        # Obtener jugadores
        jugadores = self.db.obtener_jugadores()
        if not jugadores:
            messagebox.showwarning("Advertencia", "Primero debes crear jugadores")
            ventana.destroy()
            return
        
        jug_dict = {f"{j['id_jugador']} - {j['nombre']} {j['apellidos']}": j['id_jugador'] for j in jugadores}
        
        ttk.Label(frame, text="Jugador:").grid(row=0, column=0, sticky='w', pady=5)
        combo_jugador = ttk.Combobox(frame, values=list(jug_dict.keys()), width=40)
        combo_jugador.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="ID Encuentro:").grid(row=1, column=0, sticky='w', pady=5)
        entry_encuentro = ttk.Entry(frame, width=42)
        entry_encuentro.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Estado Físico (0-100):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fisico = ttk.Entry(frame, width=42)
        entry_fisico.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Estado Emocional (0-100):").grid(row=3, column=0, sticky='w', pady=5)
        entry_emocional = ttk.Entry(frame, width=42)
        entry_emocional.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Estado Intelectual (0-100):").grid(row=4, column=0, sticky='w', pady=5)
        entry_intelectual = ttk.Entry(frame, width=42)
        entry_intelectual.grid(row=4, column=1, pady=5)
        
        ttk.Label(frame, text="Observaciones:").grid(row=5, column=0, sticky='w', pady=5)
        text_obs = tk.Text(frame, width=32, height=4)
        text_obs.grid(row=5, column=1, pady=5)
        
        def guardar():
            try:
                id_jugador = jug_dict[combo_jugador.get()]
                id_encuentro = int(entry_encuentro.get())
                estado_fisico = float(entry_fisico.get())
                estado_emocional = float(entry_emocional.get())
                estado_intelectual = float(entry_intelectual.get())
                observaciones = text_obs.get("1.0", tk.END).strip() or None
                
                self.db.insertar_estado_jugador(
                    id_jugador, id_encuentro, estado_fisico,
                    estado_emocional, estado_intelectual, observaciones
                )
                messagebox.showinfo("Éxito", "Estado del jugador registrado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_prediccion(self):
        """Ventana para insertar predicción"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Predicción")
        ventana.geometry("500x450")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nueva Predicción", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="ID Encuentro:").grid(row=0, column=0, sticky='w', pady=5)
        entry_encuentro = ttk.Entry(frame, width=42)
        entry_encuentro.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Probabilidad Local (%):").grid(row=1, column=0, sticky='w', pady=5)
        entry_prob_local = ttk.Entry(frame, width=42)
        entry_prob_local.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Probabilidad Empate (%):").grid(row=2, column=0, sticky='w', pady=5)
        entry_prob_empate = ttk.Entry(frame, width=42)
        entry_prob_empate.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Probabilidad Visitante (%):").grid(row=3, column=0, sticky='w', pady=5)
        entry_prob_visitante = ttk.Entry(frame, width=42)
        entry_prob_visitante.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Pronóstico Final:").grid(row=4, column=0, sticky='w', pady=5)
        combo_pronostico = ttk.Combobox(frame, values=['1', 'X', '2'], width=40)
        combo_pronostico.grid(row=4, column=1, pady=5)
        
        def guardar():
            try:
                id_encuentro = int(entry_encuentro.get())
                prob_local = float(entry_prob_local.get())
                prob_empate = float(entry_prob_empate.get())
                prob_visitante = float(entry_prob_visitante.get())
                pronostico = combo_pronostico.get()
                
                self.db.insertar_prediccion(
                    id_encuentro, prob_local, prob_empate,
                    prob_visitante, pronostico
                )
                messagebox.showinfo("Éxito", "Predicción insertada correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_equipo(self):
        """Ventana para insertar equipo"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Equipo")
        ventana.geometry("450x300")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Equipo", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        # Obtener clubes
        clubes = self.db.obtener_clubes()
        if not clubes:
            messagebox.showwarning("Advertencia", "Primero debes crear un club")
            ventana.destroy()
            return
        
        clubes_dict = {f"{c['id_club']} - {c['nombre']}": c['id_club'] for c in clubes}
        
        ttk.Label(frame, text="Club:").grid(row=0, column=0, sticky='w', pady=5)
        combo_club = ttk.Combobox(frame, values=list(clubes_dict.keys()), width=35)
        combo_club.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Nombre Equipo:").grid(row=1, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=37)
        entry_nombre.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Categoría:").grid(row=2, column=0, sticky='w', pady=5)
        entry_categoria = ttk.Entry(frame, width=37)
        entry_categoria.insert(0, "Primera División")
        entry_categoria.grid(row=2, column=1, pady=5)
        
        def guardar():
            try:
                id_club = clubes_dict[combo_club.get()]
                self.db.insertar_equipo(
                    id_club,
                    entry_nombre.get(),
                    entry_categoria.get()
                )
                messagebox.showinfo("Éxito", "Equipo insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_jugador(self):
        """Ventana para insertar jugador"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Jugador")
        ventana.geometry("450x450")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Jugador", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Apellidos:").grid(row=1, column=0, sticky='w', pady=5)
        entry_apellidos = ttk.Entry(frame, width=30)
        entry_apellidos.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha Nac. (YYYY-MM-DD):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fecha = ttk.Entry(frame, width=30)
        entry_fecha.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Posición:").grid(row=3, column=0, sticky='w', pady=5)
        entry_posicion = ttk.Entry(frame, width=30)
        entry_posicion.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Peso Influencia:").grid(row=4, column=0, sticky='w', pady=5)
        entry_peso = ttk.Entry(frame, width=30)
        entry_peso.insert(0, "1.00")
        entry_peso.grid(row=4, column=1, pady=5)
        
        ttk.Label(frame, text="Pie Dominante:").grid(row=5, column=0, sticky='w', pady=5)
        combo_pie = ttk.Combobox(frame, values=['derecho', 'izquierdo', 'ambos'], width=28)
        combo_pie.grid(row=5, column=1, pady=5)
        
        def guardar():
            try:
                self.db.insertar_jugador(
                    entry_nombre.get(),
                    entry_apellidos.get(),
                    entry_fecha.get(),
                    entry_posicion.get() or None,
                    float(entry_peso.get()),
                    combo_pie.get() or None
                )
                messagebox.showinfo("Éxito", "Jugador insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_entrenador(self):
        """Ventana para insertar entrenador"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Entrenador")
        ventana.geometry("450x350")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Entrenador", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Apellidos:").grid(row=1, column=0, sticky='w', pady=5)
        entry_apellidos = ttk.Entry(frame, width=30)
        entry_apellidos.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha Nac. (YYYY-MM-DD):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fecha = ttk.Entry(frame, width=30)
        entry_fecha.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Peso Influencia:").grid(row=3, column=0, sticky='w', pady=5)
        entry_peso = ttk.Entry(frame, width=30)
        entry_peso.insert(0, "1.00")
        entry_peso.grid(row=3, column=1, pady=5)
        
        def guardar():
            try:
                self.db.insertar_entrenador(
                    entry_nombre.get(),
                    entry_apellidos.get(),
                    entry_fecha.get(),
                    float(entry_peso.get())
                )
                messagebox.showinfo("Éxito", "Entrenador insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_arbitro(self):
        """Ventana para insertar árbitro"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Árbitro")
        ventana.geometry("450x380")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Árbitro", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w', pady=5)
        entry_nombre = ttk.Entry(frame, width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Apellidos:").grid(row=1, column=0, sticky='w', pady=5)
        entry_apellidos = ttk.Entry(frame, width=30)
        entry_apellidos.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha Nac. (YYYY-MM-DD):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fecha = ttk.Entry(frame, width=30)
        entry_fecha.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Rol:").grid(row=3, column=0, sticky='w', pady=5)
        combo_rol = ttk.Combobox(frame, values=['principal', 'asistente', 'auxiliar'], width=28)
        combo_rol.set('principal')
        combo_rol.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Peso Influencia:").grid(row=4, column=0, sticky='w', pady=5)
        entry_peso = ttk.Entry(frame, width=30)
        entry_peso.insert(0, "1.00")
        entry_peso.grid(row=4, column=1, pady=5)
        
        def guardar():
            try:
                self.db.insertar_arbitro(
                    entry_nombre.get(),
                    entry_apellidos.get(),
                    entry_fecha.get(),
                    combo_rol.get(),
                    float(entry_peso.get())
                )
                messagebox.showinfo("Éxito", "Árbitro insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_jornada(self):
        """Ventana para insertar jornada"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Jornada")
        ventana.geometry("450x350")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nueva Jornada", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        # Obtener temporadas
        temporadas = self.db.obtener_temporadas()
        if not temporadas:
            messagebox.showwarning("Advertencia", "Primero debes crear una temporada")
            ventana.destroy()
            return
        
        temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
        
        ttk.Label(frame, text="Temporada:").grid(row=0, column=0, sticky='w', pady=5)
        combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=35)
        combo_temp.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Número de Jornada:").grid(row=1, column=0, sticky='w', pady=5)
        entry_numero = ttk.Entry(frame, width=37)
        entry_numero.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, sticky='w', pady=5)
        entry_fecha = ttk.Entry(frame, width=37)
        entry_fecha.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Estado:").grid(row=3, column=0, sticky='w', pady=5)
        entry_estado = ttk.Entry(frame, width=37)
        entry_estado.insert(0, "programada")
        entry_estado.grid(row=3, column=1, pady=5)
        
        def guardar():
            try:
                id_temp = temp_dict[combo_temp.get()]
                self.db.insertar_jornada(
                    id_temp,
                    int(entry_numero.get()),
                    entry_fecha.get(),
                    entry_estado.get()
                )
                messagebox.showinfo("Éxito", "Jornada insertada correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    def ventana_encuentro(self):
        """Ventana para insertar encuentro"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar Encuentro")
        ventana.geometry("500x500")
        ventana.configure(bg='#ffffff')
        
        ttk.Label(ventana, text="Nuevo Encuentro", style='Title.TLabel').pack(pady=10)
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=10, padx=20, fill='both')
        
        # Obtener temporadas para jornadas
        temporadas = self.db.obtener_temporadas()
        if not temporadas:
            messagebox.showwarning("Advertencia", "Primero debes crear una temporada")
            ventana.destroy()
            return
        
        ttk.Label(frame, text="Selecciona Temporada:").grid(row=0, column=0, sticky='w', pady=5)
        temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
        combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=40)
        combo_temp.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Jornada:").grid(row=1, column=0, sticky='w', pady=5)
        combo_jornada = ttk.Combobox(frame, width=40)
        combo_jornada.grid(row=1, column=1, pady=5)
        
        def cargar_jornadas(event):
            id_temp = temp_dict[combo_temp.get()]
            jornadas = self.db.obtener_jornadas(id_temp)
            jorn_dict = {f"{j['id_jornada']} - Jornada {j['numero_jornada']}": j['id_jornada'] for j in jornadas}
            combo_jornada['values'] = list(jorn_dict.keys())
            combo_jornada.jorn_dict = jorn_dict
        
        combo_temp.bind('<<ComboboxSelected>>', cargar_jornadas)
        
        # Obtener equipos
        equipos = self.db.obtener_equipos()
        if not equipos:
            messagebox.showwarning("Advertencia", "Primero debes crear equipos")
            ventana.destroy()
            return
        
        eq_dict = {f"{e['id_equipo']} - {e['nombre_equipo']}": e['id_equipo'] for e in equipos}
        
        ttk.Label(frame, text="Equipo Local:").grid(row=2, column=0, sticky='w', pady=5)
        combo_local = ttk.Combobox(frame, values=list(eq_dict.keys()), width=40)
        combo_local.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Equipo Visitante:").grid(row=3, column=0, sticky='w', pady=5)
        combo_visitante = ttk.Combobox(frame, values=list(eq_dict.keys()), width=40)
        combo_visitante.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Fecha/Hora (YYYY-MM-DD HH:MM:SS):").grid(row=4, column=0, sticky='w', pady=5)
        entry_fecha = ttk.Entry(frame, width=42)
        entry_fecha.insert(0, "2024-08-20 20:00:00")
        entry_fecha.grid(row=4, column=1, pady=5)
        
        ttk.Label(frame, text="Resultado Local (opcional):").grid(row=5, column=0, sticky='w', pady=5)
        entry_res_local = ttk.Entry(frame, width=42)
        entry_res_local.grid(row=5, column=1, pady=5)
        
        ttk.Label(frame, text="Resultado Visitante (opcional):").grid(row=6, column=0, sticky='w', pady=5)
        entry_res_visitante = ttk.Entry(frame, width=42)
        entry_res_visitante.grid(row=6, column=1, pady=5)
        
        def guardar():
            try:
                id_jornada = combo_jornada.jorn_dict[combo_jornada.get()]
                id_local = eq_dict[combo_local.get()]
                id_visitante = eq_dict[combo_visitante.get()]
                
                res_local = int(entry_res_local.get()) if entry_res_local.get() else None
                res_visitante = int(entry_res_visitante.get()) if entry_res_visitante.get() else None
                
                self.db.insertar_encuentro(
                    id_jornada, id_local, id_visitante,
                    entry_fecha.get(), res_local, res_visitante
                )
                messagebox.showinfo("Éxito", "Encuentro insertado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="💾 Guardar", command=guardar,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                 width=15).pack(pady=20)
    
    # ==================== MÉTODOS DE CONSULTA ====================
    
    def ver_temporadas(self):
        """Muestra todas las temporadas"""
        try:
            temporadas = self.db.obtener_temporadas()
            self.texto_resultados.delete('1.0', tk.END)
            
            if not temporadas:
                self.texto_resultados.insert(tk.END, "No hay temporadas registradas.")
                return
            
            self.texto_resultados.insert(tk.END, "📅 TEMPORADAS REGISTRADAS\n")
            self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
            
            for temp in temporadas:
                self.texto_resultados.insert(tk.END, f"ID: {temp['id_temporada']}\n")
                self.texto_resultados.insert(tk.END, f"Nombre: {temp['nombre']}\n")
                self.texto_resultados.insert(tk.END, f"Inicio: {temp['fecha_inicio']}\n")
                self.texto_resultados.insert(tk.END, f"Fin: {temp['fecha_fin']}\n")
                self.texto_resultados.insert(tk.END, f"Estado: {temp['estado']}\n")
                self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
        except Exception as e:
            self.texto_resultados.delete('1.0', tk.END)
            self.texto_resultados.insert(tk.END, f"Error: {str(e)}")
    
    def ver_clubes(self):
        """Muestra todos los clubes"""
        try:
            clubes = self.db.obtener_clubes()
            self.texto_resultados.delete('1.0', tk.END)
            
            if not clubes:
                self.texto_resultados.insert(tk.END, "No hay clubes registrados.")
                return
            
            self.texto_resultados.insert(tk.END, "🏟️  CLUBES REGISTRADOS\n")
            self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
            
            for club in clubes:
                self.texto_resultados.insert(tk.END, f"ID: {club['id_club']}\n")
                self.texto_resultados.insert(tk.END, f"Nombre: {club['nombre']}\n")
                self.texto_resultados.insert(tk.END, f"Ciudad: {club['ciudad'] or 'N/A'}\n")
                self.texto_resultados.insert(tk.END, f"Estadio: {club['estadio'] or 'N/A'}\n")
                self.texto_resultados.insert(tk.END, f"Año Fundación: {club['año_fundacion'] or 'N/A'}\n")
                self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
        except Exception as e:
            self.texto_resultados.delete('1.0', tk.END)
            self.texto_resultados.insert(tk.END, f"Error: {str(e)}")
    
    def ver_equipos(self):
        """Muestra todos los equipos"""
        try:
            equipos = self.db.obtener_equipos()
            self.texto_resultados.delete('1.0', tk.END)
            
            if not equipos:
                self.texto_resultados.insert(tk.END, "No hay equipos registrados.")
                return
            
            self.texto_resultados.insert(tk.END, "⚽ EQUIPOS REGISTRADOS\n")
            self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
            
            for equipo in equipos:
                self.texto_resultados.insert(tk.END, f"ID: {equipo['id_equipo']}\n")
                self.texto_resultados.insert(tk.END, f"Nombre: {equipo['nombre_equipo']}\n")
                self.texto_resultados.insert(tk.END, f"Club: {equipo['nombre_club']}\n")
                self.texto_resultados.insert(tk.END, f"Ciudad: {equipo['ciudad']}\n")
                self.texto_resultados.insert(tk.END, f"Categoría: {equipo['categoria']}\n")
                self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
        except Exception as e:
            self.texto_resultados.delete('1.0', tk.END)
            self.texto_resultados.insert(tk.END, f"Error: {str(e)}")
    
    def ver_jugadores(self):
        """Muestra todos los jugadores"""
        try:
            jugadores = self.db.obtener_jugadores()
            self.texto_resultados.delete('1.0', tk.END)
            
            if not jugadores:
                self.texto_resultados.insert(tk.END, "No hay jugadores registrados.")
                return
            
            self.texto_resultados.insert(tk.END, "👤 JUGADORES REGISTRADOS\n")
            self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
            
            for jugador in jugadores:
                self.texto_resultados.insert(tk.END, f"ID: {jugador['id_jugador']}\n")
                self.texto_resultados.insert(tk.END, f"Nombre: {jugador['nombre']} {jugador['apellidos']}\n")
                self.texto_resultados.insert(tk.END, f"Fecha Nac.: {jugador['fecha_nacimiento']}\n")
                self.texto_resultados.insert(tk.END, f"Posición: {jugador['posicion_principal'] or 'N/A'}\n")
                self.texto_resultados.insert(tk.END, f"Pie Dominante: {jugador['pie_dominante'] or 'N/A'}\n")
                self.texto_resultados.insert(tk.END, f"Peso Influencia: {jugador['peso_influencia']}\n")
                self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
        except Exception as e:
            self.texto_resultados.delete('1.0', tk.END)
            self.texto_resultados.insert(tk.END, f"Error: {str(e)}")
    
    def ver_plantilla(self):
        """Muestra la plantilla de un equipo"""
        try:
            # Crear ventana para seleccionar equipo y temporada
            ventana = tk.Toplevel(self.root)
            ventana.title("Ver Plantilla")
            ventana.geometry("400x250")
            ventana.configure(bg='#ffffff')
            
            ttk.Label(ventana, text="Selecciona Equipo y Temporada", style='Title.TLabel').pack(pady=10)
            
            frame = ttk.Frame(ventana)
            frame.pack(pady=10, padx=20, fill='both')
            
            equipos = self.db.obtener_equipos()
            if not equipos:
                messagebox.showwarning("Advertencia", "No hay equipos registrados")
                ventana.destroy()
                return
            
            eq_dict = {f"{e['id_equipo']} - {e['nombre_equipo']}": e['id_equipo'] for e in equipos}
            
            ttk.Label(frame, text="Equipo:").grid(row=0, column=0, sticky='w', pady=5)
            combo_equipo = ttk.Combobox(frame, values=list(eq_dict.keys()), width=35)
            combo_equipo.grid(row=0, column=1, pady=5)
            
            temporadas = self.db.obtener_temporadas()
            if not temporadas:
                messagebox.showwarning("Advertencia", "No hay temporadas registradas")
                ventana.destroy()
                return
            
            temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
            
            ttk.Label(frame, text="Temporada:").grid(row=1, column=0, sticky='w', pady=5)
            combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=35)
            combo_temp.grid(row=1, column=1, pady=5)
            
            def cargar():
                try:
                    id_equipo = eq_dict[combo_equipo.get()]
                    id_temp = temp_dict[combo_temp.get()]
                    
                    plantilla = self.db.obtener_plantilla_equipo(id_equipo, id_temp)
                    self.texto_resultados.delete('1.0', tk.END)
                    
                    if not plantilla:
                        self.texto_resultados.insert(tk.END, "No hay jugadores en esta plantilla.")
                        ventana.destroy()
                        return
                    
                    self.texto_resultados.insert(tk.END, "📋 PLANTILLA\n")
                    self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
                    
                    for jug in plantilla:
                        self.texto_resultados.insert(tk.END, f"Dorsal: {jug['dorsal'] or 'N/A'}\n")
                        self.texto_resultados.insert(tk.END, f"Jugador: {jug['nombre_completo']}\n")
                        self.texto_resultados.insert(tk.END, f"Posición: {jug['posicion_principal'] or 'N/A'}\n")
                        self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
                    
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            tk.Button(ventana, text="Cargar", command=cargar, bg='#2ecc71', fg='white', width=15).pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def ver_encuentros(self):
        """Muestra los encuentros de una jornada"""
        try:
            # Crear ventana para seleccionar jornada
            ventana = tk.Toplevel(self.root)
            ventana.title("Ver Encuentros")
            ventana.geometry("450x250")
            ventana.configure(bg='#ffffff')
            
            ttk.Label(ventana, text="Selecciona Temporada y Jornada", style='Title.TLabel').pack(pady=10)
            
            frame = ttk.Frame(ventana)
            frame.pack(pady=10, padx=20, fill='both')
            
            temporadas = self.db.obtener_temporadas()
            if not temporadas:
                messagebox.showwarning("Advertencia", "No hay temporadas registradas")
                ventana.destroy()
                return
            
            temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
            
            ttk.Label(frame, text="Temporada:").grid(row=0, column=0, sticky='w', pady=5)
            combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=35)
            combo_temp.grid(row=0, column=1, pady=5)
            
            ttk.Label(frame, text="Jornada:").grid(row=1, column=0, sticky='w', pady=5)
            combo_jornada = ttk.Combobox(frame, width=37)
            combo_jornada.grid(row=1, column=1, pady=5)
            
            def cargar_jornadas(event):
                id_temp = temp_dict[combo_temp.get()]
                jornadas = self.db.obtener_jornadas(id_temp)
                jorn_dict = {f"Jornada {j['numero_jornada']}": j['id_jornada'] for j in jornadas}
                combo_jornada['values'] = list(jorn_dict.keys())
                combo_jornada.jorn_dict = jorn_dict
            
            combo_temp.bind('<<ComboboxSelected>>', cargar_jornadas)
            
            def cargar():
                try:
                    if not hasattr(combo_jornada, 'jorn_dict'):
                        messagebox.showwarning("Advertencia", "Selecciona una temporada primero")
                        return
                    
                    id_jornada = combo_jornada.jorn_dict[combo_jornada.get()]
                    encuentros = self.db.obtener_encuentros_jornada(id_jornada)
                    
                    self.texto_resultados.delete('1.0', tk.END)
                    
                    if not encuentros:
                        self.texto_resultados.insert(tk.END, "No hay encuentros en esta jornada.")
                        ventana.destroy()
                        return
                    
                    self.texto_resultados.insert(tk.END, "⚔️  ENCUENTROS\n")
                    self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
                    
                    for enc in encuentros:
                        self.texto_resultados.insert(tk.END, f"ID: {enc['id_encuentro']}\n")
                        self.texto_resultados.insert(tk.END, f"Jornada {enc['numero_jornada']}\n")
                        self.texto_resultados.insert(tk.END, f"{enc['equipo_local']} vs {enc['equipo_visitante']}\n")
                        self.texto_resultados.insert(tk.END, f"Fecha: {enc['fecha_hora']}\n")
                        
                        if enc['resultado_local'] is not None:
                            self.texto_resultados.insert(tk.END, f"Resultado: {enc['resultado_local']} - {enc['resultado_visitante']}\n")
                        else:
                            self.texto_resultados.insert(tk.END, "Resultado: Pendiente\n")
                        
                        self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
                    
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            tk.Button(ventana, text="Cargar", command=cargar, bg='#2ecc71', fg='white', width=15).pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def ver_predicciones(self):
        """Muestra las predicciones de una jornada"""
        try:
            # Crear ventana para seleccionar jornada
            ventana = tk.Toplevel(self.root)
            ventana.title("Ver Predicciones")
            ventana.geometry("450x250")
            ventana.configure(bg='#ffffff')
            
            ttk.Label(ventana, text="Selecciona Temporada y Jornada", style='Title.TLabel').pack(pady=10)
            
            frame = ttk.Frame(ventana)
            frame.pack(pady=10, padx=20, fill='both')
            
            temporadas = self.db.obtener_temporadas()
            if not temporadas:
                messagebox.showwarning("Advertencia", "No hay temporadas registradas")
                ventana.destroy()
                return
            
            temp_dict = {f"{t['id_temporada']} - {t['nombre']}": t['id_temporada'] for t in temporadas}
            
            ttk.Label(frame, text="Temporada:").grid(row=0, column=0, sticky='w', pady=5)
            combo_temp = ttk.Combobox(frame, values=list(temp_dict.keys()), width=35)
            combo_temp.grid(row=0, column=1, pady=5)
            
            ttk.Label(frame, text="Jornada:").grid(row=1, column=0, sticky='w', pady=5)
            combo_jornada = ttk.Combobox(frame, width=37)
            combo_jornada.grid(row=1, column=1, pady=5)
            
            def cargar_jornadas(event):
                id_temp = temp_dict[combo_temp.get()]
                jornadas = self.db.obtener_jornadas(id_temp)
                jorn_dict = {f"Jornada {j['numero_jornada']}": j['id_jornada'] for j in jornadas}
                combo_jornada['values'] = list(jorn_dict.keys())
                combo_jornada.jorn_dict = jorn_dict
            
            combo_temp.bind('<<ComboboxSelected>>', cargar_jornadas)
            
            def cargar():
                try:
                    if not hasattr(combo_jornada, 'jorn_dict'):
                        messagebox.showwarning("Advertencia", "Selecciona una temporada primero")
                        return
                    
                    id_jornada = combo_jornada.jorn_dict[combo_jornada.get()]
                    predicciones = self.db.obtener_predicciones_jornada(id_jornada)
                    
                    self.texto_resultados.delete('1.0', tk.END)
                    
                    if not predicciones:
                        self.texto_resultados.insert(tk.END, "No hay predicciones en esta jornada.")
                        ventana.destroy()
                        return
                    
                    self.texto_resultados.insert(tk.END, "🔮 PREDICCIONES\n")
                    self.texto_resultados.insert(tk.END, "="*80 + "\n\n")
                    
                    for pred in predicciones:
                        self.texto_resultados.insert(tk.END, f"ID: {pred['id_prediccion']}\n")
                        self.texto_resultados.insert(tk.END, f"{pred['equipo_local']} vs {pred['equipo_visitante']}\n")
                        self.texto_resultados.insert(tk.END, f"Probabilidad Local: {pred['probabilidad_local']}%\n")
                        self.texto_resultados.insert(tk.END, f"Probabilidad Empate: {pred['probabilidad_empate']}%\n")
                        self.texto_resultados.insert(tk.END, f"Probabilidad Visitante: {pred['probabilidad_visitante']}%\n")
                        self.texto_resultados.insert(tk.END, f"Pronóstico: {pred['pronostico_final']}\n")
                        self.texto_resultados.insert(tk.END, "-"*80 + "\n\n")
                    
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            tk.Button(ventana, text="Cargar", command=cargar, bg='#2ecc71', fg='white', width=15).pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    
    # Inicializar la interfaz
    app = InterfazPredicciones(root)
    
    # Mostrar ventana
    root.mainloop()