from instrutor import Instrutor
from aluno import Aluno
from treino_exercicio import Exercicio
from ranking import Ranking
from academia import Academia
from interface import Interface


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

# Loop interativo
menu = Interface(academia_top, ranking)
executando = True

while executando:
    menu.exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        executando = menu.executar_opcao(opcao)
    except ValueError:
        print("Por favor, insira um número válido.")
