from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, cpf, data_nascimento, registro):
        super().__init__(nome, cpf, data_nascimento)
        self.registro = registro
