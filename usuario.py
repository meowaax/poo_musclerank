
class Usuario:
    def __init__(self, nome, cpf, data_nascimento,academia):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.pontuacao = 0
        from academia import Academia
        if isinstance(academia, Academia):
            self.academia = academia
        else:
            raise ValueError("O parâmetro 'academia' deve ser uma instância da classe Academia.")
    
    def adicionar_pontos(self, pontos):
        self.pontuacao += pontos
    
    def __str__(self):
        return f"{self.nome} - Pontuação: {self.pontuacao}"
    

