import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()

def cadastrar_usuario(nome, email, senha, telefone, endereco):
    if menu.usuarios.buscar_usuario_por_email(email):
        messagebox.showerror("Erro", "Usuário já cadastrado!")
    else:
        novo_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "telefone": telefone,
            "endereco": endereco,
            "tipo": "usuario"
        }
        menu.usuarios.adicionar_usuario(novo_usuario)
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        root.destroy()

root = tk.Tk()
root.title("CuidaPet - Cadastro")
root.geometry("450x500")
root.configure(bg=COR_FUNDO)

tk.Label(root, text="Cadastro", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=20)

campos = {}
for label_text in ["Nome", "Email", "Senha", "Telefone", "Endereço"]:
    tk.Label(root, text=label_text, font=("Arial", 12), bg=COR_FUNDO).pack()
    entry = tk.Entry(root, font=("Arial", 12), width=30, show="*" if label_text == "Senha" else None)
    entry.pack(pady=5)
    campos[label_text.lower()] = entry

tk.Button(
    root,
    text="Cadastre-se",
    bg=COR_VERDE,
    font=("Arial", 14),
    command=lambda: cadastrar_usuario(
        campos["nome"].get(),
        campos["email"].get(),
        campos["senha"].get(),
        campos["telefone"].get(),
        campos["endereço"].get()
    )
).pack(pady=20)

root.mainloop()