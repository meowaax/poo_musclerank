class Menu:
    @staticmethod
    def exibir():
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

    @staticmethod
    def ler_opcao():
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
