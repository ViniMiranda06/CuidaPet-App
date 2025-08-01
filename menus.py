from user import Usuario, GerenciadorUsuarios
from animal import Animal, GerenciadorAnimais
from pedido import Pedido, GerenciadorPedidos
from editarperfil import EditorPerfil

class MenuSistema:
    """
    Classe para gerenciar menus do sistema relacionados a usuários, animais e solicitações em um sistema de adoção e tratamento.
    Parâmetros:
- Nenhum: esta classe é inicializada sem parâmetros externos.
Lógica de processamento:
- Inicializa instâncias de gerenciadores de usuários, animais e solicitações para lidar com as respectivas operações.
- Inclui recursos para registro de usuários, login, edição de perfis e gerenciamento de solicitações.
- Oferece menus operacionais distintos para usuários regulares e administradores, aprimorando a interação do usuário e o gerenciamento do sistema.
    """
    def __init__(self):
        self.usuarios = GerenciadorUsuarios()
        self.animais = GerenciadorAnimais()
        self.pedidos = GerenciadorPedidos()
        self.editor = EditorPerfil(self.usuarios)
        self.pedidos = GerenciadorPedidos()

    def cadastrar_usuario(self):
        """Registra um novo usuário com os detalhes fornecidos, caso o e-mail ainda não esteja em uso.
Parâmetros:
- Nenhum
Retorna:
- Nenhum
Lógica de processamento:
- Solicita ao usuário que insira os detalhes necessários para o registro, como nome, e-mail, senha, número de telefone e endereço.
            - Verifica se o e-mail fornecido já está associado a um usuário existente. Se estiver, exibe uma mensagem indicando que o usuário já está registrado.
- Se o e-mail não for encontrado no banco de dados, cria um novo objeto de usuário e o adiciona ao sistema, confirmando o registro bem-sucedido."""
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
        """Lida com o login e a autenticação do usuário.
Parâmetros:
- Nenhum: este método não aceita parâmetros.
Retorna:
- Nenhum: este método não retorna nenhum valor.
Lógica de processamento:
- Solicita ao usuário que insira seu e-mail e senha para autenticação.
            - Utiliza o método “usuarios.autenticar_usuario” para verificar as credenciais.
- Redireciona para o menu apropriado com base no tipo de usuário (“administrador” ou usuário regular).
- Exibe uma mensagem de boas-vindas se a autenticação for bem-sucedida; caso contrário, exibe uma mensagem de erro para credenciais inválidas."""
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
        """Exibe e gerencia o menu do usuário para operações de adoção e solicitação de tratamento.
Parâmetros:
- e-mail (str): Endereço de e-mail do usuário para personalizar solicitações e edição de perfil.
Retorna:
- Nenhum
Lógica de processamento:
- Exibe continuamente o menu do usuário até que ele opte por sair.
            - Lida com a entrada do usuário para navegar por diferentes opções para visualizar ou solicitar serviços relacionados a animais.
- Suporta a edição do perfil do usuário e gerencia solicitações de adoção ou tratamento com o e-mail fornecido."""
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
                confirmar = input("Tem certeza que deseja sair? (s/N): ").strip().lower()
                if confirmar in ("s", "sim"):
                    break

            else:
                print("Opção inválida!")

    def menu_editar_perfil(self, email):
        """Exibe um menu para editar as informações do perfil do usuário.
Parâmetros:
- e-mail (str): O e-mail atual do usuário cujo perfil será editado.
Retorna:
- Nenhum: Esta função não retorna nenhum valor; ela opera interativamente com o usuário.
        Lógica de processamento:
- Solicita continuamente ao usuário que edite as informações do perfil até que ele escolha “Voltar” (sair).
- Atualiza campos específicos com base nas informações inseridas pelo usuário, como nome, e-mail, senha, telefone e endereço.
- Valida as escolhas do usuário e trata entradas inválidas exibindo uma mensagem apropriada."""
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
        """Exibe uma lista de animais de um tipo específico.
Parâmetros:
- tipo (str): O tipo de animais a exibir (por exemplo, “mamíferos”, “répteis”).
Retorna:
- Nenhum: Esta função imprime o resultado diretamente.
        Lógica de processamento:
- Busca uma lista de animais de uma lista associada com base no tipo especificado.
- Imprime uma lista formatada de animais, mostrando seu nome, espécie, raça e idade.
- Indica se não há animais disponíveis do tipo especificado."""
        animais = self.animais.listar_animais(tipo)
        print(f"\n--- Animais para {tipo} ---")
        if not animais:
            print("Nenhum animal disponível.")
        else:
            for animal in animais:
                print(f"Nome: {animal['nome']} | Espécie: {animal['especie']} | Raça: {animal['raca']} | Idade: {animal['idade']} anos")

    def menu_administrador(self):
        """Fornece uma interface de menu para um administrador gerenciar registros de animais e visualizar solicitações.
Parâmetros:
- Nenhum
Retorna:
- Nenhum
Lógica de processamento:
- Exibe um menu com opções para registrar, remover animais, visualizar solicitações ou sair.
            - Solicita continuamente a entrada do usuário até que a opção de sair seja selecionada.
- Lida com ações com base na escolha do usuário, incluindo interação com os objetos “Animais” e “Pedidos”."""
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
                confirmar = input("Tem certeza que deseja sair? (s/N): ").strip().lower()
                if confirmar in ("s", "sim"):
                    break

            else:
                print("Opção inválida!")
