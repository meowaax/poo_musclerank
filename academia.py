
from aluno import Aluno
from instrutor import Instrutor

class Academia:
    def __init__(self, nome_acad, cnpj, local):
        self.nome_acad = nome_acad
        self.cnpj = cnpj
        self.local = local
        self.alunos = []     
        self.instrutores = []
        # self.pontuacao_total = Aqui ele deve conter a somatoria de todos os pontos. 

    def inserir_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} inserido com sucesso!")
        else:
            print("O objeto informado não é um Aluno válido.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno.nome} removido com sucesso!")
        else:
            print("Aluno não encontrado na lista.")

    def inserir_instrutor(self, instrutor):
        if isinstance(instrutor, Instrutor):
            self.instrutores.append(instrutor)
            print(f"Instrutor {instrutor.nome} inserido com sucesso!")
        else:
            print("O objeto informado não é um Instrutor válido.")

    def remover_instrutor(self, instrutor):
        if instrutor in self.instrutores:
            self.instrutores.remove(instrutor)
            print(f"Instrutor {instrutor.nome} removido com sucesso!")
        else:
            print("Instrutor não encontrado na lista.")

    def __str__(self):
        return f"Academia: {self.nome_acad} (CNPJ: {self.cnpj}) - Local: {self.local}"