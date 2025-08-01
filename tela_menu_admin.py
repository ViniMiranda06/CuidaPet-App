import tkinter as tk
from tkinter import messagebox  


# Paleta de cores CuidaPet Admin
COR_FUNDO = "#F4EDE3"    # Bege claro de fundo
COR_MARROM = "#BFA6A0"   # Marrom claro para botões

def criar_tela_menu_admin(root, email, mostrar_tela_callback):
    """Cria uma interface de menu de administração na janela raiz especificada.
Parâmetros:
- root (tk.Tk): A janela raiz onde a interface do menu será anexada.
- email (str): O endereço de e-mail do usuário administrador.
- mostrar_tela_callback (função): Uma função de retorno de chamada para exibir telas diferentes.
    Retorna:
- tk.Frame: Um quadro contêiner com a interface do menu de administração.
Lógica de processamento:
- Inicializa uma barra lateral com botões para diferentes funções de administração.
- Os botões são configurados com uma função de retorno de chamada para exibir telas de administração específicas.
- A cor do botão muda para vermelho para a opção “Sair”."""

    def confirmar_sair():
        if messagebox.askyesno("Confirmar saída", "Deseja realmente sair?"):
            root.destroy()


    frame_menu = tk.Frame(root, bg=COR_FUNDO)

    # Barra lateral de botões
    barra = tk.Frame(frame_menu, bg=COR_MARROM, width=160)
    barra.pack(side="left", fill="y")

    # Botões do menu (ainda não abrem telas, mas já visíveis)
    opcoes = [
    ("Animais em Adoção", lambda: mostrar_tela_callback("adm_adocao")),
    ("Animais em Tratamento", lambda: mostrar_tela_callback("adm_tratamento")),
    ("Usuários", lambda: mostrar_tela_callback("adm_usuarios")),
    ("Denúncias", lambda: mostrar_tela_callback("adm_denuncias")),
    ("Feedbacks", lambda: mostrar_tela_callback("adm_feedbacks")),
    ("Sair", confirmar_sair)
]


    for texto, acao in opcoes:
        cor_botao = "red" if texto == "Sair" else COR_MARROM
        tk.Button(barra, text=texto, font=("Arial", 12, "bold"), bg=cor_botao,
                fg="black", width=16, height=4, wraplength=150, command=acao).pack(pady=10)

    # Painel principal (parte central da tela)
    painel = tk.Frame(frame_menu, bg=COR_FUNDO)
    painel.pack(expand=True, fill="both")

    tk.Label(painel, text="Painel do Administrador", font=("Helvetica", 22, "bold"),
             bg=COR_FUNDO).pack(pady=60)

    return frame_menu