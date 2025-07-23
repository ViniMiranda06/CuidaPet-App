import tkinter as tk
from tkinter import messagebox
import json
import os

# 🎨 Cores CuidaPet
COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_FEEDBACK = "feedbacks.json"

# 🔒 Garante que o arquivo existe
def inicializar_feedbacks():
    if not os.path.exists(ARQUIVO_FEEDBACK):
        with open(ARQUIVO_FEEDBACK, "w", encoding="utf-8") as f:
            json.dump([], f)

# 📥 Lê todos os feedbacks
def ler_feedbacks():
    inicializar_feedbacks()
    with open(ARQUIVO_FEEDBACK, "r", encoding="utf-8") as f:
        return json.load(f)

# 🗑️ Salva feedbacks atualizados
def salvar_feedbacks(lista):
    with open(ARQUIVO_FEEDBACK, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

# 🖼️ Tela principal
def criar_tela_adm_feedbacks(root, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Feedbacks Recebidos", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=15)

    lista = ler_feedbacks()

    if lista:
        for idx, feedback in enumerate(lista):
            box = tk.Frame(container, bg=COR_FUNDO, bd=1, relief="solid")
            box.pack(pady=6)

            texto = f"{feedback['email']} — {feedback['mensagem']}"
            tk.Label(box, text=texto, font=("Arial", 11), bg=COR_FUNDO,
                     wraplength=420, justify="left").pack(side="left", padx=10)

            def excluir(indice=idx, email=feedback["email"]):
                if messagebox.askyesno("Confirmação", f"Excluir feedback de {email}?"):
                    nova = lista[:indice] + lista[indice+1:]
                    salvar_feedbacks(nova)
                    messagebox.showinfo("Excluído", f"Feedback removido.")
                    voltar_callback("adm_feedbacks")

            tk.Button(box, text="Excluir", font=("Arial", 10), bg=COR_MARROM,
                      command=excluir).pack(side="right", padx=10)
    else:
        tk.Label(container, text="Nenhum feedback recebido ainda.", font=("Arial", 12), bg=COR_FUNDO).pack(pady=30)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("menu_admin")).pack(pady=20)

    return frame