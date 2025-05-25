import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def cadastrar_cliente():
    nome = entry_nome.get().strip()
    cpf = entry_cpf.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    if nome and cpf:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cliente (cli_nome, cli_cpf, cli_email, cli_telefone) VALUES (%s, %s, %s, %s)", (nome, cpf, email, telefone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente cadastrado.")
        listar_clientes()
    else:
        messagebox.showwarning("Atenção", "Nome e CPF são obrigatórios.")

def listar_clientes():
    lista.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    for row in cursor.fetchall():
        lista.insert(tk.END, f"{row[0]} | {row[1]} | CPF: {row[2]}")
    conn.close()

def excluir_cliente():
    selecao = lista.curselection()
    if selecao:
        cliente_selecionado = lista.get(selecao[0])
        id_cliente = cliente_selecionado.split(" | ")[0]
        confirmar = messagebox.askyesno("Confirmação", "Deseja realmente excluir este cliente?")
        if confirmar:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cliente WHERE id_cli = %s", (id_cliente,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Cliente excluído.")
            listar_clientes()
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para excluir.")

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.configure(bg='white')
janela.geometry("500x500")

# Fontes
label_font = ("Calibri", 12)
entry_font = ("Calibri", 12)
button_font = ("Calibri", 12)
list_font = ("Calibri", 11)
titulo_font = ("Calibri", 16)

# Faixa vermelha com título
top_frame = tk.Frame(janela, bg="#cc0000", height=50)
top_frame.pack(fill='x')
tk.Label(top_frame, text="Cadastro de Clientes", bg="#cc0000", fg="white", font=titulo_font).pack(pady=10)

# Frame para o restante do conteúdo
conteudo = tk.Frame(janela, bg="white")
conteudo.pack(pady=10)

# Campos de entrada e labels
tk.Label(conteudo, text="Nome", bg="white", font=label_font).grid(row=0, column=0, sticky='e', padx=10, pady=5)
entry_nome = tk.Entry(conteudo, font=entry_font, bg="#f0f0f0")
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(conteudo, text="CPF", bg="white", font=label_font).grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_cpf = tk.Entry(conteudo, font=entry_font, bg="#f0f0f0")
entry_cpf.grid(row=1, column=1, padx=10, pady=5)

tk.Label(conteudo, text="E-mail", bg="white", font=label_font).grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_email = tk.Entry(conteudo, font=entry_font, bg="#f0f0f0")
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(conteudo, text="Telefone", bg="white", font=label_font).grid(row=3, column=0, sticky='e', padx=10, pady=5)
entry_telefone = tk.Entry(conteudo, font=entry_font, bg="#f0f0f0")
entry_telefone.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_cadastrar = tk.Button(conteudo, text="Cadastrar", command=cadastrar_cliente, bg="#cc0000", fg="white", font=button_font)
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10, ipadx=20)

btn_excluir = tk.Button(conteudo, text="Excluir Selecionado", command=excluir_cliente, bg="#cc0000", fg="white", font=button_font)
btn_excluir.grid(row=5, column=0, columnspan=2, pady=5, ipadx=10)

# Lista de clientes
lista = tk.Listbox(janela, width=60, height=10, font=list_font)
lista.pack(padx=10, pady=10)

listar_clientes()
janela.mainloop()