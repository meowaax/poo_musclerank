from datetime import datetime

class Treino:
    def __init__(self, nome, descricao, duracao, pontos, instrutor):
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.pontos = pontos
        self.instrutor = instrutor
        self.exercicios = []
        self.data_criacao = datetime.now()

    def adicionar_exercicio(self, exercicio):
        if not exercicio or not isinstance(exercicio, str):
            print("Erro: O exercício precisa ser um nome válido.")
            return
        
        if exercicio not in self.exercicios:
            self.exercicios.append(exercicio)
        else:
            print(f"O exercício '{exercicio}' já está no treino.")

    def __contains__(self, exercicio):
        return exercicio in self.exercicios

    def listar_exercicios(self):
        if not self.exercicios:
            return "Nenhum exercício adicionado."
        return ", ".join(self.exercicios)

    def __str__(self):
        return (f"\nTreino: {self.nome}"
            f"\nDescrição: {self.descricao}"
            f"\nDuração: {self.duracao} minutos"
            f"\nPontos: {self.pontos}"
            f"\nInstrutor: {self.instrutor}"
            f"\nCriado em: {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
            f"\nExercícios: {self.listar_exercicios()}")

# Exemplo de uso:
treino = Treino("Treino de Perna", "Posterior", 80, 10, "Instrutor 1")

treino.adicionar_exercicio("Cadeira Flexora")

print(treino)