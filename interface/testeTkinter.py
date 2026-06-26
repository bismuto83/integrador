import tkinter as tk
from tkinter import ttk


def calcular():
    resultado_var.set("Implementar depois")


janela = tk.Tk()
janela.title("Calculadora de Integrais definidas")
janela.geometry("600x300")


ttk.Label(janela, text="Função f(x):").pack(pady=(10, 0))
entrada_funcao = ttk.Entry(janela, width=40)
entrada_funcao.pack()
entrada_funcao.insert(0, "x**2")


frame_parametros = ttk.Frame(janela)
frame_parametros.pack(pady=15)
ttk.Label(frame_parametros, text="a").grid(row=0, column=0)
entrada_a = ttk.Entry(frame_parametros, width=8)
entrada_a.grid(row=0, column=1)
entrada_a.insert(0, "0")

ttk.Label(frame_parametros, text="b").grid(row=0, column=2, padx=(15, 0))

entrada_b = ttk.Entry(frame_parametros, width=8)
entrada_b.grid(row=0, column=3)
entrada_b.insert(0, "1")

ttk.Label(frame_parametros, text="n").grid(row=0, column=4, padx=(15, 0))

entrada_n = ttk.Entry(frame_parametros, width=10)
entrada_n.grid(row=0, column=5)
entrada_n.insert(0, "1000")


ttk.Button(
    janela,
    text="Calcular",
    command=calcular
).pack()


resultado_var = tk.StringVar()
resultado_var.set("Resultado aparecerá aqui")
ttk.Label(
    janela,
    textvariable=resultado_var,
    font=("Arial", 11)
).pack(pady=20)


janela.mainloop() 
