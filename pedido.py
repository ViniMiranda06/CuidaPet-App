import json
import os

class Pedido:
    def __init__(self, email, animal_id, tipo):
        self.email = email
        self.animal_id = animal_id
        self.tipo = tipo

    def to_dict(self):
        return {
            "email": self.email,
            "animal_id": self.animal_id,
            "tipo": self.tipo
        }

class GerenciadorPedidos:
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
        # 🔄 Carrega pedidos atualizados direto do JSON
        pedidos_atuais = self.carregar_pedidos()

        # 🚫 Verifica se o pedido já existe
        for p in pedidos_atuais:
            if (
                p.get("email") == pedido.email and
                p.get("animal_id") == pedido.animal_id and
                p.get("tipo") == pedido.tipo
            ):
                return False  # Pedido duplicado

        # ✅ Adiciona novo pedido
        pedidos_atuais.append(pedido.to_dict())
        self.pedidos = pedidos_atuais  # atualiza a lista interna
        self.salvar_pedidos()
        return True

    def listar_pedidos_do_usuario(self, email):
        pedidos_atuais = self.carregar_pedidos()  # 🔄 Atualiza a lista com os dados reais
        return [p for p in pedidos_atuais if p.get("email") == email]

    def remover_pedido(self, email, animal_id, tipo):
        for i, p in enumerate(self.pedidos):
            if p.get("email") == email and p.get("animal_id") == animal_id and p.get("tipo") == tipo:
                del self.pedidos[i]
                self.salvar_pedidos()
                return True
        return False