import json
import os

CAMINHO_PEDIDOS = "pedidos.json"

class GerenciadorPedidos:
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