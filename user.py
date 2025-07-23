import json
import os

class Usuario:
    def __init__(self, nome, email, senha, telefone, endereco, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.tipo = tipo  

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "tipo": self.tipo
        }

class GerenciadorUsuarios:
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