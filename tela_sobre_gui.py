import tkinter as tk
from tkinter import messagebox
import json
import os

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
ARQUIVO_FEEDBACK = "feedbacks.json"

# 🔒 Garante que o arquivo existe
def inicializar_feedbacks():
    if not os.path.exists(ARQUIVO_FEEDBACK):
        with open(ARQUIVO_FEEDBACK, "w", encoding="utf-8") as f:
            json.dump([], f)

# 💾 Salva feedback
def salvar_feedback(email, texto):
    inicializar_feedbacks()
    with open(ARQUIVO_FEEDBACK, "r", encoding="utf-8") as f:
        lista = json.load(f)
    lista.append({"email": email, "mensagem": texto})
    with open(ARQUIVO_FEEDBACK, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

# 🖼️ Tela principal de "Sobre nós"
def criar_tela_sobre(root, email, voltar_callback):
    """Cria uma tela “Sobre” com botões para navegar pela missão, contato e retornar ao menu.
    Parâmetros:
- root (tk.Tk ou tk.Frame): O widget pai onde este quadro será colocado.
- email (str): O e-mail associado à sessão do usuário, usado na missão e no feedback.
- voltar_callback (callable): Função a ser chamada quando o botão “Voltar” for clicado, geralmente para retornar a um menu anterior.
    Retorna:
- tk.Frame: Um quadro contendo a interface “Sobre” para integração na GUI.
Lógica de processamento:
- Configura botões com texto e dimensões específicos.
- Empacota botões com espaçamento apropriado no quadro.
- Define comandos de botão usando funções lambda para manter o contexto do usuário e fornecer navegação."""
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    # Botão: Missão
    tk.Button(container, text="Conheça nossa missão", font=("Arial", 14), bg=COR_VERDE,
              width=22, height=2,
              command=lambda: abrir_missao(root, email, voltar_callback)).pack(pady=10)

    # Botão: Fale conosco
    tk.Button(container, text="Fale conosco", font=("Arial", 14), bg=COR_VERDE,
              width=22, height=2,
              command=lambda: abrir_feedback(root, email, voltar_callback)).pack(pady=10)

    # Botão: Voltar
    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2,
              command=lambda: voltar_callback("menu")).pack(pady=30)

    return frame

# 📄 Tela com texto da missão
def abrir_missao(root, email, voltar_callback):
    """Exibe uma declaração de missão e informações de contato em uma janela GUI.
Parâmetros:
- root (tk.Widget): O widget raiz onde o quadro GUI será colocado.
- email (str): O endereço de e-mail de contato, embora não seja manipulado diretamente dentro desta função.
- voltar_callback (função): Função de retorno de chamada para lidar com a ação do botão “Voltar”.
    Retorna:
- Nenhum
Lógica de processamento:
- Exibe uma mensagem de texto sobre a missão do projeto em um quadro Tkinter.
- Fornece um botão “Voltar” que aciona o ‘voltar_callback’ para navegar de volta ao menu."""
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    texto = (
    "Prazer! Nós somos Igor e Vinicius, criadores e desenvolvedores do CuidaPet. Nossa parceria surgiu de uma forma inusitada, "
    "mas muito positiva para ambos. Somos estudantes da Universidade Federal Rural de Pernambuco (UFRPE), e junto com o professor "
    "orientador Cleyton Vanut, foi possível criar e tirar essa ideia do papel.\n\n"
    "A nossa inspiração para dar vida a este projeto nasceu da vontade de oferecer voz e cuidado aos animais que infelizmente não têm "
    "o direito de serem apenas animais.\n\n"
    "O nosso sistema foi desenvolvido de forma leve e intuitiva. Esperamos que você tenha curtido! Qualquer coisa, é só mandar um e-mail "
    "pra gente — vamos trocar uma ideia!\n\n"
    "\"A grandeza de uma nação pode ser julgada pelo modo que seus animais são tratados.\" — Mahatma Gandhi\n\n"
    "Para falar com Igor: igordv2k19@gmail.com\n"
    "Para falar com Vinicius: viniolimi2806@gmail.com"
)

    tk.Label(container, text=texto, font=("Arial", 12), wraplength=430, justify="left", bg=COR_FUNDO).pack(pady=20)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=10)

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

# 📣 Tela de envio de feedback
def abrir_feedback(root, email, voltar_callback):
    """Abre uma interface de feedback dentro de um aplicativo Tkinter, permitindo que os usuários enviem sugestões ou perguntas.
Parâmetros:
- root (tk.Tk): A janela raiz onde o quadro de feedback será colocado.
- email (str): O endereço de e-mail associado ao envio do feedback.
- voltar_callback (função): Uma função de retorno de chamada para navegar de volta ao menu anterior.
    Retorna:
Nenhum
Lógica de processamento:
- Uma área de texto é fornecida para os usuários inserirem seus comentários.
        - O botão “Confirmar” envia o feedback se a área de texto contiver texto.
- Uma caixa de mensagem informa ao usuário se o envio do feedback foi bem-sucedido ou avisa se nenhum texto foi inserido.
- O botão “Voltar” navega o usuário de volta para um menu usando a função de retorno fornecida."""
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Dúvidas? Sugestões? Envie um feedback!", font=("Helvetica", 14, "bold"), bg=COR_FUNDO).pack(pady=10)

    campo = tk.Text(container, width=50, height=6, font=("Arial", 12))
    campo.pack(pady=10)

    def enviar():
        """Envia o feedback do usuário após a validação.
Parâmetros:
- Nenhum
Retorna:
- Nenhum
Lógica de processamento:
- Recupera a entrada de texto a partir da posição “1.0” até o “fim” e remove os espaços em branco ao redor.
- Valida se o texto não está vazio antes de prosseguir com o envio do feedback.
            - Salva o feedback usando a função “salvar_feedback” com o e-mail e o texto do usuário.
- Exibe uma mensagem de sucesso quando o envio do feedback é bem-sucedido.
- Redireciona o usuário de volta ao menu usando “voltar_callback”. Se o texto estiver vazio, exibe uma mensagem de aviso."""
        texto = campo.get("1.0", "end").strip()
        if texto:
            salvar_feedback(email, texto)
            messagebox.showinfo("Enviado", "Seu feedback foi enviado com sucesso.")
            voltar_callback("menu")
        else:
            messagebox.showwarning("Aviso", "Escreva algo antes de confirmar.")

    tk.Button(container, text="Confirmar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=enviar).pack(pady=10)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=10)

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()
