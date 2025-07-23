import json
import os

class Usuario:
    """Representa um usuário com atributos específicos.
    Parâmetros:
- nome (str): O nome do usuário.
- email (str): O endereço de e-mail do usuário.
- senha (str): A senha da conta do usuário.
- telefone (str): O número de telefone do usuário.
- endereço (str): O endereço físico do usuário.
        - tipo (str): O tipo de usuário, seja ‘usuário’ ou ‘administrador’.
    Lógica de processamento:
- Armazena informações do usuário com validação para o tipo de usuário ser ‘usuário’ ou ‘administrador’.
- Fornece um método para converter os atributos do usuário em um formato de dicionário para fácil acesso e manipulação."""
    def __init__(self, nome, email, senha, telefone, endereco, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.tipo = tipo  # 'usuario' ou 'administrador'

    def to_dict(self):
        """Converte os atributos de uma instância em um dicionário.
Retorna:
- dict: Um dicionário contendo os atributos da instância como pares chave-valor.
Lógica de processamento:
- Extraia vários atributos da instância e os mapeia para chaves com nomes idênticos em um dicionário."""
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
    Gerenciador de dados do usuário armazenados em um arquivo JSON.
Parâmetros:
- arquivo (str): Nome do arquivo JSON onde os dados do usuário estão armazenados. O padrão é “users.json”.
    Lógica de processamento:
- Carrega os usuários do arquivo JSON, se ele existir; caso contrário, retorna uma lista vazia.
- Permite adicionar novos usuários à lista e salva as alterações no arquivo.
- Pesquisa usuários por e-mail para autenticar ou editar suas informações.
- Fornece métodos para listar todos os usuários atualmente armazenados.
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
        self.usuarios.append(usuario.to_dict())
        self.salvar_usuarios()

    def buscar_usuario_por_email(self, email):
        for u in self.usuarios:
            if u["email"] == email:
                return u
        return None

    def autenticar_usuario(self, email, senha):
        usuario = self.buscar_usuario_por_email(email)
        if usuario and usuario["senha"] == senha:
            return usuario
        return None

    def editar_usuario(self, email, novos_dados):
        for i, u in enumerate(self.usuarios):
            if u["email"] == email:
                self.usuarios[i].update(novos_dados)
                self.salvar_usuarios()
                return True
        return False

    def listar_usuarios(self):
        return self.usuarios
