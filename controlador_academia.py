class ControladorAcademia:
    def __init__(self, academia, ranking):
        self.academia = academia
        self.ranking = ranking

    def adicionar_aluno(self):
        from aluno import Aluno

        nome = input("Digite o nome do aluno: ")
        cpf = input("Digite o CPF do aluno: ")
        data_nascimento = input("Digite a data de nascimento (DD-MM-YYYY): ")
        matricula = input("Digite a matrícula: ")
        instrutor_nome = input("Nome do instrutor responsável: ")

        instrutor = next((i for i in self.academia.instrutores if i.nome == instrutor_nome), None)
        if instrutor:
            aluno = Aluno(nome, cpf, data_nascimento, matricula, instrutor, self.academia)
            self.academia.inserir_aluno(aluno)
            self.ranking.adicionar_participante(aluno)
        else:
            print("Instrutor não encontrado.")

    def adicionar_instrutor(self):
        from instrutor import Instrutor

        nome = input("Digite o nome do instrutor: ")
        cpf = input("Digite o CPF do instrutor: ")
        data_nascimento = input("Digite a data de nascimento (DD-MM-YYYY): ")
        registro = input("Digite o registro do instrutor: ")

        instrutor = Instrutor(nome, cpf, data_nascimento, registro, self.academia)
        self.academia.inserir_instrutor(instrutor)
        self.ranking.adicionar_participante(instrutor)

    def adicionar_exercicio(self):
        nome_aluno = input("Digite o nome do aluno: ")
        aluno = next((a for a in self.academia.alunos if a.nome == nome_aluno), None)

        if aluno:
            nome_exercicio = input("Digite o nome do exercício: ")
            descricao = input("Digite a descrição do exercício: ")
            pontuacao = int(input("Digite a quantidade de pontos: "))

            aluno.adicionar_exercicio(nome_exercicio, descricao, pontuacao)
        else:
            print("Aluno não encontrado.")

    def concluir_exercicio(self):
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
                    else:
                        print("Escolha inválida!")
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número.")
        else:
            print("Aluno não encontrado!")

    def deletar_treino(self):
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

    def exibir_ranking_alunos(self):
        self.ranking.exibir_ranking_alunos()

    def exibir_ranking_instrutores(self):
        self.ranking.exibir_ranking_instrutores()

    def exibir_dados_academia(self):
        print(self.academia)

    def exibir_alunos(self):
        print("\n=== Alunos da Academia ===")
        for aluno in self.academia.alunos:
            print(aluno)

    def exibir_instrutores(self):
        print("\n=== Instrutores da Academia ===")
        for instrutor in self.academia.instrutores:
            print(instrutor)
