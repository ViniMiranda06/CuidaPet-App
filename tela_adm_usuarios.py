import tkinter as tk
import json
from tkinter import messagebox

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_USUARIOS = "usuarios.json"

def ler_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def salvar_usuarios(lista):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_adm_usuarios(root, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Usuários Cadastrados", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=15)

    lista = ler_usuarios()

    for usuario in lista:
        box = tk.Frame(container, bg=COR_FUNDO, bd=1, relief="solid")
        box.pack(pady=6)

        txt = f"{usuario['nome']} • {usuario['email']} • {usuario['tipo']}"
        tk.Label(box, text=txt, font=("Arial", 12), bg=COR_FUNDO).pack(side="left", padx=10)

        def excluir(email=usuario["email"], nome=usuario["nome"]):
            if messagebox.askyesno("Confirmação", f"Excluir usuário {nome}?"):
                nova = [u for u in lista if u["email"] != email]
                salvar_usuarios(nova)
                messagebox.showinfo("Excluído", f"{nome} foi removido.")
                voltar_callback("adm_usuarios")

        tk.Button(box, text="Excluir", font=("Arial", 10), bg=COR_MARROM, command=excluir).pack(side="right", padx=10)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("menu_admin")).pack(pady=20)

    return frame