from datetime import datetime

class Treino:
    def __init__(self):
        self.exercicios = []
        self.data_criacao = datetime.now()

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def __contains__(self, exercicio):
        return exercicio in self.exercicios

    def listar_exercicios(self):
        return [str(ex) for ex in self.exercicios]

    def __str__(self):
        return f"Treino: {self.descricao} | Duração: {self.duracao} minutos | Instrutor: {self.instrutor.nome}"
