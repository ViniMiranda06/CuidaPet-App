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
    """Salva uma reclamação no banco de dados.
Parâmetros:
- email (str): O endereço de e-mail da pessoa que está fazendo a reclamação.
- nome (str): O nome da pessoa que está fazendo a reclamação.
- tipo (str): O tipo de reclamação que está sendo feita.
- texto (str): O texto detalhado da reclamação.
    Retorna:
- Nenhum: Esta função não retorna um valor.
Lógica de processamento:
- Inicializa o arquivo JSON se ele não existir.
- Determina o novo ID para a reclamação encontrando o ID máximo existente e adicionando 1.
- Adiciona a nova reclamação à lista de reclamações existentes e as salva no arquivo."""
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
    """Exibe uma tela mostrando relatórios associados a um determinado e-mail.
Parâmetros:
- root (Tkinter Frame): O quadro raiz onde a exibição deve ser colocada.
- email (str): O endereço de e-mail usado para buscar relatórios.
- voltar_callback (função): Função de retorno de chamada a ser invocada quando o usuário quiser navegar de volta.
    Retorna:
- Nenhum
Lógica de processamento:
- Usa o parâmetro email para buscar relatórios associados.
- Se houver relatórios, os exibe; caso contrário, informa ao usuário que não há relatórios disponíveis.
- Contém um botão para retornar ao menu principal usando o callback fornecido."""
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
    """Crie uma interface de tela de relatório.
Parâmetros:
- root (tk.Tk): A janela raiz onde a interface será anexada.
- email (str): O endereço de e-mail do usuário, usado para operações contextuais.
- voltar_callback (função): Uma função de retorno de chamada a ser executada quando o botão “Voltar” for clicado.
    Retorna:
- tk.Frame: O quadro que contém os elementos da interface.
Lógica de processamento:
- Inicializa um quadro com cor de fundo específica e o coloca no centro da janela raiz.
- Adiciona um rótulo e três botões à interface, conectando-os às funções de comando apropriadas para diferentes ações."""
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