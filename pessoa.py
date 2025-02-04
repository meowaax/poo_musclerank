class Pessoa:
    def __init__(self, nome, cpf, data_nascimento, sexo):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"
