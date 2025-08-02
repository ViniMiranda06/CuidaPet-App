from user import GerenciadorUsuarios

class EditorPerfil:
    """
    A classe EditorPerfil permite editar vários atributos do perfil do usuário por meio de um gerenciador de usuários.
Parâmetros:
- gerenciador_usuarios (GerenciadorUsuarios): uma instância do GerenciadorUsuarios responsável por gerenciar as operações de dados do usuário.
    Lógica de processamento:
- Utiliza a instância gerenciador_usuarios para atualizar os atributos do perfil do usuário.
- Cada método envia um dicionário contendo o novo atributo e seu valor para um método em gerenciador_usuarios.
- Retorna o resultado da operação realizada pelo gerenciador_usuarios.
    """
    def __init__(self, gerenciador_usuarios: GerenciadorUsuarios):
        self.gerenciador = gerenciador_usuarios

    def editar_nome(self, email, novo_nome):
        return self.gerenciador.editar_usuario(email, {"nome": novo_nome})

    def editar_email(self, email_atual, novo_email):
        return self.gerenciador.editar_usuario(email_atual, {"email": novo_email})

    def editar_senha(self, email, nova_senha):
        return self.gerenciador.editar_usuario(email, {"senha": nova_senha})

    def editar_telefone(self, email, novo_telefone):
        return self.gerenciador.editar_usuario(email, {"telefone": novo_telefone})

    def editar_endereco(self, email, novo_endereco):
        return self.gerenciador.editar_usuario(email, {"endereco": novo_endereco})