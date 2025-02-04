class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.pontuacao = 0

    
    def adicionar_pontos(self, pontos):
        self.pontuacao += pontos
    
    def __str__(self):
        return f"{self.nome} - Pontuação: {self.pontuacao}"
