from datetime import date

class Treino:
    def __init__(self, descricao, exercicios, duracao, instrutor):
        self.descricao = descricao
        self.exercicios = exercicios
        self.duracao = duracao  # min
        self.instrutor = instrutor
        self.data_criacao = date.today()

    def __str__(self):
        return f"Treino: {self.descricao} | Duração: {self.duracao} minutos | Instrutor: {self.instrutor.nome}"
