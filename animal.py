import json
import os

class Animal:
    def __init__(self, nome, especie, idade, raca, descricao, tipo):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.descricao = descricao
        self.tipo = tipo  

    def to_dict(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "raca": self.raca,
            "descricao": self.descricao,
            "tipo": self.tipo
        }

class GerenciadorAnimais:
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
        lista = self.animais_adocao if tipo == "adocao" else self.animais_tratamento
        for i, a in enumerate(lista):
            if a["nome"] == nome:
                del lista[i]
                self.salvar_animais(tipo)
                return True
        return False
    
    def buscar_animal_por_id(self, id_animal, tipo):
        if tipo == "adocao":
            for animal in self.animais_adocao:
                if animal["id"] == id_animal:
                    return animal
        elif tipo == "tratamento":
            for animal in self.animais_tratamento:
                if animal["id"] == id_animal:
                    return animal
        return None