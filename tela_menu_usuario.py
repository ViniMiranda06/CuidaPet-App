import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema
from PIL import Image, ImageTk

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
COR_VERMELHO = "#E57373"

menu = MenuSistema()

def criar_tela_menu_usuario(root, email, mostrar_tela_callback):
    """Cria uma interface de menu do usuário dentro de uma determinada janela raiz tkinter.
Parâmetros:
- raiz (tk.Tk): A janela pai tkinter onde o quadro do menu será anexado.
        - email (str): O e-mail do usuário, que pode ser usado para personalizar a interface.
- mostrar_tela_callback (função): Uma função de retorno de chamada que lida com a lógica de exibição para diferentes opções de tela dentro do menu.
Retorna:
- tk.Frame: Um widget tkinter Frame contendo o layout e a lógica completos do menu.
    Lógica de processamento:
- Constrói uma barra lateral com botões que representam diferentes opções, cada um conectado ao `mostrar_tela_callback`.
- Inclui uma caixa de diálogo de confirmação para o botão Sair para verificar a intenção do usuário antes de fechar o aplicativo.
- Tenta carregar e exibir uma imagem de logotipo; recorre a uma exibição de texto se o carregamento da imagem falhar."""
    frame_menu = tk.Frame(root, bg=COR_FUNDO)

    def confirmar_sair():
        if messagebox.askyesno("Confirmar saída", "Deseja realmente sair?"):
            root.destroy()

    # Barra lateral
    barra = tk.Frame(frame_menu, bg=COR_VERDE, width=160)
    barra.pack(side="left", fill="y")

    opcoes = [
        ("Animais em Adoção", lambda: mostrar_tela_callback("adocao")),
        ("Animais em Tratamento", lambda: mostrar_tela_callback("tratamento")),
        ("Meus Pedidos", lambda: mostrar_tela_callback("pedidos")),
        ("Denúncia", lambda: mostrar_tela_callback("denuncia")),
        ("Meu perfil", lambda: mostrar_tela_callback("perfil")),
        ("Sobre nós", lambda: mostrar_tela_callback("sobre")),
    ]

    for texto, acao in opcoes:
        btn = tk.Button(
            barra,
            text=texto,
            font=("Arial", 12, "bold"),
            wraplength=120,
            justify="center",
            bg=COR_VERDE,
            fg="black",
            width=16,
            height=4,
            command=acao
        )
        btn.pack(pady=10)

    tk.Button(
        barra,
        text="Sair",
        font=("Arial", 12, "bold"),
        wraplength=120,
        justify="center",
        bg=COR_VERMELHO,
        fg="black",
        width=16,
        height=4,
        command=confirmar_sair
    ).pack(pady=10)

    # Painel principal
    painel = tk.Frame(frame_menu, bg=COR_FUNDO)
    painel.pack(expand=True, fill="both")

    # Topo com frase + logo centralizada
    topo = tk.Frame(painel, bg=COR_FUNDO)
    topo.pack(pady=30)

    tk.Label(
        topo,
        text="O que você procura hoje?",
        font=("Helvetica", 22, "bold"),
        bg=COR_FUNDO
    ).pack(pady=(0, 20))

    try:
        imagem_logo = Image.open("logo.png").resize((300, 250))
        logo = ImageTk.PhotoImage(imagem_logo)
        logo_label = tk.Label(topo, image=logo, bg=COR_FUNDO)
        logo_label.pack()
        topo.logo_img = logo
    except:
        tk.Label(topo, text="🐾 CuidaPet", font=("Helvetica", 18), bg=COR_FUNDO).pack()

    return frame_menu