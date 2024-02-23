import tkinter as tk
from tkinter import messagebox

def convertidorDePesosMexicanosADolar():
    try:
        dolares = float(captura1.get())
        if dolares:
            dolarAPesosMexicanos = 17.12  
            pesosMexicanos = dolares * dolarAPesosMexicanos
            messagebox.showinfo("Resultado", f"{dolares} dólares son {pesosMexicanos} pesos mexicanos.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida en dólares.")

ventana = tk.Tk()
ventana.title("Conversor de Dólares a Pesos Mexicanos")

dolar = tk.Label(ventana, text="Ingrese la cantidad en dólares:")
dolar.pack()

captura1 = tk.Entry(ventana)
captura1.pack()

boton = tk.Button(ventana, text="Convertir", command=convertidorDePesosMexicanosADolar)
boton.pack()

ventana.mainloop()
