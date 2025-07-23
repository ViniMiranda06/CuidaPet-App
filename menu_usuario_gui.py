import tkinter as tk
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
COR_VERMELHO = "#E57373"

menu = MenuSistema()

def abrir_menu_usuario(email):
    """Create and display a user menu interface using Tkinter.
    Parameters:
        - email (str): The email of the user, used for specific action callbacks related to the user's profile.
    Returns:
        - None: This function does not return a value. It initializes and runs the Tkinter main loop to display the user menu.
    Processing Logic:
        - Sets up a Tkinter window with predefined size, title, and background color.
        - Configures a sidebar with options for viewing animals, requesting actions, editing the profile, and exiting.
        - Buttons in the sidebar call specific functions with actions linked to the user's email.
        - Arranges a central visual area in the window with a welcoming label."""
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