from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.matricula = matricula
        self.treinos = []  
        self.pontuacao = 0

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def listar_treinos(self):
        return [str(treino) for treino in self.treinos]
