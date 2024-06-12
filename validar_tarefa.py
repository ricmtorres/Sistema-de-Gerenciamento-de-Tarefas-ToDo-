class ValidadarTarefa:

    @staticmethod
    def validar(tarefa):
        if tarefa is None:
            raise ValueError("Tarefa não pode ser nulo")
        if tarefa.codigo is None:
            raise ValueError("Código de tarefa não pode ser nulo")
        if tarefa.titulo == "":
            raise ValueError("O titulo não pode ser vazio")
