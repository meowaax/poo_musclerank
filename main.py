from academia import Academia
from instrutor import Instrutor
from aluno import Aluno
from ranking import Ranking

if __name__ == "__main__":
    # Criação da Academia
    academia_top = Academia("Academia Top", "12.345.678/0001-99", "Rua das Flores, 123")

    # Criação do Instrutor vinculado à Academia
    instrutor = Instrutor("Carlos Silva", "123.456.789-00", "1985-06-15", "INST001", academia_top)

    # Criação dos Alunos vinculados ao Instrutor e à Academia
    aluno1 = Aluno("Ana Souza", "987.654.321-00", "2000-04-22", "ALU001", instrutor, academia_top)
    aluno2 = Aluno("João Lima", "567.890.123-45", "1998-03-12", "ALU002", instrutor, academia_top)

    # Inserindo Instrutor e Alunos na Academia
    academia_top.inserir_instrutor(instrutor)
    academia_top.inserir_aluno(aluno1)
    academia_top.inserir_aluno(aluno2)

    # Criando o Ranking e adicionando os participantes
    ranking = Ranking()
    ranking.adicionar_participante(instrutor)
    ranking.adicionar_participante(aluno1)
    ranking.adicionar_participante(aluno2)

    # Criando treinos para os alunos
    aluno1.criar_treino('Treino', 'Alternado', 60)
    aluno2.criar_treino('Treino', 'Alternado', 40)

    # Adicionando exercícios aos treinos do dia
    aluno1.adicionar_exercicio("Supino", "Exercício para o peitoral", 100)
    aluno1.adicionar_exercicio("Agachamento", "Exercício para pernas e glúteos", 150)
    aluno2.adicionar_exercicio("Rosca Direta", "Exercício para bíceps", 120)

    # Concluindo os exercícios do dia para cada aluno
    for exercicio in aluno1.treino_do_dia.exercicios:
        aluno1.concluir_exercicio(exercicio)

    for exercicio in aluno2.treino_do_dia.exercicios:
        aluno2.concluir_exercicio(exercicio)

    # Exibindo o ranking final
    print("\n=== Ranking de Alunos ===")
    ranking.exibir_ranking_alunos()

    print("\n=== Ranking de Instrutores ===")
    ranking.exibir_ranking_instrutores()

    # Exibindo as informações da Academia, incluindo os instrutores e alunos cadastrados
    print("\n=== Informações da Academia ===")
    print(academia_top)

    # Exibindo os alunos vinculados à academia
    print("\n=== Alunos da Academia ===")
    for aluno in academia_top.alunos:
        print(aluno)

    # Exibindo os instrutores vinculados à academia
    print("\n=== Instrutores da Academia ===")
    for instrutor in academia_top.instrutores:
        print(instrutor)
