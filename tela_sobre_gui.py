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
    """Creates a 'Sobre' screen with buttons for navigating mission, contact, and returning to menu.
    Parameters:
        - root (tk.Tk or tk.Frame): The parent widget where this frame will be placed.
        - email (str): The email associated with the user session, used in mission and feedback.
        - voltar_callback (callable): Function to be called when the 'Voltar' button is clicked, usually to return to a previous menu.
    Returns:
        - tk.Frame: A frame containing the 'Sobre' interface for integration into the GUI.
    Processing Logic:
        - Configures buttons with specific text and dimensions.
        - Packs buttons with appropriate spacing in the frame.
        - Sets button commands using lambda functions to maintain user context and provide navigation."""
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
    """Display a mission statement and contact information in a GUI window.
    Parameters:
        - root (tk.Widget): The root widget where the GUI frame will be placed.
        - email (str): The contact email address, though not directly manipulated within this function.
        - voltar_callback (function): Callback function to handle the "Voltar" button action.
    Returns:
        - None
    Processing Logic:
        - Displays a text message about the project's mission in a Tkinter Frame.
        - Provides a "Voltar" button that triggers the 'voltar_callback' to navigate back to the menu."""
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
    """Open a feedback interface within a Tkinter application allowing users to send suggestions or questions.
    Parameters:
        - root (tk.Tk): The root window where the feedback frame will be placed.
        - email (str): The email address associated with the feedback submission.
        - voltar_callback (function): A callback function to navigate back to the previous menu.
    Returns:
        None
    Processing Logic:
        - A text area is provided for users to input their feedback.
        - The 'Confirmar' button sends the feedback if the text area contains text.
        - A message box informs the user whether the feedback sending was successful or warns if no text was entered.
        - The 'Voltar' button navigates the user back to a menu using the provided callback function."""
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Dúvidas? Sugestões? Envie um feedback!", font=("Helvetica", 14, "bold"), bg=COR_FUNDO).pack(pady=10)

    campo = tk.Text(container, width=50, height=6, font=("Arial", 12))
    campo.pack(pady=10)

    def enviar():
        """Send user feedback after validation.
        Parameters:
            - None
        Returns:
            - None
        Processing Logic:
            - Retrieves text input starting from position "1.0" to "end" and removes surrounding whitespace.
            - Validates that the text is not empty before proceeding with feedback submission.
            - Saves the feedback using the 'salvar_feedback' function with the user email and text.
            - Displays a success message on successful feedback submission.
            - Redirects the user back to the menu using 'voltar_callback'. If the text is empty, it shows a warning message."""
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