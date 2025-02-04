from pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, registro):
        super().__init__(nome, cpf, data_nascimento)
        self.registro = registro
        self.pontuacao = 0

    def __str__(self):
        return f"{self.nome} - Registro: {self.registro}"
