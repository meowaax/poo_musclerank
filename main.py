from instrutor import Instrutor
from aluno import Aluno
from ranking import Ranking


# exemplo

if __name__ == "__main__":
    instrutor = Instrutor("Carlos Silva", "123.456.789-00", "1985-06-15", "INST001")

    aluno1 = Aluno("Ana Souza", "987.654.321-00", "2000-04-22", "ALU001", instrutor)
    aluno2 = Aluno("João Lima", "567.890.123-45", "1998-03-12", "ALU002", instrutor)

    ranking = Ranking()
    ranking.adicionar_participante(instrutor)
    ranking.adicionar_participante(aluno1)
    ranking.adicionar_participante(aluno2)

    aluno1.criar_treino('Treino', 'Alternado', 60)
    aluno2.criar_treino('Treino', 'Alternado', 40)

    # Adicionar treino do dia
    aluno1.adicionar_exercicio("Supino", "Exercício para o peitoral", 100)
    aluno1.adicionar_exercicio("Agachamento", "Exercício para pernas e glúteos", 150)
    aluno2.adicionar_exercicio("Rosca Direta", "Exercício para bíceps", 120)

    # Concluir exercícios
    for exercicio in aluno1.treino_do_dia.exercicios:
        aluno1.concluir_exercicio(exercicio)

    for exercicio in aluno2.treino_do_dia.exercicios:
        aluno2.concluir_exercicio(exercicio)

    # Exibir ranking final
    ranking.exibir_ranking_alunos()
    ranking.exibir_ranking_instrutores()
    
