import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def cadastrar_imovel():
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    rua = entry_rua.get().strip()
    cep = entry_cep.get().strip()
    numero = entry_numero.get().strip()
    valor = entry_valor.get().strip()
    tipo = tipo_var.get()

    if estado and cidade and rua and cep and numero and valor and tipo:
        try:
            valor = float(valor)
            conn = conectar()
            cursor = conn.cursor()

            apartamento = tipo == "apartamento"
            casa = tipo == "casa"
            chale = tipo == "chale"
            hotel = tipo == "hotel"
            pousada = tipo == "pousada"

            cursor.execute("""
                INSERT INTO imovel (
                    im_estado, im_cidade, im_rua, im_cep, im_numero, im_valor_aluguel,
                    im_apartamento, im_casa, im_chale, im_hotel, im_pousada
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (estado, cidade, rua, cep, numero, valor, apartamento, casa, chale, hotel, pousada))

            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Imóvel cadastrado com sucesso!")
            limpar_campos()
            carregar_imoveis()
        except ValueError:
            messagebox.showerror("Erro", "Valor do aluguel deve ser numérico.")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")

def limpar_campos():
    entry_estado.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_cep.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    tipo_var.set("")

def carregar_imoveis():
    listbox_imoveis.delete(0, tk.END)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_imovel, im_estado, im_cidade, im_rua, im_numero, im_valor_aluguel
            FROM imovel
        """)
        imoveis = cursor.fetchall()
        conn.close()
        for imovel in imoveis:
            linha = f"ID {imovel[0]} - {imovel[1]} - {imovel[2]}, {imovel[3]}, Nº {imovel[4]} | R$ {imovel[5]:.2f}"
            listbox_imoveis.insert(tk.END, linha)
    except Exception as e:
        listbox_imoveis.insert(tk.END, f"Erro ao carregar imóveis: {e}")

def excluir_imovel():
    selecao = listbox_imoveis.curselection()
    if not selecao:
        messagebox.showwarning("Atenção", "Selecione um imóvel para excluir.")
        return

    item_texto = listbox_imoveis.get(selecao[0])
    try:
        id_imovel = int(item_texto.split(" ")[1])
        confirmacao = messagebox.askyesno("Confirmação", f"Deseja realmente excluir o imóvel ID {id_imovel}?")
        if confirmacao:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM imovel WHERE id_imovel = %s", (id_imovel,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", f"Imóvel ID {id_imovel} excluído com sucesso.")
            carregar_imoveis()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir imóvel: {e}")

# GUI
janela = tk.Tk()
janela.title("Cadastro de Imóveis")
janela.geometry("500x650")
janela.configure(bg='white')

top_frame = tk.Frame(janela, bg="#cc0000", height=50)
top_frame.pack(fill='x')

titulo = tk.Label(top_frame, text="Cadastro de Imóveis", bg="#cc0000", fg="white", font=("Calibri", 16))
titulo.place(relx=0.5, rely=0.5, anchor='center')  # centraliza o texto no topo


form = tk.Frame(janela, bg="white")
form.pack(pady=10)

def criar_label_entry(texto, row):
    tk.Label(form, text=texto, bg="white", font=("Arial", 12)).grid(row=row, column=0, sticky='e', padx=10, pady=5)
    entry = tk.Entry(form, font=("Arial", 12), bg="#f0f0f0")
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

entry_estado = criar_label_entry("Estado", 0)
entry_cidade = criar_label_entry("Cidade", 1)
entry_rua = criar_label_entry("Rua", 2)
entry_cep = criar_label_entry("CEP", 3)
entry_numero = criar_label_entry("Número", 4)
entry_valor = criar_label_entry("Valor Aluguel (R$)", 5)

tk.Label(form, text="Tipo de Imóvel", bg="white", font=("Arial", 12)).grid(row=6, column=0, sticky='e', padx=10, pady=5)
tipo_var = tk.StringVar()
tipos = [("Apartamento", "apartamento"), ("Casa", "casa"), ("Chalé", "chale"), ("Hotel", "hotel"), ("Pousada", "pousada")]
tipo_frame = tk.Frame(form, bg="white")
tipo_frame.grid(row=6, column=1, padx=10, pady=5, sticky='w')

for texto, valor in tipos:
    tk.Radiobutton(tipo_frame, text=texto, variable=tipo_var, value=valor, bg="white", font=("Arial", 11)).pack(anchor='w')

tk.Button(janela, text="Cadastrar Imóvel", command=cadastrar_imovel, bg="#cc0000", fg="white",
          font=("Arial", 12, "bold"), activebackground="#990000", activeforeground="white").pack(pady=10, ipadx=20)

tk.Label(janela, text="Imóveis Cadastrados", bg="white", font=("Arial", 12, "bold")).pack()
listbox_imoveis = tk.Listbox(janela, width=70, height=10, font=("Arial", 10))
listbox_imoveis.pack(padx=10, pady=10)

tk.Button(janela, text="Atualizar Lista", command=carregar_imoveis, bg="#cc0000", fg="white",
          font=("Arial", 11, "bold"), activebackground="#990000", activeforeground="white").pack(pady=5)

tk.Button(janela, text="Excluir Selecionado", command=excluir_imovel, bg="#cc0000", fg="white",
          font=("Arial", 11, "bold"), activebackground="#990000", activeforeground="white").pack(pady=5)

carregar_imoveis()
janela.mainloop()
