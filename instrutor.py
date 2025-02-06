from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, registro, academia):
        # Agora repassamos o parâmetro 'academia' para o construtor de Usuario
        super().__init__(nome, cpf, data_nascimento, academia)
        self.registro = registro
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        return [str(aluno) for aluno in self.alunos]
    
    def __str__(self):
        return f"Instrutor: {self.nome} - Pontuação: {self.pontuacao}"

