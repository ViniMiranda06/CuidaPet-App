import json
import os

class Animal:
    """
    Representa um animal com atributos específicos para fins de adoção ou tratamento.
Parâmetros:
- nome (str): O nome do animal.
- espécie (str): A espécie do animal.
- idade (int): A idade do animal.
- raça (str): A raça do animal.
        - descrição (str): Uma descrição que fornece detalhes adicionais sobre o animal.
- tipo (str): Indica se o animal está disponível para “adoção” ou se requer “tratamento”.
Lógica de processamento:
- Armazena e gerencia atributos relacionados a um animal.
- Facilita a conversão de dados de instância em um formato de dicionário.
    """
    def __init__(self, nome, especie, idade, raca, descricao, tipo):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.descricao = descricao
        self.tipo = tipo  # 'adocao' ou 'tratamento'

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
    GerenciadorAnimais: Gerencia uma coleção de animais para fins de adoção ou tratamento.
Parâmetros:
- arquivo_adocao (str): O nome do arquivo que contém a lista de animais disponíveis para adoção.
- arquivo_tratamento (str): O nome do arquivo que contém a lista de animais em tratamento.
    Lógica de processamento:
- Carrega listas de animais de arquivos JSON especificados durante a inicialização.
- Pode salvar informações sobre os animais nos respectivos arquivos quando ocorrem modificações.
- Suporta métodos para adicionar, listar e remover animais, garantindo a persistência dos dados.
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
