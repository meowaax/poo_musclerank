from datetime import datetime

# Definindo a classe Exercicio
class Exercicio:
    def __init__(self, nome, descricao, pontos):
        self._nome = nome
        self._descricao = descricao
        self._pontos = pontos

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, pontos):
        if pontos >= 0:
            self._pontos = pontos
        else:
            raise ValueError("Os pontos devem ser um valor positivo.")
    
    def __str__(self):
        return (f"\nNome: {self._nome}"
                f"\nDescrição: {self._descricao}"
                f"\nPontos: {self._pontos}")

# Definindo a classe Treino
class Treino:
    def __init__(self, instrutor):
        self._instrutor = instrutor
        self._exercicios = []
        self._data_criacao = datetime.now()
    
    @property
    def instrutor(self):
        return self._instrutor

    @instrutor.setter
    def instrutor(self, instrutor):
        self._instrutor = instrutor
    
    @property
    def exercicios(self):
        return self._exercicios

    def adicionar_exercicio(self, exercicio):
        if isinstance(exercicio, Exercicio):
            self._exercicios.append(exercicio)
        else:
            raise ValueError("O objeto deve ser uma instância da classe Exercicio.")

    def listar_exercicios(self):
        if not self._exercicios:
            return "Nenhum exercício adicionado."
        return "\n".join(str(exercicio) for exercicio in self._exercicios)

    def calcular_pontos_totais(self):
        return sum(exercicio.pontos for exercicio in self._exercicios)
    
    def __len__(self):
        return len(self._exercicios)
    
    def __str__(self):
        return (f"\nInstrutor: {self._instrutor}"
                f"\nCriado em: {self._data_criacao.strftime('%d/%m/%Y %H:%M')}"
                f"\n\nExercícios: {self.listar_exercicios()}"
                f"\n\nPontos Totais: {self.calcular_pontos_totais()}")
