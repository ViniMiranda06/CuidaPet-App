import json
import os

class Animal:
    """
Representa um animal com características específicas e fornece funcionalidade para converter atributos em um formato de dicionário.
Parâmetros:
- nome (str): O nome do animal.
- espécie (str): A espécie à qual o animal pertence.
- idade (int): A idade do animal.
- raça (str): A raça do animal, se aplicável.
        - descrição (str): Uma descrição textual ou detalhes característicos do animal.
- tipo (str): O tipo ou classificação do animal, por exemplo, mamífero, ave.
Lógica de processamento:
- Constrói uma instância de animal com os atributos especificados.
    """
    def __init__(self, nome, especie, idade, raca, descricao, tipo):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.descricao = descricao
        self.tipo = tipo  

    def to_dict(self):
        """Converte os atributos da instância em uma representação de dicionário.
Parâmetros:
Nenhum
Retorna:
- dict: Um dicionário contendo nomes de atributos como chaves e seus valores da instância.
Lógica de processamento:
- Mapeia os atributos da instância para pares de chave-valor no dicionário.
- Garante que todos os atributos relevantes sejam incluídos no dicionário retornado."""
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "raca": self.raca,
            "descricao": self.descricao,
            "tipo": self.tipo
        }

class GerenciadorAnimais:
    """
    A classe GerenciadorAnimais facilita o gerenciamento de listas de animais para adoção e tratamento, lidando com o armazenamento e a recuperação de dados.
Parâmetros:
- arquivo_adocao (str): Caminho do arquivo para armazenar os dados dos animais para adoção.
- arquivo_tratamento (str): Caminho do arquivo para armazenar os dados dos animais para tratamento.
    Lógica de processamento:
- Inicializa com os caminhos dos arquivos fornecidos e carrega os dados dos animais dos respectivos arquivos.
- Suporta adição, listagem, remoção e pesquisa de animais nas categorias de adoção e tratamento.
- Salva automaticamente as alterações nos respectivos arquivos após a modificação (adição ou remoção de animais).
    """
    def __init__(self, arquivo_adocao="animais_adocao.json", arquivo_tratamento="animais_tratamento.json"):
        self.arquivo_adocao = arquivo_adocao
        self.arquivo_tratamento = arquivo_tratamento
        self.animais_adocao = self.carregar_animais(self.arquivo_adocao)
        self.animais_tratamento = self.carregar_animais(self.arquivo_tratamento)

    def carregar_animais(self, arquivo):
        if not os.path.exists(arquivo):
            return []
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_animais(self, tipo):
        if tipo == "adocao":
            with open(self.arquivo_adocao, "w", encoding="utf-8") as f:
                json.dump(self.animais_adocao, f, indent=4)
        elif tipo == "tratamento":
            with open(self.arquivo_tratamento, "w", encoding="utf-8") as f:
                json.dump(self.animais_tratamento, f, indent=4)

    def adicionar_animal(self, animal):
        if animal.tipo == "adocao":
            self.animais_adocao.append(animal.to_dict())
            self.salvar_animais("adocao")
        elif animal.tipo == "tratamento":
            self.animais_tratamento.append(animal.to_dict())
            self.salvar_animais("tratamento")

    def listar_animais(self, tipo):
        if tipo == "adocao":
            return self.animais_adocao
        elif tipo == "tratamento":
            return self.animais_tratamento
        return []

    def remover_animal(self, nome, tipo):
        """Remove um animal da lista designada com base em seu nome e tipo.
Parâmetros:
- nome (str): O nome do animal a ser removido.
- tipo (str): A categoria da lista de animais (“adocação” para adoção ou “tratamento” para tratamento).
        Retorna:
- bool: Verdadeiro se o animal foi removido com sucesso, Falso se tal animal não existir.
        Lógica de processamento:
- Determina a lista correta (adoção ou tratamento) para pesquisar com base no parâmetro “tipo”.
- Itera pela lista para encontrar a primeira ocorrência de um animal com o “nome” fornecido.
- Remove o animal identificado da lista e salva as alterações.
- Retorna um booleano indicando o sucesso ou a falha da remoção."""
        lista = self.animais_adocao if tipo == "adocao" else self.animais_tratamento
        for i, a in enumerate(lista):
            if a["nome"] == nome:
                del lista[i]
                self.salvar_animais(tipo)
                return True
        return False
    
    def buscar_animal_por_id(self, id_animal, tipo):
        """Pesquise um animal pelo seu ID dentro das categorias especificadas.
Parâmetros:
- id_animal (int): O identificador único do animal.
- tipo (str): A categoria da lista de animais a pesquisar, seja ‘adocao’ ou ‘tratamento’.
Retorna:
            - dict ou None: Retorna os dados do animal como um dicionário, se encontrado; caso contrário, retorna None.
Lógica de processamento:
- A função itera pela lista especificada de animais (“adocao” ou “tratamento”).
- Ela verifica se o ID do animal corresponde ao `id_animal` fornecido.
- Retorna os dados do animal imediatamente após encontrar uma correspondência."""
        if tipo == "adocao":
            for animal in self.animais_adocao:
                if animal["id"] == id_animal:
                    return animal
        elif tipo == "tratamento":
            for animal in self.animais_tratamento:
                if animal["id"] == id_animal:
                    return animal
        return None
