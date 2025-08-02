import tkinter as tk

# 🎨 Cores padrão CuidaPet
COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

# 🌐 Tela com link da autoridade
def abrir_tela_link_autoridade(root, voltar_callback, nome_autoridade, link):
    """Exibe uma janela da interface do usuário com informações sobre como acessar o site de uma autoridade por meio de um link fornecido.
Parâmetros:
- root (tk.Widget): O widget Tkinter raiz no qual a janela da interface do usuário será colocada.
- voltar_callback (Callable): Função a ser chamada quando o botão Voltar for pressionado.
        - nome_autoridade (str): Nome da autoridade cujo link do site é exibido.
- link (str): Link URL para o site da autoridade.
Retorna:
- Nenhum: Esta função não retorna um valor.
    Lógica de processamento:
- O quadro é criado e elevado para ocupar todo o espaço do widget raiz.
- É exibida uma mensagem de texto solicitando ao usuário que copie o link.
- O link é inserido em um campo de texto somente leitura.
- É fornecido um botão para navegar de volta para outra parte do aplicativo."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    mensagem = f"Copie e cole no seu navegador para acessar o site da {nome_autoridade}:"
    tk.Label(container, text=mensagem, font=("Arial", 14), bg=COR_FUNDO,
             wraplength=500, justify="center").pack(pady=(20, 10))

    campo_link = tk.Text(container, width=50, height=2, font=("Arial", 12))
    campo_link.pack(pady=10)
    campo_link.insert("1.0", link)
    campo_link.config(state="disabled")  # Somente leitura

    # 🔙 Botão Voltar
    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=30)

# 🧾 Tela principal de autoridades
def abrir_tela_contato_autoridades(root, voltar_callback):
    """Crie uma interface GUI para entrar em contato com as autoridades.
Parâmetros:
- root (tk.Tk): A janela raiz onde o quadro é colocado.
- voltar_callback (função): Uma função de retorno de chamada que navega de volta para um menu especificado.
Retorna:
- Nenhum: Esta função não retorna um valor; ela configura os componentes da GUI.
    Lógica de processamento:
- Um quadro principal é levantado para cobrir toda a janela da interface de contato com as autoridades.
- Vários botões são criados dentro de um contêiner para navegar para as páginas de contato de diferentes autoridades.
- Um botão “Voltar” é incluído para executar a função voltar_callback, auxiliando na navegação de volta ao menu."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.tkraise()

    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Contatar Autoridades", font=("Helvetica", 22, "bold"), bg=COR_FUNDO).pack(pady=20)

    # 👮 Polícia Militar
    tk.Button(container, text="Polícia Militar", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3,
              command=lambda: abrir_tela_link_autoridade(
                  root, voltar_callback, "Polícia Militar", "https://www.pm.pe.gov.br/"
              )).pack(pady=10)

    # ☎️ Disque denúncia
    tk.Button(container, text="Disque denúncia", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3,
              command=lambda: abrir_tela_link_autoridade(
                  root, voltar_callback, "Disque denúncia", "https://www.pe.gov.br/servico/disque-denuncia/"
              )).pack(pady=10)

    # 🌿 Ibama
    tk.Button(container, text="Ibama", font=("Arial", 14, "bold"), bg=COR_VERDE,
              width=22, height=3,
              command=lambda: abrir_tela_link_autoridade(
                  root, voltar_callback, "Ibama", "https://servicos.ibama.gov.br/ctf/"
              )).pack(pady=10)

    # 🔙 Botão Voltar
    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_VERDE,
              width=20, height=2, command=lambda: voltar_callback("menu")).pack(pady=30)