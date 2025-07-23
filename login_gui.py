import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()

def autenticar(email, senha):
    usuario = menu.usuarios.autenticar_usuario(email, senha)
    if usuario:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario['nome']}!")
        root.destroy()
        menu.menu_usuario(email)  # Você pode trocar depois para abrir GUI do usuário
    else:
        messagebox.showerror("Erro", "Credenciais inválidas.")

root = tk.Tk()
root.title("CuidaPet - Login")
root.geometry("450x400")
root.configure(bg=COR_FUNDO)

tk.Label(root, text="Login", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=30)

tk.Label(root, text="Email", font=("Arial", 12), bg=COR_FUNDO).pack()
entry_email = tk.Entry(root, font=("Arial", 12), width=30)
entry_email.pack(pady=5)

tk.Label(root, text="Senha", font=("Arial", 12), bg=COR_FUNDO).pack()
entry_senha = tk.Entry(root, font=("Arial", 12), width=30, show="*")
entry_senha.pack(pady=5)

tk.Button(
    root,
    text="Entrar",
    bg=COR_VERDE,
    font=("Arial", 14),
    command=lambda: autenticar(entry_email.get(), entry_senha.get())
).pack(pady=20)

root.mainloop()