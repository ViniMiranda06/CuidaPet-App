import tkinter as tk
from tkinter import messagebox
import json
import os
from tela_perfil_gui import buscar_dados_usuario
from datetime import datetime  # Para registrar data/hora
from tela_contato_autoridades import abrir_tela_contato_autoridades

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
    # 1. Carrega denúncias existentes ou cria lista vazia
    """Salve um relatório com os detalhes do usuário fornecidos em um arquivo JSON.
    Parâmetros:
        - e-mail (str): endereço de e-mail da pessoa que envia o relatório.
        - nome (str): Nome da pessoa que envia o relatório.
        - tipo (str): Tipo ou categoria do relatório.
        - texto (str): Descrição textual do relatório.
    Retornos:
        -None: Esta função não retorna um valor.
    Lógica de processamento:
        - Carrega relatórios existentes de 'denuncias.json' ou inicializa uma nova lista se o arquivo não existir ou estiver corrompido.
        - Cria uma nova entrada de relatório com um ID incremental e timestamp atual.
        - Anexa o novo relatório à lista existente e salva-lo de volta para 'denuncias.json'."""
    try:
        with open("denuncias.json", "r", encoding="utf-8") as f:
            denuncias = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        denuncias = []
    
    # 2. Cria nova denúncia com ID sequencial
    nova_denuncia = {
        "id": len(denuncias),  # ID simples baseado na posição
        "nome": nome,
        "email": email,
        "tipo": tipo,
        "descricao": texto,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "status": "Recebida"
    }
    
    # 3. Adiciona e salva
    denuncias.append(nova_denuncia)
    with open("denuncias.json", "w", encoding="utf-8") as f:
        json.dump(denuncias, f, indent=2, ensure_ascii=False)

def listar_denuncias_usuario(email):
    try:
        with open("denuncias.json", "r", encoding="utf-8") as f:
            denuncias = json.load(f)
            return [d for d in denuncias if d["email"] == email]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 🔍 Busca todas as denúncias do usuário
def buscar_denuncia(email):
    inicializar_arquivo()
    with open(CAMINHO_DB, "r", encoding="utf-8") as f:
        denuncias = json.load(f)
    return [d for d in denuncias if d.get("email") == email]

# 📝 Tela de escrever denúncia
def abrir_tela_escrever(root, email, voltar_callback):
    """Cria e exibe uma interface de envio de reclamações dentro de uma determinada janela.
Parâmetros:
- root (tk.Tk): A janela principal onde a interface de envio de reclamações será colocada.
- email (str): O endereço de e-mail do usuário, usado para recuperar os dados do usuário.
- voltar_callback (callable): Uma função a ser executada ao retornar ao menu anterior.
    Retorna:
- Nenhum: Esta função não retorna um valor; ela configura a interface na janela especificada.
    Lógica de processamento:
- A função configura uma área de entrada de texto para especificar reclamações.
- Um tipo de reclamação é selecionado por meio de botões de opção com opções predefinidas.
- Ao enviar o formulário, ele salva a reclamação se a descrição for fornecida e exibe uma mensagem de confirmação.
- Lida com casos de descrição vazia com uma mensagem de aviso."""
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
        """Lida com o envio e a validação de um formulário de reclamação em um aplicativo GUI.
Parâmetros:
- campo_texto (widget de texto): fonte da descrição da reclamação.
- tipo_var (StringVar): tipo de reclamação selecionado na GUI.
- email (str): e-mail usado para identificar o usuário.
            - buscar_dados_usuario (função): Função para recuperar os dados do usuário a partir de um e-mail.
- salvar_denuncia (função): Função para salvar os dados da reclamação.
- messagebox (módulo): Interface para exibir mensagens ao usuário.
- voltar_callback (função): Função de retorno de chamada para navegar de volta ao menu.
        Retorna:
- Nenhum: A função não retorna um valor. Ela atualiza o estado da GUI com base na entrada do usuário.
Lógica de processamento:
- Recupera e corta o texto da descrição da reclamação para garantir que não esteja vazio.
            - Adquire o nome do usuário através do e-mail fornecido para o rastreamento adequado da reclamação.
- Exibe mensagens informativas ou de aviso com base na completude da entrada.
- Salva a reclamação somente se a descrição não estiver vazia."""
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
    """Abra uma tela de UI para exibir relatórios do usuário.
    Parâmetros:
        - root (tk.Tk): A janela raiz ou o widget principal pai.
        - email (str): O identificador de e-mail para o usuário cujos relatórios serão exibidos.
        - voltar_callback (função): Uma função de retorno acionada quando o botão 'Voltar' é pressionado.
    Retornos:
        - tk.Frame: O quadro que contém o relatório exibe elementos da interface do usuário.
    Lógica de processamento:
        - Recupera e lista todos os relatórios associados ao email do usuário.
        - Se os relatórios existirem, eles são exibidos com detalhes como status, data, tipo e descrição.
        - Se nenhum relatório for encontrado, uma mensagem indicando que não há relatórios registrados é mostrada.
        - Adiciona um botão 'Voltar' que chama a função callback fornecida com "menu" como argumento."""
    denuncias = listar_denuncias_usuario(email)
    frame = tk.Frame(root, bg=COR_FUNDO)
    
    if denuncias:
        tk.Label(frame, text="Suas Denúncias:", font=("Helvetica", 16, "bold"), bg=COR_FUNDO).pack(pady=10)
        for denuncia in denuncias:
            texto = f"""Status: {denuncia['status']} | Data: {denuncia['data']}
Tipo: {denuncia['tipo']}
Descrição: {denuncia['descricao']}"""
            tk.Label(frame, text=texto, bg=COR_FUNDO, justify="left", wraplength=400).pack(pady=10, padx=20)
    else:
        tk.Label(frame, text="Nenhuma denúncia registrada.", bg=COR_FUNDO).pack(pady=30)
    
    tk.Button(frame, text="Voltar", command=lambda: voltar_callback("menu")).pack(pady=20)
    
    # Adicione estas linhas para exibir o frame corretamente:
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()
    return frame

# 🧾 Tela principal de denúncias
def criar_tela_denuncia(root, email, voltar_callback):
    """Crie uma interface de reclamação dentro do widget root usando o Tkinter.
    Parâmetros:
        - root (tk.Tk ou tk.Frame): O widget pai onde o quadro será colocado.
        - email (str): e-mail do usuário para gerenciar as funcionalidades de reclamação.
        - voltar_callback (chamável): função de retorno para lidar com ações de navegação.
    Retornos:
        - tk.Frame: Um widget de quadro contendo os elementos da interface de reclamação.
    Lógica de processamento:
        - Inclui um recipiente principal para as opções de reclamação.
        - Fornece botões para criar e visualizar reclamações, entrar em contato com autoridades legais e navegar de volta.
        - Comandos para botões usam funções lambda para passar parâmetros necessários."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Realizar Denúncia", font=("Helvetica", 22, "bold"), bg=COR_FUNDO).pack(pady=20)

    tk.Button(container, text="Escrever denúncia", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3, command=lambda: abrir_tela_escrever(root, email, voltar_callback)).pack(pady=12)

    tk.Button(container, text="Ver minhas denúncias", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3, command=lambda: abrir_tela_ver(root, email, voltar_callback)).pack(pady=12)

    # ☎️ Botão: Contatar autoridades legais — NOVO!
    tk.Button(container, text="Contatar autoridades legais", font=("Arial", 14, "bold"), bg=COR_VERDE,
          width=22, height=3,
          command=lambda: abrir_tela_contato_autoridades(root, voltar_callback)).pack(pady=12)

    # 🔙 Botão: Voltar
    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=30)

    return frame