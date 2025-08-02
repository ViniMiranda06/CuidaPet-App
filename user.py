import json
import os

class Usuario:
    """
    Representa um usuário com informações pessoais e de contato.
    Parâmetros:
        - nome (str): O nome do usuário.
        - email (str): O endereço de e-mail do usuário.
        - senha (str): A senha para autenticação do usuário.
        - telefone (str): O número de telefone de contato do usuário.
        - endereco (str): O endereço físico do usuário.
        - tipo (str): O tipo ou função atribuída ao usuário.
    Lógica de processamento:
        - Armazena informações do usuário como atributos de classe na inicialização.
    """
    def __init__(self, nome, email, senha, telefone, endereco, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.tipo = tipo  

    def to_dict(self):
        """Converta os atributos do objeto em uma representação de dicionário.
        Parâmetros:
            -None: Este método não leva nenhum parâmetro externo.
        Retornos:
            - dict: Um dicionário contendo os atributos do objeto com chaves como nomes de atributo e valores como valores de atributo.
        Lógica de processamento:
            - Coleta os atributos 'nome', 'email', 'senha', 'telefone', 'endereco' e 'tipo' do objeto.
            - Constrói um dicionário com nomes de atributos como chaves e valores correspondentes do objeto."""
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "tipo": self.tipo
        }

class GerenciadorUsuarios:
    """
    GerenciadorUsuarios classe é projetado para gerenciar contas de usuário armazenadas em um arquivo JSON.
    Parâmetros:
        - arquivo (str): Nome do arquivo onde os dados do usuário são armazenados, o padrão é "usuarios.json".
    Lógica de processamento:
        - Carrega usuários existentes do arquivo JSON especificado após a inicialização usando o método carregar_usuarios.
        - Adiciona novos usuários anexando à lista e salvando de volta ao arquivo JSON.
        - Facilita a autenticação do usuário, validando e-mail e senha com credenciais armazenadas.
        - Suporta a pesquisa, edição e listagem de usuários com base em e-mail e outros critérios.
    Exemplos:
        - Para criar uma instância: manager = GerenciadorUsuarios()
        - Para adicionar um usuário: manager.adicionar_usuario({"nome": "John", "email": "john@example.com", "senha": "1234"})
        - Para autenticar um usuário: ‘manager.autenticar_usuario("john@example.com", "1234")
        - Para editar os detalhes do usuário: ‘manager.editar_usuario("john@example.com", {"nome": "John Doe"}‘)
        - Para listar todos os usuários: print(manager.listar_utilizadores())
    """
    def __init__(self, arquivo="usuarios.json"):
        self.arquivo = arquivo
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_usuarios(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, indent=4)

    def adicionar_usuario(self, usuario):
        if isinstance(usuario, dict):  # Aceita tanto dicionário quanto objeto
            self.usuarios.append(usuario)
        else:
            self.usuarios.append(usuario.to_dict())
        self.salvar_usuarios()

    def buscar_usuario_por_email(self, email):
        for u in self.usuarios:
            if u["email"] == email:
                return u
        return None

    def autenticar_usuario(self, email, senha):
        """Autenticar um usuário verificando e-mail e senha.
        Parâmetros:
            - email (str): O endereço de e-mail do usuário tentando fazer login.
            - senha (str): A senha fornecida pelo usuário.
        Retornos:
            - dict ou str: Retorna o dicionário do usuário após login bem-sucedido, caso contrário retorna uma string indicando "senha_incorreta" ou "email_incorreto".
        Lógica de processamento:
            - A função primeiro recupera as informações do usuário usando o e-mail fornecido.
            - Valida a existência do usuário e verifica a senha em relação às credenciais armazenadas.
            - Fornece uma mensagem de sucesso ou indicação de erro específica com base no resultado da autenticação."""
        usuario = self.buscar_usuario_por_email(email)
        if usuario:
            if usuario["senha"] == senha:
                return usuario  # ✅ Login bem-sucedido
            else:
                return "senha_incorreta"
        else:
            return "email_incorreto"

    def editar_usuario(self, email, novos_dados):
        for i, u in enumerate(self.usuarios):
            if u["email"] == email:
                self.usuarios[i].update(novos_dados)
                self.salvar_usuarios()
                return True
        return False

    def listar_usuarios(self):
        return self.usuarios