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
        print("5. Exibir Ranking de Alunos")
        print("6. Exibir Ranking de Instrutores")
        print("7. Exibir Informações da Academia")
        print("8. Exibir Alunos da Academia")
        print("9. Exibir Instrutores da Academia")
        print("10. SAIR")

    def executar_opcao(self, opcao):
        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            cpf = input("Digite o CPF do aluno: ")
            data_nascimento = input("Digite a data de nascimento do aluno (YYYY-MM-DD): ")
            matricula = input("Digite a matrícula do aluno: ")
            instrutor_nome = input("Digite o nome do instrutor responsável: ")

            instrutor = next((i for i in self.academia.instrutores if i.nome == instrutor_nome), None)
            if instrutor:
                aluno = Aluno(nome, cpf, data_nascimento, matricula, instrutor, self.academia)
                self.academia.inserir_aluno(aluno)
                self.ranking.adicionar_participante(aluno)
                print(f"Aluno {nome} adicionado com sucesso!")
            else:
                print("Instrutor não encontrado!")

        elif opcao == 2:
            nome = input("Digite o nome do instrutor: ")
            cpf = input("Digite o CPF do instrutor: ")
            data_nascimento = input("Digite a data de nascimento do instrutor (YYYY-MM-DD): ")
            matricula = input("Digite a matrícula do instrutor: ")

            instrutor = Instrutor(nome, cpf, data_nascimento, matricula, self.academia)
            self.academia.inserir_instrutor(instrutor)
            self.ranking.adicionar_participante(instrutor)
            print(f"Instrutor {nome} adicionado com sucesso!")

        elif opcao == 3:
            aluno_nome = input("Digite o nome do aluno: ")
            aluno = next((a for a in self.academia.alunos if a.nome == aluno_nome), None)

            if aluno:
                nome_exercicio = input("Digite o nome do exercício: ")
                descricao = input("Digite a descrição do exercício: ")
                pontos = int(input("Digite os pontos do exercício: "))
                aluno.adicionar_exercicio(nome_exercicio, descricao, pontos)
                print(f"Exercício {nome_exercicio} adicionado ao treino do dia do aluno {aluno.nome}.")
            else:
                print("Aluno não encontrado!")

        elif opcao == 4:
            aluno_nome = input("Digite o nome do aluno: ")
            aluno = next((a for a in self.academia.alunos if a.nome == aluno_nome), None)

            if aluno:
                if aluno.treino_do_dia and aluno.treino_do_dia.exercicios:
                    print("\nExercícios disponíveis:")
                    for idx, exercicio in enumerate(aluno.treino_do_dia.exercicios, start=1):
                        print(f"{idx}. {exercicio.nome} - {exercicio.descricao} ({exercicio.pontos} pontos)")

                    try:
                        escolha = int(input("Escolha o número do exercício concluído: ")) - 1
                        if 0 <= escolha < len(aluno.treino_do_dia.exercicios):
                            aluno.concluir_exercicio(aluno.treino_do_dia.exercicios[escolha])
                            print("Exercício concluído com sucesso!")
                        else:
                            print("Escolha inválida!")
                    except ValueError:
                        print("Entrada inválida! Por favor, insira um número.")
                else:
                    print("Nenhum exercício disponível para concluir.")
            else:
                print("Aluno não encontrado!")

        elif opcao == 5:
            self.ranking.exibir_ranking_alunos()

        elif opcao == 6:
            self.ranking.exibir_ranking_instrutores()

        elif opcao == 7:
            print(self.academia)

        elif opcao == 8:
            print("\n=== Alunos da Academia ===")
            for aluno in self.academia.alunos:
                print(aluno)

        elif opcao == 9:
            print("\n=== Instrutores da Academia ===")
            for instrutor in self.academia.instrutores:
                print(instrutor)

        elif opcao == 10:
            print("Saindo do sistema...")
            return False

        else:
            print("Opção inválida!")
        return True