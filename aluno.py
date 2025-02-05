from usuario import Usuario
from instrutor import Instrutor
from treino_exercicio import Treino, Exercicio

class Aluno(Usuario):
    def __init__(self, nome, cpf, data_nascimento, matricula, instrutor):
        super().__init__(nome, cpf, data_nascimento)
        if not isinstance(instrutor, Instrutor):
            raise ValueError('O instrutor deve estar registrado no sistema.')
        self.instrutor = instrutor
        self.instrutor.adicionar_aluno(self)
        self.matricula = matricula
    
    def criar_treino(self, nome, descricao, duracao):
        self.treino_do_dia = Treino(nome, descricao, duracao, self.instrutor)
        
    def adicionar_exercicio(self, nome, descricao, pontos):
        if self.treino_do_dia:
            exercicio = Exercicio(nome, descricao, pontos)
            self.treino_do_dia.adicionar_exercicio(exercicio)
        else:
            print('Você precisa criar um treino primeiro.')

    def concluir_exercicio(self, exercicio):
        if exercicio in self.treino_do_dia.exercicios:
            self.adicionar_pontos(exercicio.pontos)
            self.instrutor.adicionar_pontos(exercicio.pontos // 2)
            print(f"{self.nome} concluiu o exercício: {exercicio.nome} e ganhou {exercicio.pontos} pontos!")
        else:
            print(f"Exercício {exercicio.nome} não faz parte do treino do dia!")
    
    def __str__(self):
        return f"Aluno: {self.nome} - Pontuação: {self.pontuacao}"
