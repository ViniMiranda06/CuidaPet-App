import tkinter as tk
import json
from tkinter import messagebox

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_ADOCAO = "animais_adocao.json"

def ler_animais():
    try:
        with open(ARQUIVO_ADOCAO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def salvar_animais(lista):
    with open(ARQUIVO_ADOCAO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_adm_animais(root, voltar_callback):
    """Cria e retorna um quadro para a tela de administração mostrando animais disponíveis para adoção.
    Parâmetros:
        - root (tk.Tk ou tk.Frame): A janela de raiz ou quadro onde este novo quadro deve ser compactado ou colocado.
        - voltar_callback (função): função de retorno a ser executada quando os botões "Excluir" ou quaisquer outros controles são pressionados.
    Retornos:
        - tk.Frame: Um quadro contendo os elementos da interface de administração para gerenciar animais.
    Lógica de processamento:
        - O quadro exibe uma lista de animais disponíveis para adoção, cada um com um botão "Excluir" para remover o animal da lista.
        - Um animal pode ser adicionado à lista com um nome padrão, espécie e idade usando o botão "Adicionar animal".
        - O botão "Voltar" usa o `voltar_callback` para navegar de volta à tela ou menu anterior."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Animais em Adoção", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=15)

    lista = ler_animais()

    # Exibição dos blocos
    for animal in lista:
        box = tk.Frame(container, bg=COR_FUNDO, bd=1, relief="solid")
        box.pack(pady=6)

        txt = f"{animal['nome']} • {animal['especie']} • {animal['idade']}"
        tk.Label(box, text=txt, font=("Arial", 12), bg=COR_FUNDO).pack(side="left", padx=10)

        def excluir(id=animal["id"], nome=animal["nome"]):
            if messagebox.askyesno("Confirmação", f"Deseja excluir {nome}?"):
                nova = [a for a in lista if a["id"] != id]
                salvar_animais(nova)
                messagebox.showinfo("Excluído", f"{nome} foi removido.")
                voltar_callback("adm_adocao")

        tk.Button(box, text="Excluir", font=("Arial", 10), bg=COR_MARROM, command=excluir).pack(side="right", padx=10)

    # Botão para adicionar novo animal
    def adicionar():
        """Adiciona uma nova entrada animal com propriedades padrão à lista e atualiza o armazenamento persistente.
        Parâmetros:
            Nenhum
        Retornos:
            Nenhum
        Lógica de processamento:
            - Gera um ID único com base em entradas existentes na lista.
            - Anexa uma nova entrada com atributos pré-definidos à lista.
            - Chama de `salvar_animais` para persistir as alterações no armazenamento.
            - Exibe uma confirmação de messagebox e invoca um retorno de chamada para atualizar a interface do usuário."""
        novo_id = max([a["id"] for a in lista] + [-1]) + 1
        novo = {
            "id": novo_id,
            "nome": "Novo Animal",
            "especie": "Espécie",
            "idade": "Idade"
        }
        lista.append(novo)
        salvar_animais(lista)
        messagebox.showinfo("Adicionado", "Animal de teste adicionado.")
        voltar_callback("adm_adocao")

    tk.Button(container, text="Adicionar animal", font=("Arial", 12), bg=COR_MARROM,
          width=20, command=lambda: voltar_callback("adm_adicionar")).pack(pady=20)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("menu_admin")).pack(pady=10)

    return frame