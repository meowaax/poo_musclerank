# Acredito que a classe Treino deverá conter vários objetos da classe Exercicio

class Exercicio:
    def __init__(self, nome, descricao, pontos):
        self.nome = nome
        self.descricao = descricao
        self.pontos = pontos
        
    def __str__(self):
        return (f"\nNome: {self.nome}"
            f"\nDescrição: {self.descricao}"
            f"\nPontos: {self.pontos}")

# Exemplo de uso:
exercicio1 = Exercicio("Cadeira Flexora", "Posterior de Perna", 10)
exercicio2 = Exercicio("Cadeira Extensora", "Quadríceps", 10)
print(exercicio1)
print(exercicio2)