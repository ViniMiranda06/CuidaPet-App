import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
FONTE_PADRAO = ("Arial", 12)

menu = MenuSistema()

def alternar_visibilidade_senha():
    if entry_senha.cget('show') == '*':
        entry_senha.config(show='')
        btn_mostrar_senha.config(text='🙈 Ocultar')
    else:
        entry_senha.config(show='*')
        btn_mostrar_senha.config(text='👁 Mostrar')

# Janela principal
root = tk.Tk()
root.title("CuidaPet - Login")
root.geometry("400x300")
root.configure(bg=COR_FUNDO)

# Layout
tk.Label(root, text="Login", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=20)

tk.Label(root, text="Email:", font=FONTE_PADRAO, bg=COR_FUNDO).pack()
entry_email = tk.Entry(root, font=FONTE_PADRAO, width=30)
entry_email.pack(pady=5)

tk.Label(root, text="Senha:", font=FONTE_PADRAO, bg=COR_FUNDO).pack()

frame_senha = tk.Frame(root, bg=COR_FUNDO)
frame_senha.pack()

entry_senha = tk.Entry(frame_senha, font=FONTE_PADRAO, width=22, show="*")
entry_senha.pack(side="left", pady=5)

btn_mostrar_senha = tk.Button(
    frame_senha,
    text="👁 Mostrar",
    font=("Arial", 10),
    bg="#DDDDDD",
    fg="black",
    relief="raised",
    bd=1,
    padx=5,
    command=alternar_visibilidade_senha
)
btn_mostrar_senha.pack(side="left", padx=5)

def autenticar():
    """Autentica um usuário com base no e-mail e senha fornecidos.
    Parâmetros:
        - Nenhum
    Retorna:
        - Nenhum
    Lógica de processamento:
        - Recupera o e-mail e a senha dos campos de entrada.
        - Chama autenticar_usuario para verificar as credenciais.
        - Se a autenticação for bem-sucedida, exibe uma mensagem de boas-vindas e navega até o menu do usuário.
        - Exibe uma mensagem de erro se a autenticação falhar."""
    email = entry_email.get()
    senha = entry_senha.get()
    usuario = menu.usuarios.autenticar_usuario(email, senha)
    if usuario:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario['nome']}!")
        root.destroy()
        menu.menu_usuario(email)
    else:
        messagebox.showerror("Erro", "Credenciais inválidas.")

tk.Button(root, text="Entrar", bg=COR_VERDE, font=("Arial", 14), command=autenticar).pack(pady=20)

root.mainloop()
