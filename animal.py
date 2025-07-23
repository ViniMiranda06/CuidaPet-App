import json
import os

class Animal:
    """
    Represents an animal with specific characteristics and provides functionality to convert attributes into a dictionary format.
    Parameters:
        - nome (str): The name of the animal.
        - especie (str): The species to which the animal belongs.
        - idade (int): The age of the animal.
        - raca (str): The breed of the animal, if applicable.
        - descricao (str): A textual description or characteristic details of the animal.
        - tipo (str): The type or classification of the animal, e.g., mammal, bird.
    Processing Logic:
        - Constructs an animal instance with the specified attributes.
    """
    def __init__(self, nome, especie, idade, raca, descricao, tipo):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.descricao = descricao
        self.tipo = tipo  

    def to_dict(self):
        """Converts instance attributes to a dictionary representation.
        Parameters:
            None
        Returns:
            - dict: A dictionary containing attribute names as keys and their values from the instance.
        Processing Logic:
            - Maps the instance's attributes to key-value pairs in the dictionary.
            - Ensures all relevant attributes are included in the returned dictionary."""
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
    GerenciadorAnimais class facilitates the management of animal lists for adoption and treatment by handling data storage and retrieval.
    Parameters:
        - arquivo_adocao (str): File path for storing adoption animals' data.
        - arquivo_tratamento (str): File path for storing treatment animals' data.
    Processing Logic:
        - Initializes with the given file paths and loads animal data from respective files.
        - Supports adding, listing, removing, and searching animals in both adoption and treatment categories.
        - Automatically saves changes to respective files upon modification (addition or removal of animals).
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
        """Remove an animal from the designated list based on its name and type.
        Parameters:
            - nome (str): The name of the animal to be removed.
            - tipo (str): The category of the animal list ('adocao' for adoption or 'tratamento' for treatment).
        Returns:
            - bool: True if the animal was successfully removed, False if no such animal exists.
        Processing Logic:
            - Determines the correct list (adoption or treatment) to search based on the 'tipo' parameter.
            - Iterates through the list to find the first occurrence of an animal with the given 'nome'.
            - Removes the identified animal from the list and saves changes.
            - Returns boolean indicating success or failure of removal."""
        lista = self.animais_adocao if tipo == "adocao" else self.animais_tratamento
        for i, a in enumerate(lista):
            if a["nome"] == nome:
                del lista[i]
                self.salvar_animais(tipo)
                return True
        return False
    
    def buscar_animal_por_id(self, id_animal, tipo):
        """Search for an animal by its ID within specified categories.
        Parameters:
            - id_animal (int): The unique identifier of the animal.
            - tipo (str): The category of animal list to search in, either 'adocao' or 'tratamento'.
        Returns:
            - dict or None: Returns the animal's data as a dictionary if found; otherwise, returns None.
        Processing Logic:
            - The function iterates through the specified list of animals ('adocao' or 'tratamento').
            - It checks if the animal's ID matches the provided `id_animal`.
            - Returns the animal's data immediately upon finding a match."""
        if tipo == "adocao":
            for animal in self.animais_adocao:
                if animal["id"] == id_animal:
                    return animal
        elif tipo == "tratamento":
            for animal in self.animais_tratamento:
                if animal["id"] == id_animal:
                    return animal
        return None