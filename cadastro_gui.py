import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema
from user import Usuario

# 🎨 Cores padrão do CuidaPet
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()

# 🧠 Função de cadastro com validações
def cadastrar_usuario(nome, email, senha, confirmar_senha, telefone, endereco):
    if not nome.strip():
        messagebox.showerror("Erro", "Nome não pode ser vazio!")
        return

    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    if len(senha) < 6:
        messagebox.showerror("Erro", "Senha deve ter pelo menos 6 caracteres.")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem.")
        return

    if not telefone.isdigit() or len(telefone) != 11:
        messagebox.showerror("Erro", "Telefone deve ter 11 dígitos numéricos.")
        return

    if menu.usuarios.buscar_usuario_por_email(email):
        messagebox.showerror("Erro", "Usuário já cadastrado!")
    else:
        novo_usuario = Usuario(nome, email, senha, telefone, endereco, "usuario")
        menu.usuarios.adicionar_usuario(novo_usuario)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        root.destroy()

# 🖼️ Interface gráfica
root = tk.Tk()
root.title("CuidaPet - Cadastro")
root.geometry("450x600")
root.configure(bg=COR_FUNDO)

# 🔲 Container centralizado
container = tk.Frame(root, bg=COR_FUNDO)
container.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(container, text="Cadastro", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

campos = {}

# 🧾 Campos de entrada
for label, chave, ocultar in [
    ("Nome", "nome", False),
    ("Email", "email", False),
    ("Senha", "senha", True),
    ("Confirme sua senha", "confirmar_senha", True),
    ("Telefone", "telefone", False),
    ("Endereço", "endereco", False)
]:
    tk.Label(container, text=label, font=("Arial", 12), bg=COR_FUNDO).pack()
    entry = tk.Entry(container, font=("Arial", 12), width=30, show="*" if ocultar else "")
    entry.pack(pady=5)
    campos[chave] = entry

# ✅ Botão de cadastro
tk.Button(
    container,
    text="Cadastre-se",
    bg=COR_VERDE,
    font=("Arial", 14),
    width=20,
    command=lambda: cadastrar_usuario(
        campos["nome"].get(),
        campos["email"].get(),
        campos["senha"].get(),
        campos["confirmar_senha"].get(),
        campos["telefone"].get(),
        campos["endereco"].get()
    )
).pack(pady=20)

# 🔙 Botão voltar
tk.Button(
    container,
    text="Voltar",
    font=("Arial", 12),
    bg="white",
    width=20,
    command=root.destroy
).pack()

root.mainloop()