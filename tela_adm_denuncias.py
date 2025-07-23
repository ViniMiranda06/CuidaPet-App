import tkinter as tk
import json
from tkinter import messagebox

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_DENUNCIAS = "denuncias.json"

def ler_denuncias():
    try:
        with open(ARQUIVO_DENUNCIAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def salvar_denuncias(lista):
    with open(ARQUIVO_DENUNCIAS, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_adm_denuncias(root, voltar_callback):
    """Crie a tela do administrador para visualizar e gerenciar as reclamações recebidas.
Parâmetros:
- root (tk.Tk ou tk.Frame): O widget raiz onde a tela de reclamações do administrador será colocada.
- voltar_callback (função): Função de retorno de chamada para lidar com a navegação “voltar”, aceitando um identificador de tela.
    Retorna:
- tk.Frame: O quadro que contém a tela do administrador para reclamações.
Lógica de processamento:
- Lê e exibe uma lista de reclamações obtidas de uma fonte de dados.
- Cada reclamação é apresentada com opções para visualizar detalhes ou excluir.
- Fornece um botão “Voltar” para retornar ao menu do administrador."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Denúncias Recebidas", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=15)

    lista = ler_denuncias()

    for denuncia in lista:
        box = tk.Frame(container, bg=COR_FUNDO, bd=1, relief="solid")
        box.pack(pady=6)

        texto = f"{denuncia['nome']} • {denuncia['tipo']} • {denuncia['descricao']}"
        tk.Label(box, text=texto, font=("Arial", 11), bg=COR_FUNDO, wraplength=400, justify="left").pack(side="left", padx=10)

        def excluir(id=denuncia["id"], nome=denuncia["nome"]):
            if messagebox.askyesno("Confirmação", f"Excluir denúncia de {nome}?"):
                nova = [d for d in lista if d["id"] != id]
                salvar_denuncias(nova)
                messagebox.showinfo("Excluído", f"Denúncia de {nome} removida.")
                voltar_callback("adm_denuncias")

        tk.Button(box, text="Excluir", font=("Arial", 10), bg=COR_MARROM, command=excluir).pack(side="right", padx=10)

    tk.Button(container, text="Voltar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("menu_admin")).pack(pady=20)

    return frame
