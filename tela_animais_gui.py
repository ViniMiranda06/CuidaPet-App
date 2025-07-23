import tkinter as tk
from tkinter import messagebox
from menus import MenuSistema
from pedido import Pedido

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()

def criar_tela_animais(root, tipo, email, mostrar_tela_callback):
    """Cria um quadro exibindo opções de adoção ou tratamento de animais.
Parâmetros:
- raiz (tk.Tk ou tk.Widget): O widget ou janela raiz onde o quadro será adicionado.
        - tipo (str): Tipo de operação a ser realizada, “adocão” para adoção ou outro valor para animais em tratamento.
- email (str): O endereço de e-mail do usuário, usado para criar uma solicitação de adoção ou tratamento de um animal.
- mostrar_tela_callback (callable): Uma função de retorno de chamada a ser invocada ao navegar de volta para outra tela.
    Retorna:
- tk.Frame: Um quadro contendo informações sobre o animal e opções para solicitar ações.
Lógica de processamento:
- Cria cartões para cada animal e os exibe no quadro.
- Os botões nos cartões permitem que os usuários solicitem animais, acionando caixas de mensagem em caso de sucesso ou falha da solicitação.
- Um título é exibido com base no tipo de operação (“adocão” ou tratamento)."""
    frame_animais = tk.Frame(root, bg=COR_FUNDO)

    # Título
    titulo = "Animais para Adoção" if tipo == "adocao" else "Animais em Tratamento"
    tk.Label(frame_animais, text=titulo, font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

    # Painel com cards
    painel = tk.Frame(frame_animais, bg=COR_FUNDO)
    painel.pack(expand=True)

    lista = menu.animais.listar_animais(tipo)

    for animal in lista:
        card = tk.Frame(painel, bg=COR_VERDE, padx=10, pady=10)
        card.pack(pady=10, fill="x", padx=50)

        info = f"{animal['nome'].title()} • {animal['especie'].title()} • {animal['idade']}"
        tk.Label(card, text=info, font=("Arial", 12), bg=COR_VERDE).pack(anchor="w")

        def solicitar_animal(animal_id=animal["id"], tipo=tipo, email=email):
            novo_pedido = Pedido(email, animal_id, tipo)
            sucesso = menu.pedidos.adicionar_pedido(novo_pedido)
            if sucesso:
                messagebox.showinfo("Solicitação", "Animal solicitado com sucesso!")
            else:
                messagebox.showerror("Solicitação", "Este animal já foi solicitado.")

        tk.Button(
            card,
            text="Solicitar",
            font=("Arial", 12, "bold"),
            bg="#FFD966",
            command=solicitar_animal
        ).pack(pady=5)

    # Botão de voltar
    tk.Button(frame_animais, text="Voltar", font=("Arial", 12), bg=COR_VERDE, command=lambda: mostrar_tela_callback("menu")).pack(pady=20)

    return frame_animais