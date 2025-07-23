from menus import MenuSistema


def main():
    """Loop principal para interagir com o menu do sistema Cuidapet.
Parâmetros:
Nenhum
Retorna:
Nenhum
Lógica de processamento:
- Apresenta continuamente um menu ao usuário até que ele opte por sair.
- Lida com três opções: registro do usuário, login e saída do sistema.
- Solicita entradas e executa os métodos de menu associados."""
    menu = MenuSistema()

    while True:
        print("\n=== Bem-vindo ao Cuidapet ===")
        print("1. Cadastrar novo usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu.cadastrar_usuario()
        elif opcao == "2":
            menu.login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
