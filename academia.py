from aluno import Aluno
from instrutor import Instrutor

class Academia:
    def __init__(self, nome_acad, cnpj, local):
        self.__nome_acad = nome_acad
        self.__cnpj = cnpj
        self.__local = local
        self.alunos = []     
        self.instrutores = []

    @property
    def nome_acad(self):
        return self.__nome_acad

    @nome_acad.setter
    def nome_acad(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome_acad = novo_nome
        else:
            raise ValueError("Nome da academia deve ser uma string não vazia.")

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        if isinstance(novo_cnpj, str) and len(novo_cnpj) == 14 and novo_cnpj.isdigit():
            self.__cnpj = novo_cnpj
        else:
            raise ValueError("CNPJ deve ter 14 dígitos numéricos.")

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, novo_local):
        if isinstance(novo_local, str) and len(novo_local) > 0:
            self.__local = novo_local
        else:
            raise ValueError("O local deve ser uma string não vazia.")

    def inserir_aluno(self, aluno):
        try:
            if isinstance(aluno, Aluno):
                self.alunos.append(aluno)
                print(f"Aluno {aluno.nome} inserido com sucesso!")
            else:
                raise TypeError("O objeto informado não é um Aluno válido.")
        except TypeError as e:
            print(f"Erro ao inserir aluno: {e}")

    def remover_aluno(self, aluno):
        try:
            if aluno in self.alunos:
                self.alunos.remove(aluno)
                print(f"Aluno {aluno.nome} removido com sucesso!")
            else:
                raise ValueError("Aluno não encontrado na lista.")
        except ValueError as e:
            print(f"Erro ao remover aluno: {e}")

    def inserir_instrutor(self, instrutor):
        try:
            if isinstance(instrutor, Instrutor):
                self.instrutores.append(instrutor)
                print(f"Instrutor {instrutor.nome} inserido com sucesso!")
            else:
                raise TypeError("O objeto informado não é um Instrutor válido.")
        except TypeError as e:
            print(f"Erro ao inserir instrutor: {e}")

    def remover_instrutor(self, instrutor):
        try:
            if instrutor in self.instrutores:
                self.instrutores.remove(instrutor)
                print(f"Instrutor {instrutor.nome} removido com sucesso!")
            else:
                raise ValueError("Instrutor não encontrado na lista.")
        except ValueError as e:
            print(f"Erro ao remover instrutor: {e}")

    def __str__(self):
        return f"Academia: {self.__nome_acad} (CNPJ: {self.__cnpj}) - Local: {self.__local}"
