class GerenciarTarefa:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.titulo}' adicionada com sucesso!")

    def visualizar_tarefas(self):
        try:
            if len(self.tarefas) == 0:
                raise ValueError("Nenhuma tarefa cadastrada")
            for idx, tarefa in enumerate(self.tarefas):
                print(f"{idx + 1}. {tarefa}")
        except Exception as e:
            print(f"Erro ao visualizar tarefas: {e}")

    def localizar_tarefa(self, codigo):
        try:
            for tarefa in self.tarefas:
                if tarefa.codigo == codigo:
                    return tarefa
            raise ValueError(f"Tarefa com código {codigo} não encontrada")
        except Exception as e:
            print(f"Erro ao localizar tarefa: {e}")
            return None

    def atualizar_tarefa(self):
        try:
            codigo = int(input("Digite o código da tarefa: "))
            tarefa = self.localizar_tarefa(codigo)
            if tarefa:
                novo_status = input("Novo status (pendente/concluido): ").lower()
                if novo_status == "concluido":
                    tarefa.marcar_concluida()
                else:
                    tarefa.status = novo_status
                print("Status da tarefa atualizado com sucesso.")
            else:
                print("Tarefa não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar a tarefa: {e}")

    def remover_tarefa(self, codigo):
        try:
            tarefa = self.localizar_tarefa(codigo)
            if tarefa:
                self.tarefas.remove(tarefa)
                print(f"Tarefa '{tarefa.titulo}' removida com sucesso!")
            else:
                print("Tarefa não encontrada.")
        except Exception as e:
            print(f"Erro ao remover a tarefa: {e}")

    def validar_status(self, status):
        return status in ["pendente", "concluída"]
