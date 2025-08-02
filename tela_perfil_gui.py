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
    """Pesquisa dados do usuário com base no endereço de e-mail.
Parâmetros:
- e-mail (str): O endereço de e-mail do usuário a ser pesquisado no banco de dados.
    Retorna:
- dict ou None: Um dicionário contendo os dados do usuário, se o e-mail for encontrado; caso contrário, None.
Lógica de processamento:
- Verifica se o arquivo do banco de dados existe antes de tentar qualquer operação.
- Carrega os dados do usuário do arquivo JSON.
- Itera pelos registros do usuário para encontrar um e-mail correspondente."""
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
    """Atualiza os dados do usuário com base em seu e-mail.
Parâmetros:
- e-mail (str): O e-mail do usuário cujos dados precisam ser atualizados.
- novos_dados (dict): Um dicionário com pares chave-valor para os novos dados a serem atualizados.
Retorna:
- Nenhum: Esta função não retorna um valor.
    Lógica de processamento:
- Lê os dados existentes do usuário a partir de um arquivo JSON.
- Procura o usuário pelo e-mail e atualiza seus dados com os valores fornecidos.
- Grava os dados atualizados do usuário de volta no arquivo JSON."""
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
    """Cria uma interface de tela de perfil dentro de uma determinada janela raiz.
Parâmetros:
- root (tk.Tk ou tk.Widget): A janela principal do aplicativo ou widget pai onde a tela de perfil será colocada.
- email (str): O e-mail do usuário, usado para buscar e exibir dados relevantes do perfil.
        - voltar_callback (callable): Uma função de retorno de chamada a ser executada ao retornar ao menu anterior.
Retorna:
- tk.Frame: Um quadro contendo os elementos da interface do perfil do usuário, pronto para ser exibido na janela raiz.
Lógica de processamento:
- A tela de perfil é centralizada vertical e horizontalmente dentro da janela raiz.
        - Uma etiqueta exibindo “Meu Perfil” é incluída na parte superior da interface.
- Um botão “Ver meus dados” é fornecido para permitir que os usuários visualizem seus dados, chamando uma função com os parâmetros necessários.
- Um botão “Voltar” é fornecido para retornar ao menu, utilizando a função de retorno de chamada fornecida."""
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
    """Exibe a tela de dados do usuário com opções para edição e exclusão em um aplicativo Tkinter.
Parâmetros:
- root (widget Tkinter): A janela raiz ou widget pai onde o quadro será colocado.
- email (str): O e-mail do usuário cujos dados devem ser recuperados e exibidos.
        - voltar_callback (função): Uma função de retorno de chamada acionada quando o botão “Voltar” é pressionado.
Retorna:
- Nenhum: Esta função não retorna um valor; ela modifica a interface do usuário adicionando componentes ao quadro Tkinter.
    Lógica de processamento:
- Recupera os dados do usuário com base no e-mail fornecido e os exibe, se disponíveis.
- Renderiza um botão para facilitar a edição dos dados do usuário, que abre outra tela.
- Oferece uma opção para excluir a conta do usuário, com confirmação, removendo os dados associados.
- Inclui um botão para navegar de volta à tela do menu por meio do callback fornecido."""
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
    """Abra uma tela de edição para que o usuário possa atualizar suas informações pessoais.
Parâmetros:
- root (tk.Tk ou tk.Widget): A raiz da janela ou widget onde o quadro será criado.
- email (str): O endereço de e-mail do usuário para pesquisa e atualização de dados.
        - back_callback (função): Callback a ser chamado ao clicar no botão voltar, que navega para uma tela diferente.
    Retornos:
- None: A função não retorna um valor.
    Lógica de processamento:
- Cria um quadro dentro da raiz para exibir os campos de entrada e botões.
        - Inicializa os campos de entrada com os dados do usuário obtidos a partir do e-mail fornecido.
- Quando o botão "Confirmar" é pressionado, atualiza as informações do usuário e exibe uma mensagem de confirmação.
- Quando o botão "Voltar" é pressionado, executa a função de retorno para retornar à tela do menu."""
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
