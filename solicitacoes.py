import tkinter as tk
from tkinter import messagebox, ttk
from conexao import conectar
import uuid

def gerar_id_solicitacao():
    return "SOL" + str(uuid.uuid4())[:6].upper()

def registrar_solicitacao():
    id_cliente = entry_id_cliente.get().strip()
    id_imovel = entry_id_imovel.get().strip()
    data_inicio = entry_data_inicio.get().strip()
    data_fim = entry_data_fim.get().strip()
    valor = entry_valor.get().strip()
    status = combo_status.get()

    if id_cliente and id_imovel and data_inicio and data_fim and valor and status:
        id_solicitacao = gerar_id_solicitacao()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO solicitacao_locacao 
            (id_solicitacao, id_imovel, id_inquilino, data_inicio, data_fim, valor_mensal, status_aluguel, status_solicitacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (id_solicitacao, id_imovel, id_cliente, data_inicio, data_fim, valor, 'ativo', status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Solicitação registrada com sucesso!")
        limpar_campos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def limpar_campos():
    entry_id_cliente.delete(0, tk.END)
    entry_id_imovel.delete(0, tk.END)
    entry_data_inicio.delete(0, tk.END)
    entry_data_fim.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    combo_status.set("")

janela = tk.Tk()
janela.title("Solicitação de Locação")
janela.geometry("420x460")
janela.configure(bg="#f2f2f2")

faixa = tk.Frame(janela, bg="#cc0000", height=50)
faixa.pack(fill='x')
tk.Label(faixa, text="Solicitação de Locação", bg="#cc0000", fg="white", font=("Calibri", 16)).pack(pady=10)

label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

form_frame = tk.Frame(janela, bg="#f2f2f2")
form_frame.pack(pady=10)

tk.Label(form_frame, text="ID do Cliente", bg="#f2f2f2", font=label_font).grid(row=0, column=0, sticky='e', padx=10, pady=5)
entry_id_cliente = tk.Entry(form_frame, font=entry_font, bg="white")
entry_id_cliente.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="ID do Imóvel", bg="#f2f2f2", font=label_font).grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_id_imovel = tk.Entry(form_frame, font=entry_font, bg="white")
entry_id_imovel.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Data de Início", bg="#f2f2f2", font=label_font).grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_data_inicio = tk.Entry(form_frame, font=entry_font, bg="white")
entry_data_inicio.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Data de Fim", bg="#f2f2f2", font=label_font).grid(row=3, column=0, sticky='e', padx=10, pady=5)
entry_data_fim = tk.Entry(form_frame, font=entry_font, bg="white")
entry_data_fim.grid(row=3, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Valor Mensal (R$)", bg="#f2f2f2", font=label_font).grid(row=4, column=0, sticky='e', padx=10, pady=5)
entry_valor = tk.Entry(form_frame, font=entry_font, bg="white")
entry_valor.grid(row=4, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Status da Solicitação", bg="#f2f2f2", font=label_font).grid(row=5, column=0, sticky='e', padx=10, pady=5)
combo_status = ttk.Combobox(form_frame, font=entry_font, values=["pendente", "aprovada", "recusada"])
combo_status.grid(row=5, column=1, padx=10, pady=5)

btn_registrar = tk.Button(janela, text="Registrar Solicitação", command=registrar_solicitacao,
                          bg="#cc0000", fg="white", font=button_font, bd=0,
                          activebackground="#aa0000", activeforeground="white")
btn_registrar.pack(pady=20, ipadx=20)

janela.mainloop()
