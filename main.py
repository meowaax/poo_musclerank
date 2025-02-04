from instrutor import Instrutor
from aluno import Aluno
from treino import Treino


# exemplo

if __name__ == "__main__":
    instrutor = Instrutor("Carlos Silva", "123.456.789-00", "1985-06-15", "INST001")

    aluno1 = Aluno("Ana Souza", "987.654.321-00", "2000-04-22", "ALU001")
    aluno2 = Aluno("João Lima", "567.890.123-45", "1998-03-12", "ALU002")

    treino1 = Treino("Treino de Cardio", 30, instrutor)
    treino2 = Treino("Treino de Força", 45, instrutor)

    aluno1.adicionar_treino(treino1)
    aluno1.adicionar_treino(treino2)
    aluno2.adicionar_treino(treino1)

    print(f"Treinos de {aluno1.nome}:")
    for treino in aluno1.listar_treinos():
        print(treino)

    print("\nTreinos de João Lima:")
    for treino in aluno2.listar_treinos():
        print(treino)
