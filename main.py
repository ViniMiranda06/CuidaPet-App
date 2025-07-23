from menus import MenuSistema


def main():
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