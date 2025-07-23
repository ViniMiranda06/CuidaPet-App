import tkinter as tk
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
COR_VERMELHO = "#E57373"

menu = MenuSistema()

def abrir_menu_usuario(email):
    root = tk.Tk()
    root.title("CuidaPet - Menu Principal")
    root.geometry("700x500")
    root.configure(bg=COR_FUNDO)

    # 🧱 Barra lateral
    barra = tk.Frame(root, bg=COR_VERDE, width=120)
    barra.pack(side="left", fill="y")

    opcoes = [
        ("Animais em Adoção", lambda: menu.exibir_animais("adocao")),
        ("Animais em Tratamento", lambda: menu.exibir_animais("tratamento")),
        ("Solicitar Adoção", lambda: menu.adicionar_pedido(email, "adocao")),
        ("Solicitar Tratamento", lambda: menu.adicionar_pedido(email, "tratamento")),
        ("Perfil", lambda: menu.menu_editar_perfil(email)),
        ("Sair", root.destroy)
    ]

    for texto, acao in opcoes:
        cor = COR_VERMELHO if texto == "Sair" else COR_VERDE
        tk.Button(barra, text=texto, font=("Arial", 10), bg=cor, fg="black", width=18, height=2, command=acao).pack(pady=8)

    # 🖼️ Área central
    painel = tk.Frame(root, bg=COR_FUNDO)
    painel.pack(expand=True, fill="both")

    tk.Label(painel, text="O que você procura hoje?", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=40)

    root.mainloop()