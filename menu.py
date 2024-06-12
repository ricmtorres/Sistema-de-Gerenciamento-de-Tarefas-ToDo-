class Menu:

    @staticmethod
    def exibir():
        print(f"\n Menu Principal")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Localizar Tarefa")
        print("4. Atualizar Tarefas")
        print("5. Remover Tarefas")
        print("6. Sair")

        opcao = input("Escolha uma opcao: ")
        return opcao
