import json
import os

class Pedido:
    """A classe Pedido representa um pedido ou solicitação associada a um animal e usuário específicos.
Parâmetros:
- email (str): O endereço de e-mail do usuário que está fazendo o pedido.
- animal_id (int): O identificador único do animal associado ao pedido.
- tipo (str): O tipo de pedido que está sendo solicitado.
    Lógica de processamento:
- Inicializa uma instância Pedido com o e-mail, animal_id e tipo fornecidos.
- O método to_dict converte os atributos da instância Pedido em um formato de dicionário para facilitar o armazenamento ou a serialização."""
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
    """
    Gerencia uma lista de pedidos carregando, salvando e atualizando um arquivo JSON.
Parâmetros:
- arquivo (str): Caminho para o arquivo JSON onde os pedidos são armazenados. O padrão é “pedidos.json”.
Lógica de processamento:
- Se o arquivo JSON não existir, inicializa uma lista vazia de pedidos.
        - Garante que a lista de pedidos esteja sempre atualizada com o conteúdo do arquivo.
- Usa serialização/desserialização JSON para lidar com o armazenamento e a recuperação de dados.
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
        # 🔄 Carrega pedidos atualizados direto do JSON
        """Adiciona um novo pedido à lista, caso ainda não exista.
Parâmetros:
- pedido (objeto): O objeto do pedido contendo os atributos “email”, “animal_id” e “tipo”.
Retorna:
- bool: Retorna True se o pedido for adicionado com sucesso, False se o pedido for uma duplicata.
        Lógica de processamento:
- Carrega a lista atual de pedidos de um arquivo JSON.
- Verifica se já existe um pedido com o mesmo “email”, “animal_id” e “tipo” na lista.
- Adiciona o novo pedido à lista e o salva, se nenhuma duplicata for encontrada."""
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