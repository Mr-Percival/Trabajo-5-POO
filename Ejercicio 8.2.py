import tkinter as tk
from tkinter import messagebox
import statistics

def calcular():
    try:
        notas = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()), float(entry5.get())]
        promedio = statistics.mean(notas)
        desviacion_estandar = statistics.stdev(notas)
        mayor_nota = max(notas)
        menor_nota = min(notas)
        
        resultado.set(f"Promedio: {promedio:.2f}\nDesviación Estándar: {desviacion_estandar:.2f}\nMayor Nota: {mayor_nota}\nMenor Nota: {menor_nota}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except statistics.StatisticsError:
        messagebox.showerror("Error", "Se requieren al menos dos notas diferentes para calcular la desviación estándar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Notas")

# Crear los widgets
tk.Label(root, text="Ingrese las cinco notas del estudiante:").grid(row=0, columnspan=2)

tk.Label(root, text="Nota 1:").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

tk.Label(root, text="Nota 2:").grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Label(root, text="Nota 3:").grid(row=3, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

tk.Label(root, text="Nota 4:").grid(row=4, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=4, column=1)

tk.Label(root, text="Nota 5:").grid(row=5, column=0)
entry5 = tk.Entry(root)
entry5.grid(row=5, column=1)

tk.Button(root, text="Calcular", command=calcular).grid(row=6, columnspan=2)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).grid(row=7, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()