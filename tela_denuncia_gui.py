import tkinter as tk
from tkinter import messagebox
import json
import os
from tela_perfil_gui import buscar_dados_usuario

# 🎨 Cores padrão CuidaPet
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"
CAMINHO_DB = "denuncias.json"

# 🔧 Garante que o arquivo existe
def inicializar_arquivo():
    if not os.path.exists(CAMINHO_DB):
        with open(CAMINHO_DB, "w", encoding="utf-8") as f:
            json.dump([], f)

# 📥 Função para salvar denúncia
def salvar_denuncia(email, nome, tipo, texto):
    inicializar_arquivo()
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        denuncias = json.load(f)

    novo_id = max([d.get("id", 0) for d in denuncias], default=-1) + 1

    nova_denuncia = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "tipo": tipo,
        "descricao": texto
    }

    denuncias.append(nova_denuncia)
    with open(CAMINHO_DB, "w", encoding="utf-8") as f:
        json.dump(denuncias, f, indent=2, ensure_ascii=False)

# 🔍 Busca todas as denúncias do usuário
def buscar_denuncia(email):
    inicializar_arquivo()
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        denuncias = json.load(f)
    return [d for d in denuncias if d.get("email") == email]

# 📝 Tela de escrever denúncia
def abrir_tela_escrever(root, email, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)

    tk.Label(frame, text="Escreva sua denúncia abaixo:", font=("Arial", 14), bg=COR_FUNDO).pack(pady=10)

    # 🔘 Tipo da denúncia
    tk.Label(frame, text="Tipo da denúncia:", font=("Helvetica", 14, "bold"), bg=COR_FUNDO).pack(pady=(10, 5))
    tipo_var = tk.StringVar(value="Negligência")

    frame_radios = tk.Frame(frame, bg=COR_FUNDO)
    frame_radios.pack(pady=5)

    TIPOS = ["Negligência", "Maus-tratos", "Abandono", "Exploração"]
    for tipo in TIPOS:
        tk.Radiobutton(
            frame_radios,
            text=tipo,
            variable=tipo_var,
            value=tipo,
            font=("Arial", 12),
            bg=COR_FUNDO,
            anchor="w",
            width=20,
            justify="left"
        ).pack(anchor="w", padx=20, pady=2)

    # 📝 Campo de texto
    campo_texto = tk.Text(frame, width=45, height=10, font=("Arial", 12))
    campo_texto.pack(pady=20)

    # 🚀 Função de envio
    def enviar():
        descricao = campo_texto.get("1.0", "end").strip()
        tipo = tipo_var.get()
        nome = buscar_dados_usuario(email)["nome"]

        if descricao:
            salvar_denuncia(email, nome, tipo, descricao)
            messagebox.showinfo("Enviado", "Denúncia enviada com sucesso.")
            voltar_callback("menu")
        else:
            messagebox.showwarning("Aviso", "Por favor, descreva o ocorrido.")

    # 🟩 Botões com tamanho maior
    tk.Button(frame, text="Enviar denúncia", font=("Arial", 14), bg=COR_VERDE,
              width=22, height=2, command=enviar).pack(pady=10)

    tk.Button(frame, text="Voltar", font=("Arial", 14), bg=COR_VERDE,
              width=22, height=2, command=lambda: voltar_callback("menu")).pack(pady=10)

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

# 📖 Tela de visualizar denúncias
def abrir_tela_ver(root, email, voltar_callback):
    relatos = buscar_denuncia(email)
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    if relatos:
        tk.Label(container, text="Suas denúncias:", font=("Helvetica", 16, "bold"), bg=COR_FUNDO).pack(pady=10)
        for d in relatos:
            txt = f"Tipo: {d['tipo']}\nDescrição: {d['descricao']}"
            tk.Label(container, text=txt, font=("Arial", 11), bg=COR_FUNDO, wraplength=400, justify="left").pack(pady=10)
    else:
        tk.Label(container, text="Você ainda não realizou nenhuma denúncia.", font=("Arial", 12), bg=COR_FUNDO).pack(pady=30)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=20)

    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

# 🧾 Tela principal de denúncias
def criar_tela_denuncia(root, email, voltar_callback):
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Realizar Denúncia", font=("Helvetica", 22, "bold"), bg=COR_FUNDO).pack(pady=20)

    tk.Button(container, text="Escrever denúncia", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3, command=lambda: abrir_tela_escrever(root, email, voltar_callback)).pack(pady=12)

    tk.Button(container, text="Ver minhas denúncias", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3, command=lambda: abrir_tela_ver(root, email, voltar_callback)).pack(pady=12)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=30)

    return frame