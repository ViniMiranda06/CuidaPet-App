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
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Dúvidas? Sugestões? Envie um feedback!", font=("Helvetica", 14, "bold"), bg=COR_FUNDO).pack(pady=10)

    campo = tk.Text(container, width=50, height=6, font=("Arial", 12))
    campo.pack(pady=10)

    def enviar():
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