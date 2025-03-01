from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, registro, academia):
        super().__init__(nome, cpf, data_nascimento, academia)
        self._registro = registro
        self._alunos = []
    
    @property
    def registro(self):
        return self._registro
    
    @registro.setter
    def registro(self, registro):
        self._registro = registro
    
    @property
    def alunos(self):
        return self._alunos
    
    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)
    
    def listar_alunos(self):
        return [str(aluno) for aluno in self._alunos]
    
    def __str__(self):
        return f"Instrutor: {self.nome} - Pontuação: {self.pontuacao}"
    