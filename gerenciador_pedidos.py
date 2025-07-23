import json
import os

CAMINHO_PEDIDOS = "pedidos.json"

class GerenciadorPedidos:
    """
    A classe GerenciadorPedidos gerencia uma coleção de pedidos, lidando com persistência e validação.
Parâmetros:
- Nenhum (a inicialização não requer parâmetros).
Lógica de processamento:
- Inicializa carregando os pedidos existentes de um arquivo JSON; retorna uma lista vazia se o arquivo estiver ausente.
- Salva os pedidos de volta em um arquivo JSON, garantindo que os caracteres Unicode sejam preservados.
        - Valida a exclusividade verificando atributos específicos antes de adicionar um novo pedido.
- Fornece métodos para verificar a existência e listar pedidos específicos de um usuário.
    """
    def __init__(self):
        self.pedidos = self.carregar_pedidos()

    def carregar_pedidos(self):
        if not os.path.exists(CAMINHO_PEDIDOS):
            return []
        with open(CAMINHO_PEDIDOS, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_pedidos(self):
        with open(CAMINHO_PEDIDOS, "w", encoding="utf-8") as f:
            json.dump(self.pedidos, f, indent=4, ensure_ascii=False)

    def adicionar_pedido(self, pedido):
        """Adiciona um novo pedido à lista armazenada no formato JSON, caso ainda não exista.
Parâmetros:
- pedido (Pedido): Um objeto que representa os detalhes do pedido a ser adicionado.
Retorna:
- bool: Retorna True se o pedido foi adicionado com sucesso, False se o pedido já existe.
        Lógica de processamento:
- Carrega os pedidos existentes de um arquivo JSON.
- Verifica se algum pedido existente corresponde ao e-mail, animal_id e tipo presentes no objeto pedido fornecido.
- Acrescenta o novo pedido à lista e o salva somente se ele não corresponder a nenhum pedido existente."""
        self.pedidos = self.carregar_pedidos()  # 🔄 Atualiza a lista com o que está no JSON

        for p in self.pedidos:
            if p["email"] == pedido.email and p["animal_id"] == pedido.animal_id and p["tipo"] == pedido.tipo:
                return False  # Já solicitado

        self.pedidos.append(pedido.to_dict())
        self.salvar_pedidos()
        return True

    def pedido_ja_existe(self, email, tipo, animal_id):
        for pedido in self.pedidos:
            if pedido["email"] == email and pedido["tipo"] == tipo and pedido["animal_id"] == animal_id:
                return True
        return False

    def listar_pedidos_do_usuario(self, email):
        return [pedido for pedido in self.pedidos if pedido["email"] == email]