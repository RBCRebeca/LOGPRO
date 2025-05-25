import tkinter as tk
import subprocess
import sys
import os

def voltar_menu():
    janela.destroy()
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_menu = os.path.join(diretorio_atual, "menu.py")
    if os.path.exists(caminho_menu):
        subprocess.Popen([sys.executable, caminho_menu])
    else:
        print(f"'menu.py' não encontrado em: {caminho_menu}")

# Função genérica para abrir scripts
def abrir_arquivo(script):
    if os.path.exists(script):
        subprocess.Popen([sys.executable, script])
    else:
        print(f"Arquivo '{script}' não encontrado.")

# Funções para cada botão
def abrir_clientes():
    abrir_arquivo("cadastro_clientes.py")

def abrir_imoveis():
    abrir_arquivo("cadastro_imoveis.py")

def abrir_solicitacoes():
    abrir_arquivo("solicitacoes.py")

def abrir_status():
    abrir_arquivo("status_clientes.py")

# Janela principal
janela = tk.Tk()
janela.title("Menu - Sistema de Locação")
janela.configure(bg='#f2f2f2')
janela.geometry("400x350")

# Fonte dos títulos e botões
titulo_font = ("Calibri", 16)
button_font = ("Calibri", 12)

# Faixa superior com título
top_frame = tk.Frame(janela, bg="#cc0000", height=50)
top_frame.pack(fill='x')
tk.Label(top_frame, text="Menu Principal", bg="#cc0000", fg="white", font=titulo_font).pack(pady=10)

# Área de botões
conteudo = tk.Frame(janela, bg="#f2f2f2")
conteudo.pack(pady=20)

# Botões com fundo vermelho e texto branco
tk.Button(conteudo, text="Cadastro de Clientes", width=30, bg="#cc0000", fg="white", font=button_font, command=abrir_clientes, activebackground="#990000", activeforeground="white").pack(pady=5)
tk.Button(conteudo, text="Cadastro de Imóveis", width=30, bg="#cc0000", fg="white", font=button_font, command=abrir_imoveis, activebackground="#990000", activeforeground="white").pack(pady=5)
tk.Button(conteudo, text="Solicitações de Locação", width=30, bg="#cc0000", fg="white", font=button_font, command=abrir_solicitacoes, activebackground="#990000", activeforeground="white").pack(pady=5)
tk.Button(conteudo, text="Ver Status de Clientes", width=30, bg="#cc0000", fg="white", font=button_font, command=abrir_status, activebackground="#990000", activeforeground="white").pack(pady=5)

# Loop principal
janela.mainloop()
