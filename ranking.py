class Ranking:
    def __init__(self):
        self.ranking_alunos = []
        self.ranking_instrutores = []

    def adicionar_participante(self, usuario):
        if usuario.__class__.__name__ == "Aluno":
            self.ranking_alunos.append(usuario)
        elif usuario.__class__.__name__ == "Instrutor":
            self.ranking_instrutores.append(usuario)

    def exibir_ranking_alunos(self):
        ranking_ordenado = sorted(self.ranking_alunos, key=lambda x: x.pontuacao, reverse=True)
        print("\nRanking de Alunos:")
        for i, aluno in enumerate(ranking_ordenado, start=1):
            print(f"{i}. {aluno}")

    def exibir_ranking_instrutores(self):
        ranking_ordenado = sorted(self.ranking_instrutores, key=lambda x: x.pontuacao, reverse=True)
        print("\nRanking de Instrutores:")
        for i, instrutor in enumerate(ranking_ordenado, start=1):
            print(f"{i}. {instrutor}")
