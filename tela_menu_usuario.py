import tkinter as tk
from menus import MenuSistema

# Cores padrão do CuidaPet
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
COR_VERMELHO = "#E57373"

menu = MenuSistema()

def criar_tela_menu_usuario(root, email, mostrar_tela_callback):
    frame_menu = tk.Frame(root, bg=COR_FUNDO)

    # Barra lateral aumentada
    barra = tk.Frame(frame_menu, bg=COR_VERDE, width=160)
    barra.pack(side="left", fill="y")

    # Botões grandes para funcionalidade
    opcoes = [
    ("Animais em Adoção", lambda: mostrar_tela_callback("adocao")),
    ("Animais em Tratamento", lambda: mostrar_tela_callback("tratamento")),
    ("Meus Pedidos", lambda: mostrar_tela_callback("pedidos")),
    ("Denúncia", lambda: mostrar_tela_callback("denuncia")),
    ("Meu perfil", lambda: mostrar_tela_callback("perfil")),
    ("Sobre nós", lambda: mostrar_tela_callback("sobre")),
    ("Sair", lambda: root.destroy())
]

    for texto, acao in opcoes:
        cor_botao = COR_VERMELHO if texto == "Sair" else COR_VERDE
        tk.Button(
    barra,
    text=texto,
    font=("Arial", 12, "bold"),
    wraplength=120,          # Permite quebra de linha
    justify="center",        # Centraliza o texto dentro do botão
    bg=cor_botao,
    fg="black",
    width=16,
    height=4,                # Aumenta altura pra acomodar 2 linhas
    command=acao
).pack(pady=10)

    # Área central
    painel = tk.Frame(frame_menu, bg=COR_FUNDO)
    painel.pack(expand=True, fill="both")

    tk.Label(
        painel,
        text="O que você procura hoje?",
        font=("Helvetica", 22, "bold"),
        bg=COR_FUNDO
    ).pack(pady=60)

    return frame_menu