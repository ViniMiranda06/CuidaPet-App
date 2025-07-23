import tkinter as tk
from tkinter import messagebox
import json

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_ADOCAO = "animais_adocao.json"
ARQUIVO_TRATAMENTO = "animais_tratamento.json"

def ler_animais_adocao():
    try:
        with open(ARQUIVO_ADOCAO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def ler_animais_tratamento():
    try:
        with open(ARQUIVO_TRATAMENTO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def salvar_animais_tratamento(lista):
    with open(ARQUIVO_TRATAMENTO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_mover_tratamento(root, voltar_callback):
    """Cria uma interface tkinter para gerenciar as atribuições de tratamento dos animais. 
    Parâmetros:
        - root (tk.Tk): A janela raiz pai para anexar este quadro.
        - voltar_callback (Callable[[str], None]): Função de retorno de chamada a ser executada ao retornar ao menu anterior.
    Retorna:
- tk.Frame: Um quadro tkinter contendo a interface para selecionar e mover animais para tratamento.
    Lógica de processamento:
- A função recupera a lista de animais disponíveis para adoção e aqueles que já estão em tratamento.
- Ela verifica se há entradas duplicadas na lista de tratamento e avisa o usuário se um animal já foi movido.
- Ao mover um animal para tratamento, ela atualiza a lista de tratamento e salva as alterações.
- Fornece um botão para voltar à tela anterior usando a função de retorno de chamada especificada."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Selecionar Animal para Tratamento", font=("Helvetica", 20, "bold"),
             bg=COR_FUNDO).pack(pady=15)

    lista_adocao = ler_animais_adocao()
    lista_tratamento = ler_animais_tratamento()
    ids_tratamento = [a["id"] for a in lista_tratamento]

    for animal in lista_adocao:
        box = tk.Frame(container, bg=COR_FUNDO, bd=1, relief="solid")
        box.pack(pady=6)

        txt = f"{animal['nome']} • {animal['especie']} • {animal['raca']} • {animal['idade']}"
        tk.Label(box, text=txt, font=("Arial", 12), bg=COR_FUNDO).pack(side="left", padx=10)

        def mover(id=animal["id"], dados=animal):
            if id in ids_tratamento:
                messagebox.showwarning("Já movido", f"{dados['nome']} já está em tratamento.")
                return
            lista_tratamento.append(dados)
            salvar_animais_tratamento(lista_tratamento)
            messagebox.showinfo("Sucesso", f"{dados['nome']} movido para tratamento.")
            voltar_callback("adm_tratamento")

        tk.Button(box, text="Mover para tratamento", font=("Arial", 10), bg=COR_MARROM,
                  command=mover).pack(side="right", padx=10)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("adm_tratamento")).pack(pady=20)

    return frame