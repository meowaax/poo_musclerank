from datetime import datetime

# Definindo a classe Exercicio
class Exercicio:
    def __init__(self, nome, descricao, pontos):
        self.nome = nome
        self.descricao = descricao
        self.pontos = pontos
        
    def __str__(self):
        return (f"\nNome: {self.nome}"
                f"\nDescrição: {self.descricao}"
                f"\nPontos: {self.pontos}")

# Definindo a classe Treino
class Treino:
    def __init__(self, nome, descricao, duracao, instrutor):
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.instrutor = instrutor
        self.exercicios = []
        self.data_criacao = datetime.now()
    
    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def listar_exercicios(self):
        if not self.exercicios:
            return "Nenhum exercício adicionado."
        return "\n".join(str(exercicio) for exercicio in self.exercicios)

    def calcular_pontos_totais(self):
        return sum(exercicio.pontos for exercicio in self.exercicios)

    def __str__(self):
        return (f"\nTreino: {self.nome}"
                f"\nDescrição: {self.descricao}"
                f"\nDuração: {self.duracao} minutos"
                f"\nInstrutor: {self.instrutor}"
                f"\nCriado em: {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
                f"\n\nExercícios: {self.listar_exercicios()}"
                f"\n\nPontos Totais: {self.calcular_pontos_totais()}")

# Exemplo de uso:

# Criando instâncias de Exercicios
#exercicio1 = Exercicio("Cadeira Flexora", "Posterior de Perna", 10)
#exercicio2 = Exercicio("Cadeira Extensora", "Quadríceps", 10)

# Criando uma instância de Treino
#treino = Treino("Treino de Perna", "Foco em resistência muscular", 80, "Instrutor 1")

# Adicionando exercícios ao treino
#treino.exercicios.append(exercicio1)
#treino.exercicios.append(exercicio2)

# Imprimindo o treino com os exercícios adicionados
#print(treino)