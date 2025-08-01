import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from menus import MenuSistema
from user import Usuario

# Variáveis globais
email_global = ""
frame_menu = None
frame_pedidos = None
frame_animais_adocao = None
frame_animais_tratamento = None
frame_denuncia = None
frame_perfil = None
frame_sobre = None
frame_menu_admin = None
frame_adm_adocao = None
frame_adicionar_animal = None
frame_adm_tratamento = None
frame_mover_tratamento = None
frame_adm_usuarios = None
frame_adm_denuncias = None
frame_adm_feedbacks = None


# 🎨 Cores
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()
root = tk.Tk()
root.title("CuidaPet")
root.geometry("500x550")
root.configure(bg=COR_FUNDO)

# 🖼️ Carregar logo uma vez
try:
    imagem_logo = Image.open("logo.png")
    imagem_logo = imagem_logo.resize((250, 220))
    logo = ImageTk.PhotoImage(imagem_logo)
except:
    logo = None

# 🔁 Função para trocar de tela
def mostrar_tela(nome):
    if nome == "inicial":
        tela_inicial.tkraise()
    elif nome == "login":
        tela_login.tkraise()
    elif nome == "cadastro":
        tela_cadastro.tkraise()
    elif nome == "menu":
        frame_menu.tkraise()
    elif nome == "adocao":
        frame_animais_adocao.tkraise()
    elif nome == "tratamento":
        frame_animais_tratamento.tkraise()
    elif nome == "pedidos":
        from tela_pedidos_gui import criar_tela_pedidos
        global frame_pedidos
        if frame_pedidos:
            frame_pedidos.destroy()
        frame_pedidos = criar_tela_pedidos(root, email_global, mostrar_tela)
        frame_pedidos.place(x=0, y=0, relwidth=1, relheight=1)
        frame_pedidos.tkraise()

    elif nome == "denuncia":
        if frame_denuncia:
            frame_denuncia.tkraise()
        else:
            print("[DEBUG] Frame de denúncia não foi criado ainda.")

    elif nome == "perfil":
        frame_perfil.tkraise()

    elif nome == "sobre":
        frame_sobre.tkraise()

    elif nome == "menu_admin":
        frame_menu_admin.tkraise()

    elif nome == "adm_adicionar":
        global frame_adicionar_animal
        from tela_adm_adicionar_animal import criar_tela_adicionar_animal
        frame_adicionar_animal = criar_tela_adicionar_animal(root, mostrar_tela)
        frame_adicionar_animal.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adicionar_animal.tkraise()

    elif nome == "adm_adocao":
        global frame_adm_adocao
        from tela_adm_animais import criar_tela_adm_animais
        frame_adm_adocao = criar_tela_adm_animais(root, mostrar_tela)
        frame_adm_adocao.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adm_adocao.tkraise()

    elif nome == "adm_tratamento":
        global frame_adm_tratamento
        from tela_adm_tratamento import criar_tela_adm_tratamento
        frame_adm_tratamento = criar_tela_adm_tratamento(root, mostrar_tela)
        frame_adm_tratamento.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adm_tratamento.tkraise()

    elif nome == "adm_tratamento_adicionar":
        global frame_mover_tratamento
        from tela_adm_mover_tratamento import criar_tela_mover_tratamento
        frame_mover_tratamento = criar_tela_mover_tratamento(root, mostrar_tela)
        frame_mover_tratamento.place(x=0, y=0, relwidth=1, relheight=1)
        frame_mover_tratamento.tkraise()

    elif nome == "adm_usuarios":
        global frame_adm_usuarios
        from tela_adm_usuarios import criar_tela_adm_usuarios
        frame_adm_usuarios = criar_tela_adm_usuarios(root, mostrar_tela)
        frame_adm_usuarios.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adm_usuarios.tkraise()

    elif nome == "adm_denuncias":
        global frame_adm_denuncias
        from tela_adm_denuncias import criar_tela_adm_denuncias
        frame_adm_denuncias = criar_tela_adm_denuncias(root, mostrar_tela)
        frame_adm_denuncias.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adm_denuncias.tkraise()

    elif nome == "adm_feedbacks":
        global frame_adm_feedbacks
        from tela_adm_feedbacks import criar_tela_adm_feedbacks
        frame_adm_feedbacks = criar_tela_adm_feedbacks(root, mostrar_tela)
        frame_adm_feedbacks.place(x=0, y=0, relwidth=1, relheight=1)
        frame_adm_feedbacks.tkraise()




# 📃 TELA INICIAL
tela_inicial = tk.Frame(root, bg=COR_FUNDO)
tela_inicial.place(x=0, y=0, relwidth=1, relheight=1)

frame_inicial = tk.Frame(tela_inicial, bg=COR_FUNDO)
frame_inicial.pack(expand=True)

if logo:
    tk.Label(frame_inicial, image=logo, bg=COR_FUNDO).pack(pady=10)
tk.Label(frame_inicial, text="Bem-vindo ao CuidaPet!", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=10)
tk.Button(frame_inicial, text="Login", font=("Arial", 14), bg=COR_VERDE, width=20, height=2, command=lambda: mostrar_tela("login")).pack(pady=10)
tk.Button(frame_inicial, text="Cadastro", font=("Arial", 14), bg=COR_VERDE, width=20, height=2, command=lambda: mostrar_tela("cadastro")).pack(pady=10)



# 🔐 TELA DE LOGIN
tela_login = tk.Frame(root, bg=COR_FUNDO)
tela_login.place(x=0, y=0, relwidth=1, relheight=1)

frame_login = tk.Frame(tela_login, bg=COR_FUNDO)
frame_login.pack(expand=True)

if logo:
    tk.Label(frame_login, image=logo, bg=COR_FUNDO).pack(pady=10)
tk.Label(frame_login, text="Login", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=10)
tk.Label(frame_login, text="Email", font=("Arial", 12), bg=COR_FUNDO).pack()
entry_email = tk.Entry(frame_login, font=("Arial", 12), width=30)
entry_email.pack(pady=5)
tk.Label(frame_login, text="Senha", font=("Arial", 12), bg=COR_FUNDO).pack()
entry_senha = tk.Entry(frame_login, font=("Arial", 12), width=30, show="*")
entry_senha.pack(pady=5)

def autenticar():
    email = entry_email.get().strip()
    senha = entry_senha.get().strip()
    resultado = menu.usuarios.autenticar_usuario(email, senha)

    if resultado == "email_incorreto":
        messagebox.showerror("Erro", "Email incorreto.")
        return

    elif resultado == "senha_incorreta":
        messagebox.showerror("Erro", "Senha incorreta.")
        return

    elif isinstance(resultado, dict):  # Login bem-sucedido
        usuario = resultado
        global email_global, frame_menu, frame_animais_adocao, frame_animais_tratamento, frame_pedidos, frame_denuncia, frame_perfil, frame_sobre, frame_menu_admin, frame_adm_adocao, frame_adicionar_animal, frame_adm_tratamento, frame_mover_tratamento, frame_adm_usuarios, frame_adm_denuncias, frame_adm_feedbacks
        email_global = email
        tipo = usuario.get("tipo", "usuario")
        messagebox.showinfo("Login", f"Bem-vindo, {usuario['nome']}!")

        # Painel do ADMIN
        if tipo == "administrador":
            if frame_menu_admin is None:
                from tela_menu_admin import criar_tela_menu_admin
                frame_menu_admin = criar_tela_menu_admin(root, email_global, mostrar_tela)
                frame_menu_admin.place(x=0, y=0, relwidth=1, relheight=1)
            mostrar_tela("menu_admin")
            return

        # Painel do USUÁRIO
        if frame_menu is None:
            from tela_menu_usuario import criar_tela_menu_usuario
            frame_menu = criar_tela_menu_usuario(root, email_global, mostrar_tela)
            frame_menu.place(x=0, y=0, relwidth=1, relheight=1)

        if frame_animais_adocao is None or frame_animais_tratamento is None:
            from tela_animais_gui import criar_tela_animais
            frame_animais_adocao = criar_tela_animais(root, "adocao", email_global, mostrar_tela)
            frame_animais_adocao.place(x=0, y=0, relwidth=1, relheight=1)
            frame_animais_tratamento = criar_tela_animais(root, "tratamento", email_global, mostrar_tela)
            frame_animais_tratamento.place(x=0, y=0, relwidth=1, relheight=1)

        if frame_pedidos is None:
            from tela_pedidos_gui import criar_tela_pedidos
            frame_pedidos = criar_tela_pedidos(root, email_global, mostrar_tela)
            frame_pedidos.place(x=0, y=0, relwidth=1, relheight=1)

        if frame_denuncia is None:
            from tela_denuncia_gui import criar_tela_denuncia
            frame_denuncia = criar_tela_denuncia(root, email_global, mostrar_tela)
            frame_denuncia.place(x=0, y=0, relwidth=1, relheight=1)

        if frame_perfil is None:
            from tela_perfil_gui import criar_tela_perfil
            frame_perfil = criar_tela_perfil(root, email_global, mostrar_tela)
            frame_perfil.place(x=0, y=0, relwidth=1, relheight=1)

        if frame_sobre is None:
            from tela_sobre_gui import criar_tela_sobre
            frame_sobre = criar_tela_sobre(root, email_global, mostrar_tela)
            frame_sobre.place(x=0, y=0, relwidth=1, relheight=1)

        mostrar_tela("menu")

tk.Button(frame_login, text="Entrar", font=("Arial", 14), bg=COR_VERDE, command=autenticar).pack(pady=10)
tk.Button(frame_login, text="Voltar", font=("Arial", 12), command=lambda: mostrar_tela("inicial")).pack()

# 📝 TELA DE CADASTRO
tela_cadastro = tk.Frame(root, bg=COR_FUNDO)
tela_cadastro.place(x=0, y=0, relwidth=1, relheight=1)

frame_cadastro = tk.Frame(tela_cadastro, bg=COR_FUNDO)
frame_cadastro.pack(expand=True)

if logo:
    tk.Label(frame_cadastro, image=logo, bg=COR_FUNDO).pack(pady=10)
tk.Label(frame_cadastro, text="Cadastro", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=10)

campos = {}
for campo in ["Nome", "Email", "Senha", "Telefone", "Endereço"]:
    tk.Label(frame_cadastro, text=campo, font=("Arial", 12), bg=COR_FUNDO).pack()
    entry = tk.Entry(frame_cadastro, font=("Arial", 12), width=30, show="*" if campo == "Senha" else None)
    entry.pack(pady=5)
    campos[campo.lower()] = entry

def cadastrar():
    # Validações
    nome = campos["nome"].get().strip()
    email = campos["email"].get().strip()
    senha = campos["senha"].get().strip()
    telefone = campos["telefone"].get().strip()
    endereco = campos["endereço"].get().strip()

    if not nome:
        messagebox.showerror("Erro", "Nome não pode ser vazio!")
        return

    if "@" not in email or "." not in email.split("@")[1]:
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    if len(senha) < 6:
        messagebox.showerror("Erro", "Senha deve ter pelo menos 6 caracteres.")
        return

    if not telefone.isdigit() or len(telefone) != 11:
        messagebox.showerror("Erro", "Telefone deve ter 11 dígitos numéricos.")
        return

    # Verifica se usuário já existe
    if menu.usuarios.buscar_usuario_por_email(email):
        messagebox.showerror("Erro", "Usuário já cadastrado!")
        return

    # Cria objeto Usuario e cadastra
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        telefone=telefone,
        endereco=endereco,
        tipo="usuario"
    )
    menu.usuarios.adicionar_usuario(novo_usuario)
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    mostrar_tela("login")

tk.Button(frame_cadastro, text="Cadastre-se", font=("Arial", 14), bg=COR_VERDE, command=cadastrar).pack(pady=10)
tk.Button(frame_cadastro, text="Voltar", font=("Arial", 12), command=lambda: mostrar_tela("inicial")).pack()

# 🔁 Inicia na tela inicial
tela_inicial.tkraise()
root.mainloop()
