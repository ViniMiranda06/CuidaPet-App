import tkinter as tk
from tkinter import messagebox
import json
import os

# Cores CuidaPet
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
CAMINHO_DB = "usuarios.json"

# 🧾 Localiza dados do usuário
def buscar_dados_usuario(email):
    if not os.path.exists(CAMINHO_DB):
        return None
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        lista = json.load(f)
    for u in lista:
        if u["email"] == email:
            return u
    return None

# ✏️ Atualiza dados no arquivo
def atualizar_dados_usuario(email, novos_dados):
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        lista = json.load(f)
    for u in lista:
        if u["email"] == email:
            u.update(novos_dados)
            break
    with open(CAMINHO_DB, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

# 🗑️ Exclui usuário do sistema
def excluir_usuario(email):
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        lista = json.load(f)
    lista = [u for u in lista if u["email"] != email]
    with open(CAMINHO_DB, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

# 🖼️ Tela principal de perfil
def criar_tela_perfil(root, email, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza verticalmente e horizontalmente

    tk.Label(container, text="Meu Perfil", font=("Helvetica", 22, "bold"), bg=COR_FUNDO).pack(pady=20)

    tk.Button(container, text="Ver meus dados", font=("Arial", 14), bg=COR_VERDE,
              width=22, height=2, command=lambda: abrir_tela_dados(root, email, voltar_callback)).pack(pady=12)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=10)

    return frame

# 🗂️ Tela de visualização de dados
def abrir_tela_dados(root, email, voltar_callback):
    dados = buscar_dados_usuario(email)
    frame = tk.Frame(root, bg=COR_FUNDO)

    # Container central para alinhamento
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza na tela

    tk.Label(container, text="Seus dados", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=15)

    if dados:
        for campo in ["nome", "email", "telefone", "endereco"]:
            texto = f"{campo.capitalize()}: {dados.get(campo, '')}"
            tk.Label(container, text=texto, font=("Arial", 12), bg=COR_FUNDO).pack(pady=3)

        # Botões abaixo dos dados
        tk.Button(container, text="Alterar meus dados", font=("Arial", 12), bg=COR_VERDE,
                  width=22, height=2, command=lambda: abrir_tela_edicao(root, email, voltar_callback)).pack(pady=10)

        def confirmar_exclusao():
            if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir sua conta?"):
                excluir_usuario(email)
                messagebox.showinfo("Excluído", "Sua conta foi removida.")
                root.destroy()

        tk.Button(container, text="Excluir minha conta", font=("Arial", 12), bg=COR_VERDE,
                  width=22, height=2, command=confirmar_exclusao).pack(pady=10)

    else:
        tk.Label(container, text="Não foi possível localizar seus dados.", font=("Arial", 12), bg=COR_FUNDO).pack(pady=30)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=20)

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

# ✏️ Tela de edição de dados
def abrir_tela_edicao(root, email, voltar_callback):
    dados = buscar_dados_usuario(email)
    frame = tk.Frame(root, bg=COR_FUNDO)

    tk.Label(frame, text="Altere seus dados", font=("Helvetica", 16, "bold"), bg=COR_FUNDO).pack(pady=10)

    campos = {}
    for campo in ["nome", "telefone", "endereco", "senha"]:
        tk.Label(frame, text=campo.capitalize(), font=("Arial", 12), bg=COR_FUNDO).pack()
        entrada = tk.Entry(frame, font=("Arial", 12), width=30)
        entrada.insert(0, dados.get(campo, ""))
        entrada.pack(pady=5)
        campos[campo] = entrada

    def confirmar():
        novos_dados = {campo: entrada.get() for campo, entrada in campos.items()}
        atualizar_dados_usuario(email, novos_dados)
        messagebox.showinfo("Atualizado", "Seus dados foram atualizados.")
        voltar_callback("menu")

    tk.Button(frame, text="Confirmar", font=("Arial", 12), bg=COR_VERDE, command=confirmar).pack(pady=15)
    tk.Button(frame, text="Voltar", font=("Arial", 12), bg=COR_VERDE, command=lambda: voltar_callback("menu")).pack()

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()