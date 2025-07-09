from user import Usuario, GerenciadorUsuarios
from animal import Animal, GerenciadorAnimais
from pedido import Pedido, GerenciadorPedidos
from editarperfil import EditorPerfil

class MenuSistema:
    def __init__(self):
        self.usuarios = GerenciadorUsuarios()
        self.animais = GerenciadorAnimais()
        self.pedidos = GerenciadorPedidos()
        self.editor = EditorPerfil(self.usuarios)

    def cadastrar_usuario(self):
        print("\n--- Cadastro de Usuário ---")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        tipo = "usuario"

        if self.usuarios.buscar_usuario_por_email(email):
            print("Usuário já cadastrado!")
        else:
            novo_usuario = Usuario(nome, email, senha, telefone, endereco, tipo)
            self.usuarios.adicionar_usuario(novo_usuario)
            print("Usuário cadastrado com sucesso!")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ")
        senha = input("Senha: ")
        usuario = self.usuarios.autenticar_usuario(email, senha)
        if usuario:
            print(f"Bem-vindo(a), {usuario['nome']}!")
            if usuario["tipo"] == "administrador":
                self.menu_administrador()
            else:
                self.menu_usuario(email)
        else:
            print("Credenciais inválidas.")

    def menu_usuario(self, email):
        while True:
            print("\n--- Menu do Usuário ---")
            print("1. Ver animais para adoção")
            print("2. Ver animais para tratamento")
            print("3. Solicitar adoção")
            print("4. Solicitar tratamento")
            print("5. Editar perfil")
            print("6. Sair")
            opcao = input("Escolha: ")

            if opcao == "1":
                self.exibir_animais("adocao")
            elif opcao == "2":
                self.exibir_animais("tratamento")
            elif opcao == "3":
                nome_animal = input("Nome do animal: ")
                self.pedidos.adicionar_pedido(Pedido(email, nome_animal, "adocao"))
            elif opcao == "4":
                nome_animal = input("Nome do animal: ")
                self.pedidos.adicionar_pedido(Pedido(email, nome_animal, "tratamento"))
            elif opcao == "5":
                self.menu_editar_perfil(email)
            elif opcao == "6":
                break
            else:
                print("Opção inválida!")

    def menu_editar_perfil(self, email):
        while True:
            print("\n--- Editar Perfil ---")
            print("1. Nome")
            print("2. Email")
            print("3. Senha")
            print("4. Telefone")
            print("5. Endereço")
            print("6. Voltar")
            escolha = input("Escolha: ")

            if escolha == "1":
                novo = input("Novo nome: ")
                self.editor.editar_nome(email, novo)
            elif escolha == "2":
                novo = input("Novo email: ")
                self.editor.editar_email(email, novo)
                email = novo
            elif escolha == "3":
                novo = input("Nova senha: ")
                self.editor.editar_senha(email, novo)
            elif escolha == "4":
                novo = input("Novo telefone: ")
                self.editor.editar_telefone(email, novo)
            elif escolha == "5":
                novo = input("Novo endereço: ")
                self.editor.editar_endereco(email, novo)
            elif escolha == "6":
                break
            else:
                print("Opção inválida!")

    def exibir_animais(self, tipo):
        animais = self.animais.listar_animais(tipo)
        print(f"\n--- Animais para {tipo} ---")
        if not animais:
            print("Nenhum animal disponível.")
        else:
            for animal in animais:
                print(f"Nome: {animal['nome']} | Espécie: {animal['especie']} | Raça: {animal['raca']} | Idade: {animal['idade']} anos")

    def menu_administrador(self):
        while True:
            print("\n--- Menu do Administrador ---")
            print("1. Cadastrar animal")
            print("2. Remover animal")
            print("3. Ver pedidos")
            print("4. Sair")
            escolha = input("Escolha: ")

            if escolha == "1":
                nome = input("Nome do animal: ")
                especie = input("Espécie: ")
                idade = input("Idade: ")
                raca = input("Raça: ")
                descricao = input("Descrição: ")
                tipo = input("Tipo (adocao/tratamento): ")
                animal = Animal(nome, especie, idade, raca, descricao, tipo)
                self.animais.adicionar_animal(animal)

            elif escolha == "2":
                nome = input("Nome do animal: ")
                tipo = input("Tipo (adocao/tratamento): ")
                if self.animais.remover_animal(nome, tipo):
                    print("Animal removido com sucesso.")
                else:
                    print("Animal não encontrado.")

            elif escolha == "3":
                pedidos = self.pedidos.listar_pedidos()
                print("\n--- Pedidos ---")
                for p in pedidos:
                    print(f"Usuário: {p['usuario_email']} | Animal: {p['animal_nome']} | Tipo: {p['tipo']}")

            elif escolha == "4":
                break
            else:
                print("Opção inválida!")
