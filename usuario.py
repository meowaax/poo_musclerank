class Usuario:
    def __init__(self, nome, cpf, data_nascimento, academia):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido!")
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._pontuacao = 0
        from academia import Academia
        if isinstance(academia, Academia):
            self._academia = academia
        else:
            raise ValueError("O parâmetro 'academia' deve ser uma instância da classe Academia.")

    # novo método estático
    @staticmethod
    def validar_cpf(cpf):
        """Verifica se o CPF possui 11 dígitos numéricos"""
        return isinstance(cpf, str) and cpf.isdigit() and len(cpf) == 11
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def pontuacao(self):
        return self._pontuacao
    
    @pontuacao.setter
    def pontuacao(self, pontos):
        self._pontuacao = pontos
    
    def adicionar_pontos(self, pontos):
        self._pontuacao += pontos
    
    def __str__(self):
        return f"{self._nome} - Pontuação: {self._pontuacao}"
    