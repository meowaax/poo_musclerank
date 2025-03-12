from aluno import Aluno
from instrutor import Instrutor
class Interface:
    def __init__(self, academia, ranking):
        self.academia = academia
        self.ranking = ranking

    def exibir_menu(self):
        print("\n=== MENU ===")
        print("1. Adicionar Aluno")
        print("2. Adicionar Instrutor")
        print("3. Adicionar Exercício ao Treino do Dia")
        print("4. Concluir Exercício")
        print("5. Deletar treino")
        print("6. Exibir Ranking de Alunos")
        print("7. Exibir Ranking de Instrutores")
        print("8. Exibir Informações da Academia")
        print("9. Exibir Alunos da Academia")
        print("10. Exibir Instrutores da Academia")
        print("11. SAIR")

    def executar_opcao(self, opcao):
        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            cpf = input("Digite o CPF do aluno: ")
            data_nascimento = input("Digite a data de nascimento do aluno (DD-MM-YYYY): ")
            matricula = input("Digite a matrícula do aluno: ")
            instrutor_nome = input("Digite o nome do instrutor responsável: ")

            instrutor = next((i for i in self.academia.instrutores if i.nome == instrutor_nome), None)
            if instrutor:
                aluno = Aluno(nome, cpf, data_nascimento, matricula, instrutor, self.academia)
                self.academia.inserir_aluno(aluno)
                self.ranking.adicionar_participante(aluno)
            else:
                print("Instrutor não encontrado!")

        elif opcao == 2:
            nome = input("Digite o nome do instrutor: ")
            cpf = input("Digite o CPF do instrutor: ")
            data_nascimento = input("Digite a data de nascimento do instrutor (DD-MM-YYYY): ")
            matricula = input("Digite o registro do instrutor: ")

            instrutor = Instrutor(nome, cpf, data_nascimento, matricula, self.academia)
            self.academia.inserir_instrutor(instrutor)
            self.ranking.adicionar_participante(instrutor)

        elif opcao == 3:
            aluno_nome = input("Digite o nome do aluno: ")
            aluno = next((a for a in self.academia.alunos if a.nome == aluno_nome), None)

            if aluno:
                nome_exercicio = input("Digite o nome do exercício: ")
                descricao = input("Digite a descrição do exercício: ")
                pontos = int(input("Digite os pontos do exercício: "))
                aluno.adicionar_exercicio(nome_exercicio, descricao, pontos)
            else:
                print("Aluno não encontrado!")

        elif opcao == 4:
            aluno_nome = input("Digite o nome do aluno: ")
            aluno = next((a for a in self.academia.alunos if a.nome == aluno_nome), None)

            if aluno:
                if aluno.treino_do_dia is None or len(aluno.treino_do_dia) == 0:
                    print("Nenhum exercício disponível para concluir.")
                else:
                    print("\nExercícios disponíveis:")
                    for idx, exercicio in enumerate(aluno.treino_do_dia.exercicios, start=1):
                        print(f"{idx}. {exercicio.nome} - {exercicio.descricao} ({exercicio.pontos} pontos)")

                    try:
                        escolha = int(input("Escolha o número do exercício concluído: ")) - 1
                        if 0 <= escolha < len(aluno.treino_do_dia.exercicios):
                            exercicio_concluido = aluno.treino_do_dia.exercicios[escolha]
                            aluno.concluir_exercicio(exercicio_concluido)
                            print("Exercício concluído com sucesso!")
                        else:
                            print("Escolha inválida!")
                    except ValueError:
                        print("Entrada inválida! Por favor, insira um número.")
            else:
                print("Aluno não encontrado!")

        elif opcao == 5:
            aluno_nome = input("Digite o nome do aluno para deletar o treino: ")
            aluno = next((a for a in self.academia.alunos if a.nome == aluno_nome), None)

            if aluno:
                if aluno.treino_do_dia:
                    aluno._treino_do_dia = None  # Remove o treino
                    print(f"Treino do aluno {aluno.nome} foi deletado com sucesso!")
                else:
                    print("O aluno não possui um treino ativo.")
            else:
                print("Aluno não encontrado!")
            
        elif opcao == 6:
            self.ranking.exibir_ranking_alunos()

        elif opcao == 7:
            self.ranking.exibir_ranking_instrutores()

        elif opcao == 8:
            print(self.academia)

        elif opcao == 9:
            print("\n=== Alunos da Academia ===")
            for aluno in self.academia.alunos:
                print(aluno)

        elif opcao == 10:
            print("\n=== Instrutores da Academia ===")
            for instrutor in self.academia.instrutores:
                print(instrutor)

        elif opcao == 11:
            print("Saindo do sistema...")
            return False

        else:
            print("Opção inválida!")
        return True