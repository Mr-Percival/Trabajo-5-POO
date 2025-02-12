import tkinter as tk
from math import pi, pow

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def calcular_volumen(self):
        pass

    def calcular_superficie(self):
        pass

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return pi * pow(self.radio, 2) * self.altura

    def calcular_superficie(self):
        return 2 * pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4/3) * pi * pow(self.radio, 3)

    def calcular_superficie(self):
        return 4 * pi * pow(self.radio, 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (1/3) * pow(self.base, 2) * self.altura

    def calcular_superficie(self):
        return pow(self.base, 2) + 2 * self.base * self.apotema

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        self.figura_var = tk.StringVar(value="Cilindro")

        tk.Label(root, text="Seleccione la figura geométrica:").grid(row=0, column=0, columnspan=2)

        self.radio_button = tk.Radiobutton(root, text="Cilindro", variable=self.figura_var, value="Cilindro", command=self.mostrar_campos)
        self.radio_button.grid(row=1, column=0, sticky="w")

        self.esfera_button = tk.Radiobutton(root, text="Esfera", variable=self.figura_var, value="Esfera", command=self.mostrar_campos)
        self.esfera_button.grid(row=2, column=0, sticky="w")

        self.piramide_button = tk.Radiobutton(root, text="Pirámide", variable=self.figura_var, value="Pirámide", command=self.mostrar_campos)
        self.piramide_button.grid(row=3, column=0, sticky="w")

        self.label1 = tk.Label(root, text="Radio: (cms)")
        self.label1.grid(row=1, column=1)
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=1, column=2)

        self.label2 = tk.Label(root, text="Altura: (cms)")
        self.label2.grid(row=2, column=1)
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=2, column=2)

        self.label3 = tk.Label(root, text="Base: (cms)")
        self.label3.grid(row=3, column=1)
        self.entry3 = tk.Entry(root)
        self.entry3.grid(row=3, column=2)

        self.label4 = tk.Label(root, text="Apotema: (cms)")
        self.label4.grid(row=4, column=1)
        self.entry4 = tk.Entry(root)
        self.entry4.grid(row=4, column=2)

        self.resultados = tk.Label(root, text="")
        self.resultados.grid(row=6, column=0, columnspan=3)

        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=5, column=0, columnspan=3)

        self.mostrar_campos()

    def mostrar_campos(self):
        figura = self.figura_var.get()
        if figura == "Cilindro":
            self.label1.grid()
            self.entry1.grid()
            self.label2.grid()
            self.entry2.grid()
            self.label3.grid_remove()
            self.entry3.grid_remove()
            self.label4.grid_remove()
            self.entry4.grid_remove()
        elif figura == "Esfera":
            self.label1.grid()
            self.entry1.grid()
            self.label2.grid_remove()
            self.entry2.grid_remove()
            self.label3.grid_remove()
            self.entry3.grid_remove()
            self.label4.grid_remove()
            self.entry4.grid_remove()
        elif figura == "Pirámide":
            self.label1.grid_remove()
            self.entry1.grid_remove()
            self.label2.grid()
            self.entry2.grid()
            self.label3.grid()
            self.entry3.grid()
            self.label4.grid()
            self.entry4.grid()

    def calcular(self):
        figura = self.figura_var.get()
        try:
            if figura == "Cilindro":
                radio = float(self.entry1.get())
                altura = float(self.entry2.get())
                cilindro = Cilindro(radio, altura)
                volumen = cilindro.volumen
                superficie = cilindro.superficie
            elif figura == "Esfera":
                radio = float(self.entry1.get())
                esfera = Esfera(radio)
                volumen = esfera.volumen
                superficie = esfera.superficie
            elif figura == "Pirámide":
                base = float(self.entry3.get())
                altura = float(self.entry2.get())
                apotema = float(self.entry4.get())
                piramide = Piramide(base, altura, apotema)
                volumen = piramide.volumen
                superficie = piramide.superficie

            resultado_texto = f"Volumen: {volumen:.2f} cm³\nSuperficie: {superficie:.2f} cm²"
            self.resultados.config(text=resultado_texto)
        except ValueError:
            self.resultados.config(text="Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
