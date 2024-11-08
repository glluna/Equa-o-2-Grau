import tkinter as tk
from tkinter import messagebox
import math


def calcular_raizes():
    try:
        # Obter os valores dos coeficientes
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Calcular o discriminante
        delta = b ** 2 - 4 * a * c

        # Verificar o discriminante para determinar as raízes
        if delta > 0:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            resultado = f"Duas raízes reais: x1 = {raiz1:.2f}, x2 = {raiz2:.2f}"
        elif delta == 0:
            raiz = -b / (2 * a)
            resultado = f"Uma raiz real: x = {raiz:.2f}"
        else:
            resultado = "Não há raízes reais."

        # Exibir o resultado
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "O valor de 'a' não pode ser zero em uma equação do segundo grau.")


# Configurar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Equações do 2º Grau")

# Labels e caixas de entrada para os coeficientes a, b e c
tk.Label(janela, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(janela)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(janela)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(janela)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular as raízes
botao_calcular = tk.Button(janela, text="Calcular Raízes", command=calcular_raizes)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar a interface gráfica
janela.mainloop()
