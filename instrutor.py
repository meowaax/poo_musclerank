from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, registro):
        super().__init__(nome, cpf, data_nascimento)
        self.registro = registro
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        return[str(aluno) for aluno in self.alunos]
