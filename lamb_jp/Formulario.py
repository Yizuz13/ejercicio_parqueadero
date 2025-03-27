import tkinter as Ventana

class Formulario:

    def _init_(self): 
        self.ventana_formulario = Ventana.Tk() 
        self.label_nombre = Ventana.Label(self.ventana_formulario, text="digite el nombre: ") 
        self.entry_nombre = Ventana.Entry (self.ventana_formulario) 
        self.boton_enviar = Ventana.Button(self.ventana_formulario, text="Guardar Cliente", command=self.evento_click) 
        self.boton_limpiar = Ventana.Button(self.ventana_formulario, text="limpiar", command= lambda : self.evento_borrar()) 

        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre.grid() 
        self.boton_enviar.grid() 
        self.boton_limpiar.grid() 

        self.ventana_formulario.mainloop()