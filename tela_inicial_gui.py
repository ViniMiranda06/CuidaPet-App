import tkinter as tk
from PIL import Image, ImageTk
from menus import MenuSistema  # Conectando à lógica original

# 🎨 Cores ajustadas
COR_FUNDO = "#F4EDE3"      # fundo suave e compatível com a imagem
COR_VERDE = "#A8D5BA"      # cor dos botões

menu = MenuSistema()

# 🔗 Funções que chamam sua lógica
def abrir_tela_login():
    root.destroy()
    import login_gui  # Isso abre a janela gráfica de login

def abrir_tela_cadastro():
    root.destroy()
    import cadastro_gui  # Isso abre a janela gráfica de cadastro

# 🪟 Janela principal
root = tk.Tk()
root.title("CuidaPet - Bem-vindo")
root.geometry("500x550")
root.configure(bg=COR_FUNDO)

# 🧱 Frame centralizado
frame_principal = tk.Frame(root, bg=COR_FUNDO)
frame_principal.pack(expand=True)

# 🖼️ Logo com efeito visual
try:
    imagem_logo = Image.open("logo.png")  # coloque sua logo como 'logo.png' na pasta
    imagem_logo = imagem_logo.resize((200, 200))
    logo = ImageTk.PhotoImage(imagem_logo)
    tk.Label(frame_principal, image=logo, bg=COR_FUNDO).pack(pady=10)
except:
    tk.Label(frame_principal, text="🐾 CuidaPet", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

# 📝 Texto de boas-vindas
tk.Label(frame_principal, text="Bem-vindo ao CuidaPet!", font=("Helvetica", 18, "bold"), bg=COR_FUNDO).pack(pady=20)

# 🔘 Botões centralizados
tk.Button(frame_principal, text="Login", bg=COR_VERDE, font=("Arial", 14), width=20, height=2, command=abrir_tela_login).pack(pady=10)
tk.Button(frame_principal, text="Cadastro", bg=COR_VERDE, font=("Arial", 14), width=20, height=2, command=abrir_tela_cadastro).pack(pady=10)

root.mainloop()