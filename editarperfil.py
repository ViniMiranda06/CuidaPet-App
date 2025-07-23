from user import GerenciadorUsuarios

class EditorPerfil:
    """
 A classe EditorPerfil é responsável por editar as informações do perfil do usuário.
Parâmetros:
- gerenciador_usuarios (GerenciadorUsuarios): Uma instância do GerenciadorUsuarios que gerencia os dados e as operações do usuário.
Lógica de processamento:
- Utiliza métodos da classe GerenciadorUsuarios para atualizar informações específicas do perfil de um usuário com base no e-mail do usuário.
        - As operações de atualização incluem a modificação do nome, e-mail, senha, número de telefone e endereço do usuário.
- As alterações são confirmadas invocando o método ‘editar_usuario’ da instância GerenciadorUsuarios.
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
