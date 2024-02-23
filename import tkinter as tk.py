import tkinter as tk
from tkinter import messagebox

def verificadorDeEdad():
    edad=edad1.get()

    if edad:
        edad=int(edad)
        if edad>=18:
            messagebox.showinfo("Resultado", "Eres mayor de edad.")
        else:
            messagebox.showinfo("Resultado", "Eres menor de edad.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa una edad válida.")

ventana=tk.Tk()
ventana.title("Verificar Edad")
ventana.geometry("500x500")

edad = tk.Label(ventana, text="Ingresa tu edad:")
edad.pack()
edad1 = tk.Entry(ventana)
edad1.pack()

boton=tk.Button(ventana, text="Verificar", command=verificadorDeEdad)
boton.pack()

ventana.mainloop()
