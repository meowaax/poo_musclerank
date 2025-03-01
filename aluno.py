from usuario import Usuario
from instrutor import Instrutor
from treino_exercicio import Treino, Exercicio

class Aluno(Usuario):
    def __init__(self, nome, cpf, data_nascimento, matricula, instrutor, academia):
        super().__init__(nome, cpf, data_nascimento, academia)
        if not isinstance(instrutor, Instrutor):
            raise ValueError('O instrutor deve estar registrado no sistema.')
        self._instrutor = instrutor
        self._instrutor.adicionar_aluno(self)
        self._matricula = matricula
        self._treino_do_dia = Treino(instrutor)
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    @property
    def instrutor(self):
        return self._instrutor
    
    @property
    def treino_do_dia(self):
        return self._treino_do_dia
    
    def adicionar_exercicio(self, nome, descricao, pontos):
        if self._treino_do_dia:
            exercicio = Exercicio(nome, descricao, pontos)
            self._treino_do_dia.adicionar_exercicio(exercicio)
        else:
            print('Você precisa criar um treino primeiro.')

    def concluir_exercicio(self, exercicio):
        if exercicio in self._treino_do_dia.exercicios:
            self.adicionar_pontos(exercicio.pontos)
            self._instrutor.adicionar_pontos(exercicio.pontos // 2)
            print(f"{self.nome} concluiu o exercício: {exercicio.nome} e ganhou {exercicio.pontos} pontos!")
        else:
            print(f"Exercício {exercicio.nome} não faz parte do treino do dia!")
    
    def __str__(self):
        return f"Aluno: {self.nome} - Pontuação: {self.pontuacao}"
    