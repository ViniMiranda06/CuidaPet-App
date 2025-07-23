import tkinter as tk
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
COR_VERMELHO = "#E57373"

menu = MenuSistema()

def abrir_menu_usuario(email):
    """Crie e exiba uma interface de menu do usuário usando Tkinter.
Parâmetros:
- e-mail (str): O e-mail do usuário, usado para chamadas de retorno de ações específicas relacionadas ao perfil do usuário.
Retorna:
- Nenhum: Esta função não retorna um valor. Ela inicializa e executa o loop principal do Tkinter para exibir o menu do usuário.
    Lógica de processamento:
- Configura uma janela Tkinter com tamanho, título e cor de fundo predefinidos.
- Configura uma barra lateral com opções para visualizar animais, solicitar ações, editar o perfil e sair.
- Os botões na barra lateral chamam funções específicas com ações vinculadas ao e-mail do usuário.
- Organiza uma área visual central na janela com uma etiqueta de boas-vindas."""
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
