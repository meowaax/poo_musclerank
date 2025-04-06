from menu import Menu
from controlador_academia import ControladorAcademia

class Interface:
    def __init__(self, academia, ranking):
        self.controlador = ControladorAcademia(academia, ranking)

    def executar(self):
        while True:
            Menu.exibir()
            opcao = Menu.ler_opcao()

            if opcao == 1:
                self.controlador.adicionar_aluno()
            elif opcao == 2:
                self.controlador.adicionar_instrutor()
            elif opcao == 3:
                self.controlador.adicionar_exercicio()
            elif opcao == 4:
                self.controlador.concluir_exercicio()
            elif opcao == 5:
                self.controlador.deletar_treino()
            elif opcao == 6:
                self.controlador.exibir_ranking_alunos()
            elif opcao == 7:
                self.controlador.exibir_ranking_instrutores()
            elif opcao == 8:
                self.controlador.exibir_dados_academia()
            elif opcao == 9:
                self.controlador.exibir_alunos()
            elif opcao == 10:
                self.controlador.exibir_instrutores()
            elif opcao == 11:
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
