# Acredito que a classe Treino deverá conter vários objetos da classe Exercicio

class Exercicio:
    def __init__(self, nome, descricao, pontos):
        self.nome = nome
        self.descricao = descricao
        self.pontos = pontos

    def __str__(self):
        return f"Exercício: {self.nome} - {self.descricao} ({self.pontos} pontos)"