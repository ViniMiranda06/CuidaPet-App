import json
import os

class Pedido:
    """
    Representa um pedido relacionado a um animal, podendo ser de adoção ou tratamento.
    Parameters:
        - usuario_email (str): O endereço de e-mail do usuário que está fazendo o pedido.
        - animal_nome (str): O nome do animal relacionado ao pedido.
        - tipo (str): O tipo de pedido, que pode ser 'adocao' ou 'tratamento'.
    Processing Logic:
        - Converte a instância do pedido em um dicionário de atributos quando chamado o método to_dict.
    """
    def __init__(self, usuario_email, animal_nome, tipo):
        self.usuario_email = usuario_email
        self.animal_nome = animal_nome
        self.tipo = tipo  # 'adocao' ou 'tratamento'

    def to_dict(self):
        return {
            "usuario_email": self.usuario_email,
            "animal_nome": self.animal_nome,
            "tipo": self.tipo
        }

class GerenciadorPedidos:
    """
    O GerenciadorPedidos gerencia os pedidos dos clientes e os armazena em um arquivo JSON.
    Parâmetros:
- arquivo (str): Caminho para o arquivo JSON onde os pedidos são armazenados. O padrão é “pedidos.json”.
    Lógica de processamento:
- Carrega os pedidos existentes do arquivo JSON especificado durante a inicialização.
        - Salva os pedidos de volta no arquivo após modificações, como adições ou exclusões.
- Oferece funcionalidade para adicionar, listar e remover pedidos com base em critérios determinados.
    """
    def __init__(self, arquivo="pedidos.json"):
        self.arquivo = arquivo
        self.pedidos = self.carregar_pedidos()

    def carregar_pedidos(self):
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_pedidos(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.pedidos, f, indent=4)

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido.to_dict())
        self.salvar_pedidos()

    def listar_pedidos(self):
        return self.pedidos

    def remover_pedido(self, usuario_email, animal_nome):
        for i, p in enumerate(self.pedidos):
            if p["usuario_email"] == usuario_email and p["animal_nome"] == animal_nome:
                del self.pedidos[i]
                self.salvar_pedidos()
                return True
        return False
