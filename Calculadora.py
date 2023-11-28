# Importar a biblioteca tkinter
import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title('Calculadora')

# Funções para realizar as operações matemáticas
def calcular_soma():
    try:
        resultado = float(entry_valor1.get()) + float(entry_valor2.get())
        label_resultado['text'] = 'Resultado: {}'.format(resultado)
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, digite valores válidos')

def calcular_subtracao():
    try:
        resultado = float(entry_valor1.get()) - float(entry_valor2.get())
        label_resultado['text'] = 'Resultado: {}'.format(resultado)
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, digite valores válidos')

def calcular_multiplicacao():
    try:
        resultado = float(entry_valor1.get()) * float(entry_valor2.get())
        label_resultado['text'] = 'Resultado: {}'.format(resultado)
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, digite valores válidos')

def calcular_divisao():
    try:
        resultado = float(entry_valor1.get()) / float(entry_valor2.get())
        label_resultado['text'] = 'Resultado: {}'.format(resultado)
    except ZeroDivisionError:
        messagebox.showerror('Erro', 'Não é possível dividir por zero')
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, digite valores válidos')

# Criar os widgets da janela principal
frame_entrada = tk.Frame(janela_principal)
frame_entrada.pack(padx=10, pady=10)

frame_operacoes = tk.Frame(janela_principal)
frame_operacoes.pack(padx=10, pady=10)

frame_resultado = tk.Frame(janela_principal)
frame_resultado.pack(padx=10, pady=10)

label_valor1 = tk.Label(frame_entrada, text='Digite o 1º valor:')
label_valor1.pack(side='left')

entry_valor1 = tk.Entry(frame_entrada)
entry_valor1.pack(side='left')

label_valor2 = tk.Label(frame_entrada, text='Digite o 2º valor:')
label_valor2.pack(side='left')

entry_valor2 = tk.Entry(frame_entrada)
entry_valor2.pack(side='left')

botao_soma = tk.Button(frame_operacoes, text='Soma', command=calcular_soma)
botao_soma.pack(side='left')

botao_subtracao = tk.Button(frame_operacoes, text='Subtração', command=calcular_subtracao)
botao_subtracao.pack(side='left')

botao_multiplicacao = tk.Button(frame_operacoes, text='Multiplicação', command=calcular_multiplicacao)
botao_multiplicacao.pack(side='left')

botao_divisao = tk.Button(frame_operacoes, text='Divisão', command=calcular_divisao)
botao_divisao.pack(side='left')

label_resultado = tk.Label(frame_resultado, text='Resultado:')
label_resultado.pack(side='left')

# Executar o loop principal
janela_principal.mainloop()