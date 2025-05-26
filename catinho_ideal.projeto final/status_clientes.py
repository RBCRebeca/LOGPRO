import tkinter as tk
from conexao import conectar
import subprocess
import sys
import os

def voltar_menu():
    janela.destroy()
    # Caminho dinâmico para menu_principal.py (mesma pasta do script atual)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_menu = os.path.join(diretorio_atual, "menu_principal.py")

    # Verifica se o arquivo menu_principal.py existe antes de abrir
    if os.path.exists(caminho_menu):
        subprocess.Popen([sys.executable, caminho_menu])
    else:
        print(f"'menu_principal.py' não encontrado em: {caminho_menu}")

def carregar_status():
    lista.delete(0, tk.END)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.cli_nome, s.status_solicitacao, s.status_aluguel
            FROM cliente c
            JOIN solicitacao_locacao s ON c.id_cli = s.id_inquilino
        """)
        for row in cursor.fetchall():
            nome, status_solicitacao, status_aluguel = row
            lista.insert(tk.END, f"{nome} | Solicitação: {status_solicitacao} | Aluguel: {status_aluguel}")
    except Exception as e:
        lista.insert(tk.END, f"Erro ao carregar dados: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

# Janela
janela = tk.Tk()
janela.title("Status dos Clientes")
janela.configure(bg="white")
janela.geometry("500x400")

# Faixa superior com título
faixa = tk.Frame(janela, bg="#cc0000", height=40)
faixa.pack(fill=tk.X)
titulo = tk.Label(faixa, text="Status dos Clientes", bg="#cc0000", fg="white", font=("Arial", 14, "bold"))
titulo.pack(pady=5)

# Lista de status
lista = tk.Listbox(janela, width=70, font=("Arial", 10))
lista.pack(pady=(20, 10))

# Botões com estilo vermelho e texto branco
btn_carregar = tk.Button(
    janela,
    text="Carregar Status",
    command=carregar_status,
    bg="#cc0000",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#990000",
    activeforeground="white"
)
btn_carregar.pack(pady=5)

btn_voltar = tk.Button(
    janela,
    text="Voltar ao Menu",
    command=voltar_menu,
    bg="#cc0000",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#990000",
    activeforeground="white"
)
btn_voltar.pack(pady=5)

# Inicializa carregando dados
carregar_status()
janela.mainloop()
