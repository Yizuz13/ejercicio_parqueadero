import tkinter as Ventana
import datetime

class Formulario:
    def __init__(self):
        self.ventana_formulario = Ventana.Tk()
        self.ventana_formulario.title("Registro de Vehículos")
        self.ventana_formulario.geometry("400x400")

        # Crear los widgets de la interfaz
        self.label_placa = Ventana.Label(self.ventana_formulario, text="Placa (Ej: ABC-123): ")
        self.entry_placa = Ventana.Entry(self.ventana_formulario)
        
        self.label_marca = Ventana.Label(self.ventana_formulario, text="Marca (Ej: Mazda): ")
        self.entry_marca = Ventana.Entry(self.ventana_formulario)
        
        self.label_color = Ventana.Label(self.ventana_formulario, text="Color (Ej: Blanco): ")
        self.entry_color = Ventana.Entry(self.ventana_formulario)
        
        self.label_tipo = Ventana.Label(self.ventana_formulario, text="Tipo (Residente/Visitante): ")
        self.entry_tipo = Ventana.Entry(self.ventana_formulario)
        
        self.label_error = Ventana.Label(self.ventana_formulario, text="", fg="red")  # Para mostrar errores

        self.boton_guardar = Ventana.Button(self.ventana_formulario, text="Guardar", command=self.guardar_vehiculo)
        self.boton_limpiar = Ventana.Button(self.ventana_formulario, text="Limpiar", command=lambda: self.limpiar_campos())
        self.boton_mostrar = Ventana.Button(self.ventana_formulario, text="Mostrar Registro", command=self.mostrar_registro)

        # Mostrar los registros en una etiqueta
        self.label_registro = Ventana.Label(self.ventana_formulario, text="Registros: ")

        # Ubicación de los widgets con grid
        self.label_placa.grid(row=0, column=0, pady=10, padx=10)
        self.entry_placa.grid(row=0, column=1, pady=10, padx=10)
        
        self.label_marca.grid(row=1, column=0, pady=10, padx=10)
        self.entry_marca.grid(row=1, column=1, pady=10, padx=10)
        
        self.label_color.grid(row=2, column=0, pady=10, padx=10)
        self.entry_color.grid(row=2, column=1, pady=10, padx=10)
        
        self.label_tipo.grid(row=3, column=0, pady=10, padx=10)
        self.entry_tipo.grid(row=3, column=1, pady=10, padx=10)

        self.label_error.grid(row=4, column=0, columnspan=2)  # Para mostrar errores
        self.boton_guardar.grid(row=5, column=0, pady=10, padx=10)
        self.boton_limpiar.grid(row=5, column=1, pady=10, padx=10)
        self.boton_mostrar.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

        self.label_registro.grid(row=7, column=0, columnspan=2, pady=10)

        self.lista_vehiculos = []  # Lista para almacenar los vehículos como diccionarios
        self.formulario()
        self.ventana_formulario.mainloop()

    def formulario(self):
        # Establecer el tamaño de la ventana sin agregar nada más
        self.ventana_formulario.geometry("400x400")

    def guardar_vehiculo(self):
        # Recoger los datos de los campos
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        color = self.entry_color.get()
        tipo = self.entry_tipo.get()

        # Validar si algún campo está vacío
        if not placa or not marca or not color or not tipo:
            self.label_error.config(text="Todos los campos son obligatorios.")
            return

        # Crear el diccionario del vehículo
        vehiculo = {
            'placa': placa,
            'marca': marca,
            'color': color,
            'tipo': tipo,
            'hora_ingreso': datetime.datetime.now().strftime("%H:%M:%S")  # Hora de ingreso
        }

        # Guardar el vehículo en la lista
        self.lista_vehiculos.append(vehiculo)

        # Limpiar los campos
        self.limpiar_campos()

        # Mostrar un mensaje de éxito
        self.label_error.config(text="Vehículo guardado exitosamente.")

    def limpiar_campos(self):
        # Limpiar los campos de entrada
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')

    def mostrar_registro(self):
        # Mostrar los vehículos registrados en consola y en la interfaz
        if not self.lista_vehiculos:
            self.label_registro.config(text="No hay vehículos registrados.")
        else:
            registros = "\n".join([f"Placa: {v['placa']}, Marca: {v['marca']}, Color: {v['color']}, Tipo: {v['tipo']}, Hora: {v['hora_ingreso']}" for v in self.lista_vehiculos])
            self.label_registro.config(text=registros)
            # Mostrar los registros en consola
            for vehiculo in self.lista_vehiculos:
                print(f"Placa: {vehiculo['placa']}, Marca: {vehiculo['marca']}, Color: {vehiculo['color']}, Tipo: {vehiculo['tipo']}, Hora: {vehiculo['hora_ingreso']}")

# Crear una instancia de la clase Formulario
obj_formulario = Formulario()