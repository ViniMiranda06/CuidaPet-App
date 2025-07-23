import tkinter as tk
from tkinter import messagebox
import json
import os

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_ADOCAO = "animais_adocao.json"

def salvar_animal(novo):
    if os.path.exists(ARQUIVO_ADOCAO):
        with open(ARQUIVO_ADOCAO, "r", encoding="utf-8") as f:
            lista = json.load(f)
    else:
        lista = []

    novo["id"] = max([a.get("id", 0) for a in lista] + [-1]) + 1
    lista.append(novo)

    with open(ARQUIVO_ADOCAO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_adicionar_animal(root, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Adicionar Animal em Adoção", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

    # Campos de entrada
    tk.Label(container, text="Nome:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_nome = tk.Entry(container, font=("Arial", 12), width=30)
    entry_nome.pack(pady=5)

    tk.Label(container, text="Espécie:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_especie = tk.Entry(container, font=("Arial", 12), width=30)
    entry_especie.pack(pady=5)

    tk.Label(container, text="Raça:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_raca = tk.Entry(container, font=("Arial", 12), width=30)
    entry_raca.pack(pady=5)

    tk.Label(container, text="Idade:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_idade = tk.Entry(container, font=("Arial", 12), width=30)
    entry_idade.pack(pady=5)

    def adicionar():
        nome = entry_nome.get().strip()
        especie = entry_especie.get().strip()
        raca = entry_raca.get().strip()
        idade = entry_idade.get().strip()

        if not nome or not especie or not raca or not idade:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        novo = {
            "nome": nome,
            "especie": especie,
            "raca": raca,
            "idade": idade
        }
        salvar_animal(novo)
        messagebox.showinfo("Sucesso", "Animal adicionado com sucesso!")
        voltar_callback("adm_adocao")

    tk.Button(container, text="Salvar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=adicionar).pack(pady=15)

    tk.Button(container, text="Cancelar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("adm_adocao")).pack(pady=5)

    return frame