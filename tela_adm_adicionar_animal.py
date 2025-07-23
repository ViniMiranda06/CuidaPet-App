import tkinter as tk
from tkinter import messagebox
import json
import os

COR_FUNDO = "#F4EDE3"
COR_MARROM = "#BFA6A0"
ARQUIVO_ADOCAO = "animais_adocao.json"

def salvar_animal(novo):
    """Salva uma nova entrada de animal no arquivo de adoção.
Parâmetros:
- novo (dict): Um dicionário contendo detalhes do novo animal a ser adicionado, incluindo “id”, se aplicável.
Retorna:
- Nenhum: Esta função não retorna um valor.
    Lógica de processamento:
- Verifica se o arquivo de adoção já existe e carrega seu conteúdo; caso contrário, começa com uma lista vazia.
- Atribui ao novo animal um “id” único, calculando o id máximo existente no arquivo e incrementando-o.
- Acrescenta a nova entrada de animal à lista e salva a lista atualizada de volta no arquivo."""
    if os.path.exists(ARQUIVO_ADOCAO):
        with open(ARQUIVO_ADOCAO, "r", encoding="utf-8") as f:
            lista = json.load(f)
    else:
        lista = []

    novo["id"] = max([a.get("id", 0) for a in lista] + [-1]) + 1
    lista.append(novo)

    with open(ARQUIVO_ADOCAO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

def criar_tela_adicionar_animal(root, voltar_callback):
    """Cria uma estrutura de interface do usuário para adicionar um novo animal para adoção.
Parâmetros:
- root (tk.Tk ou tk.Frame): O widget pai onde a estrutura será colocada.
- voltar_callback (função): Uma função de retorno de chamada invocada quando o usuário deseja voltar para a tela anterior.
Retorna:
- tk. Frame: Um quadro contendo todos os componentes da interface do usuário para o formulário “Adicionar animal”.
Lógica de processamento:
- Constrói um formulário da interface do usuário com campos para “Nome”, “Espécie”, “Raça” e “Idade”.
- Inclui os botões “Salvar” e “Cancelar” com as respectivas ações.
- Valida se todos os campos de entrada foram preenchidos antes de salvar os detalhes do animal."""
    frame = tk.Frame(root, bg=COR_FUNDO)
    container = tk.Frame(frame, bg=COR_FUNDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Adicionar Animal em Adoção", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

    # Campos de entrada
    tk.Label(container, text="Nome:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_nome = tk.Entry(container, font=("Arial", 12), width=30)
    entry_nome.pack(pady=5)

    tk.Label(container, text="Espécie:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_especie = tk.Entry(container, font=("Arial", 12), width=30)
    entry_especie.pack(pady=5)

    tk.Label(container, text="Raça:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_raca = tk.Entry(container, font=("Arial", 12), width=30)
    entry_raca.pack(pady=5)

    tk.Label(container, text="Idade:", font=("Arial", 12), bg=COR_FUNDO).pack()
    entry_idade = tk.Entry(container, font=("Arial", 12), width=30)
    entry_idade.pack(pady=5)

    def adicionar():
        """Adiciona um novo registro de animal após validar os campos de entrada.
Parâmetros:
- Nenhum
Retorna:
- Nenhum
Lógica de processamento:
- Recupera e corta as entradas do usuário dos campos de entrada para “nome”, “espécie”, “raça” e “idade”.
            - Verifica se algum campo de entrada está vazio e exibe uma mensagem de erro, se for o caso.
- Cria um dicionário com os detalhes do animal fornecidos e o salva usando `salvar_animal`.
- Exibe uma mensagem de sucesso após a adição bem-sucedida do animal.
- Chama `voltar_callback` com um identificador de visualização para atualizar a interface."""
        nome = entry_nome.get().strip()
        especie = entry_especie.get().strip()
        raca = entry_raca.get().strip()
        idade = entry_idade.get().strip()

        if not nome or not especie or not raca or not idade:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        novo = {
            "nome": nome,
            "especie": especie,
            "raca": raca,
            "idade": idade
        }
        salvar_animal(novo)
        messagebox.showinfo("Sucesso", "Animal adicionado com sucesso!")
        voltar_callback("adm_adocao")

    tk.Button(container, text="Salvar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=adicionar).pack(pady=15)

    tk.Button(container, text="Cancelar", font=("Arial", 12), bg=COR_MARROM,
              width=20, command=lambda: voltar_callback("adm_adocao")).pack(pady=5)

    return frame