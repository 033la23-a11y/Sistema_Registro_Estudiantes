import tkinter as tk
from tkinter import ttk, messagebox
from estudiante import Estudiante
from gestor_estudiantes import GestorEstudiantes

class InterfazEstudiantes:
    """Vista Tkinter: interacción con el usuario y coordinación con el gestor."""
    def __init__(self, raiz: tk.Tk, gestor=None):
        self.raiz = raiz
        self.gestor = gestor or GestorEstudiantes()
        self.raiz.title('Sistema de Registro de Estudiantes')
        self.raiz.geometry('850x580')
        self.raiz.minsize(730, 500)
        self.raiz.configure(bg='#f1f5f9')
        self.campos = {}
        self._crear_componentes()
        self.actualizar_tabla()

    def _crear_componentes(self):
        estilo = ttk.Style()
        if 'clam' in estilo.theme_names():
            estilo.theme_use('clam')
        estilo.configure('Treeview', rowheight=27, font=('Arial', 10))
        estilo.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        encabezado = tk.Frame(self.raiz, bg='#163a63', pady=17)
        encabezado.pack(fill='x')
        tk.Label(encabezado, text='REGISTRO DE ESTUDIANTES', font=('Arial', 19, 'bold'), bg='#163a63', fg='white').pack()
        tk.Label(encabezado, text='Implementación de Software · Programación Orientada a Objetos', font=('Arial', 10), bg='#163a63', fg='#dbeafe').pack(pady=(5, 0))
        cuerpo = tk.Frame(self.raiz, bg='#f1f5f9', padx=22, pady=16)
        cuerpo.pack(fill='both', expand=True)
        formulario = tk.LabelFrame(cuerpo, text=' Datos del estudiante ', font=('Arial', 11, 'bold'), bg='white', padx=14, pady=13)
        formulario.pack(fill='x')
        for i, (clave, etiqueta) in enumerate((('matricula', 'Matrícula'), ('nombre', 'Nombre completo'), ('edad', 'Edad'), ('carrera', 'Carrera'))):
            fila, columna = divmod(i, 2)
            tk.Label(formulario, text=etiqueta, bg='white', anchor='w').grid(row=fila * 2, column=columna, sticky='ew', padx=9, pady=(2, 0))
            entrada = ttk.Entry(formulario, width=35)
            entrada.grid(row=fila * 2 + 1, column=columna, sticky='ew', padx=9, pady=(3, 10))
            self.campos[clave] = entrada
        formulario.columnconfigure(0, weight=1)
        formulario.columnconfigure(1, weight=1)
        botones = tk.Frame(cuerpo, bg='#f1f5f9')
        botones.pack(fill='x', pady=13)
        acciones = [('Registrar', self.registrar), ('Buscar', self.buscar), ('Mostrar todos', self.actualizar_tabla), ('Eliminar', self.eliminar), ('Limpiar', self.limpiar)]
        for titulo, comando in acciones:
            tk.Button(botones, text=titulo, command=comando, bg='#245c91' if titulo != 'Eliminar' else '#b42332', fg='white', relief='flat', font=('Arial', 10, 'bold'), padx=12, pady=9, cursor='hand2').pack(side='left', padx=(0, 8))
        marco_tabla = tk.LabelFrame(cuerpo, text=' Estudiantes registrados ', font=('Arial', 11, 'bold'), bg='white', padx=10, pady=10)
        marco_tabla.pack(fill='both', expand=True)
        columnas = ('matricula', 'nombre', 'edad', 'carrera')
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas, show='headings', selectmode='browse')
        for col, titulo, ancho in [('matricula', 'Matrícula', 125), ('nombre', 'Nombre', 260), ('edad', 'Edad', 70), ('carrera', 'Carrera', 220)]:
            self.tabla.heading(col, text=titulo)
            self.tabla.column(col, width=ancho, minwidth=60)
        barra = ttk.Scrollbar(marco_tabla, orient='vertical', command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra.set)
        self.tabla.pack(side='left', fill='both', expand=True)
        barra.pack(side='right', fill='y')
        self.tabla.bind('<<TreeviewSelect>>', self._seleccionar)
        self.estado = tk.StringVar(value='Sistema listo.')
        tk.Label(self.raiz, textvariable=self.estado, anchor='w', bg='#e2e8f0', padx=12, pady=7).pack(fill='x')

    def _valores(self):
        return {clave: entrada.get().strip() for clave, entrada in self.campos.items()}

    def registrar(self):
        try:
            datos = self._valores()
            if not datos['edad']:
                raise ValueError('La edad es obligatoria.')
            try:
                edad = int(datos['edad'])
            except ValueError as error:
                raise ValueError('La edad debe ser un número entero.') from error
            estudiante = Estudiante(datos['matricula'], datos['nombre'], edad, datos['carrera'])
            self.gestor.registrar(estudiante)
            self.actualizar_tabla()
            self.limpiar()
            self.estado.set(f'Estudiante {estudiante.matricula} registrado correctamente.')
            messagebox.showinfo('Registro exitoso', 'Estudiante registrado correctamente.')
        except (ValueError, TypeError) as error:
            messagebox.showerror('Error de registro', str(error))
            self.estado.set(f'Error: {error}')

    def buscar(self):
        try:
            estudiante = self.gestor.buscar(self.campos['matricula'].get())
            if estudiante is None:
                messagebox.showinfo('Búsqueda', 'No se encontró esa matrícula.')
                self.estado.set('Matrícula no encontrada.')
                return
            self._mostrar_filas([estudiante])
            self.estado.set(f'Encontrado: {estudiante.mostrar_informacion()}')
        except ValueError as error:
            messagebox.showerror('Error', str(error))

    def eliminar(self):
        matricula = self.campos['matricula'].get().strip()
        if not matricula:
            messagebox.showerror('Error', 'Escribe o selecciona una matrícula.')
            return
        if not self.gestor.buscar(matricula):
            messagebox.showinfo('Eliminar', 'No se encontró esa matrícula.')
            return
        if messagebox.askyesno('Confirmar eliminación', f'¿Eliminar al estudiante {matricula.upper()}?'):
            self.gestor.eliminar(matricula)
            self.actualizar_tabla()
            self.limpiar()
            self.estado.set(f'Estudiante {matricula.upper()} eliminado.')

    def actualizar_tabla(self):
        self._mostrar_filas(self.gestor.listar())
        self.estado.set('Lista de estudiantes actualizada.')

    def _mostrar_filas(self, estudiantes):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for estudiante in estudiantes:
            self.tabla.insert('', 'end', values=(estudiante.matricula, estudiante.nombre, estudiante.edad, estudiante.carrera))

    def _seleccionar(self, _evento):
        seleccion = self.tabla.selection()
        if seleccion:
            valores = self.tabla.item(seleccion[0], 'values')
            for clave, valor in zip(('matricula', 'nombre', 'edad', 'carrera'), valores):
                self.campos[clave].delete(0, tk.END)
                self.campos[clave].insert(0, valor)

    def limpiar(self):
        for entrada in self.campos.values():
            entrada.delete(0, tk.END)
        self.campos['matricula'].focus_set()
