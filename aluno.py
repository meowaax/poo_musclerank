from usuario import Usuario
from treino import Treino
from exercicio import Exercicio

class Aluno(Usuario):
    def __init__(self, nome, cpf, data_nascimento, matricula, instrutor):
        super().__init__(nome, cpf, data_nascimento)
        self.matricula = matricula
        self.instrutor = instrutor
        self.treino_do_dia = Treino()  

    def adicionar_exercicio(self, nome, descricao, pontos):
        exercicio = Exercicio(nome, descricao, pontos)
        self.treino_do_dia.adicionar_exercicio(exercicio)

    def concluir_exercicio(self, exercicio):
        if exercicio in self.treino_do_dia.exercicios:
            self.adicionar_pontos(exercicio.pontos)
            self.instrutor.adicionar_pontos(exercicio.pontos // 2)
            print(f"{self.nome} concluiu o exercício: {exercicio.nome} e ganhou {exercicio.pontos} pontos!")
        else:
            print(f"Exercício {exercicio.nome} não faz parte do treino do dia!")
