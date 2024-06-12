class Tarefa:

    def __init__(self, codigo, titulo, descricao, status="pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.codigo = codigo

    def __str__(self):
        return f" Título: {self.titulo}, Descricao: {self.descricao}, Status: {self.status} "

    def atualizar(self, titulo, descricao, status=None):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def marcar_concluida(self):
        self.status = "concluída"
