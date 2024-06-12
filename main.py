from menu import Menu
from gerenciador_tarefas import GerenciarTarefa
from tarefa import Tarefa

def main():
    gerenciador_tarefas = GerenciarTarefa()
    while True:
        opcao = Menu.exibir()

        if opcao == '1':
            codigo = int(input("Digite o código da tarefa: "))
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            tarefa = Tarefa(codigo, titulo, descricao)
            gerenciador_tarefas.adicionar_tarefa(tarefa)
        elif opcao == '2':
            gerenciador_tarefas.visualizar_tarefas()
        elif opcao == '3':
            codigo = int(input("Digite o código da tarefa: "))
            tarefa = gerenciador_tarefas.localizar_tarefa(codigo)
            if tarefa:
                print(f"Tarefa localizada: {tarefa}")
            else:
                print("Tarefa não encontrada.")
        elif opcao == '4':
            gerenciador_tarefas.atualizar_tarefa()
        elif opcao == '5':
            codigo = int(input("Digite o código da tarefa: "))
            gerenciador_tarefas.remover_tarefa(codigo)
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()