import tkinter as tk
from tkinter import messagebox

def bienvenida():
    messagebox.showinfo("Bienvenida", "¡Bienvenido a esta aplicación!")

def cerrar():
    exit()

ventana=tk.Tk()
ventana.title("Interfaz con Botones")
ventana.geometry("500x500")

boton1= tk.Button(ventana, text="Cerrar App", command=cerrar)
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Mensaje de Bienvenida", command=bienvenida)
boton2.pack(pady=10)

ventana.mainloop()
