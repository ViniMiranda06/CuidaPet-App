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
    """Saves a complaint to the database.
    Parameters:
        - email (str): The email address of the person filing the complaint.
        - nome (str): The name of the person filing the complaint.
        - tipo (str): The type of complaint being filed.
        - texto (str): The detailed text of the complaint.
    Returns:
        - None: This function does not return a value.
    Processing Logic:
        - Initializes the JSON file if it does not exist.
        - Determines the new ID for the complaint by finding the existing maximum ID and adding 1.
        - Adds the new complaint to the list of existing complaints and saves them to the file."""
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
    """Creates and displays a complaint submission interface within a given window.
    Parameters:
        - root (tk.Tk): The main window where the complaint submission interface will be placed.
        - email (str): The email address of the user, used to retrieve user data.
        - voltar_callback (callable): A function to execute when returning to the previous menu.
    Returns:
        - None: This function does not return a value; it configures the interface in the given window.
    Processing Logic:
        - The function configures a text input area for specifying complaints.
        - A complaint type is selected via radio buttons with preset options.
        - On form submission, it saves the complaint if the description is provided and displays a confirmation message.
        - Handles empty description cases with a warning message."""
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
        """Handles the submission and validation of a complaint form in a GUI application.
        Parameters:
            - campo_texto (Text widget): Source of the complaint description.
            - tipo_var (StringVar): Selected type of complaint from GUI.
            - email (str): Email used to identify the user.
            - buscar_dados_usuario (function): Function to retrieve user data given an email.
            - salvar_denuncia (function): Function to save complaint data.
            - messagebox (module): Interface for displaying messages to the user.
            - voltar_callback (function): Callback function to navigate back to the menu.
        Returns:
            - None: The function does not return a value. It updates the GUI state based on user input.
        Processing Logic:
            - Retrieves and trims the complaint description text to ensure it isn't empty.
            - Acquires user name through the provided email for proper complaint tracking.
            - Displays informational or warning messages based on the completeness of the input.
            - Saves the complaint only if the description is not empty."""
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
    """Displays a screen showing reports associated with a given email.
    Parameters:
        - root (Tkinter Frame): The root frame where the display should be placed.
        - email (str): The email address used to fetch reports.
        - voltar_callback (function): Callback function to be invoked when the user wants to navigate back.
    Returns:
        - None
    Processing Logic:
        - Uses the email parameter to fetch associated reports.
        - If reports exist, displays them; otherwise, informs the user that no reports are available.
        - Contains a button to return to the main menu using the provided callback."""
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
    """Create a report screen interface.
    Parameters:
        - root (tk.Tk): The root window where the interface will be attached.
        - email (str): The email address of the user, used for contextual operations.
        - voltar_callback (function): A callback function to execute when the 'Voltar' button is clicked.
    Returns:
        - tk.Frame: The frame containing the interface elements.
    Processing Logic:
        - Initializes a frame with specific background color and places it at the center of the root window.
        - Adds a label and three buttons to the interface, connecting them to appropriate command functions for different actions."""
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