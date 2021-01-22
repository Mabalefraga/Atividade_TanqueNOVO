class Torneira:

    def __init__(self, vazao: float, nome: str):
        self.vazao = vazao
        self.nome = nome

    def modificar_vazao(self, nova_vazao:float):
        self.vazao = nova_vazao
        self.nova_vazao = nova_vazao
        print(f'A vazão foi atualizada para {self.nova_vazao} l/s')


class Tanque:

    def __init__(self, capacidade_maxima: float, capacidade: float):
        
        self.capacidade_max = capacidade_maxima
        self.capacidade_atual = capacidade
        self.historico = []
        self.torneiras_saida = []
        self.torneiras_entrada = []

    def instalar_torneira(self, nova_torneira: Torneira, saida=True)->bool:
        
        if saida == False:
            for torneira in self.torneiras_saida:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_saida.append(nova_torneira)
            print('Nova torneira adicionada com sucesso!')
        else:
            for torneira in self.torneiras_entrada:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_entrada.append(nova_torneira)
            print('Nova torneira instalada com sucesso!')
        return True

    def abrir_torneira(self, nome_torneira, tempo_segundos):
        for torneira in self.torneiras_saida:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual >= torneira.vazao*tempo_segundos:
                    self.capacidade_atual -= torneira.vazao*tempo_segundos
                    print("Água retirada do reservatório :)")
                    return True
                else:
                    self.capacidade_atual = 0
                    print("A água acabou antes do tempo :(")
                    return True
        for torneira in self.torneiras_entrada:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual + torneira.vazao*tempo_segundos <= self.capacidade_max:
                    self.capacidade_atual += torneira.vazao*tempo_segundos
                    print("Água adicionada ao reservatório :)")
                    return True
                else:
                    self.capacidade_atual = self.capacidade_max
                    print("A água acabou transbordando, você desperdiçou água!")
                    return True
        return False

    def imprimir_nome_torneiras(self):
        print("Torneiras:")
        for torneira in self.torneiras_entrada:
            print(f'O nome da torneira é {torneira.nome} e sua vazão é {torneira.vazao} l/s' )
        for torneira in self.torneiras_saida:
            print(f'O nome da torneira é {torneira.nome} e sua vazão é {torneira.vazao} l/s' )

    def recargar_reservatorio(self, recarga):
        if self.capacidade_atual + recarga <= self.capacidade_max:
            self.capacidade_atual += recarga
            print('Tanque recarregado com sucesso')
        else:
            print("A recarga não pode ser concluída")
            
    def remover_torneira(self, nome_torneira, entradaOUsaida=True)->bool:
        for torneira in self.torneiras_saida:
            if nome_torneira is None:
                print("Torneira não encontrada")
                return False               
            else:
                self.torneiras_saida.remove(torneira)
                print("Torneira removida com sucesso!")
                return True
                
        for torneira in self.torneiras_entrada:
            if nome_torneira is None:
                print("Torneira não encontrada")
                return False
            else:
                self.torneiras_entrada.remove(torneira)
                print("Torneira removida com sucesso!")
                return True

    def calcular_tempo_esvaziamento(self, vazao):
        soma_vazao = 0
        for i in self.torneiras_saida:
            soma_vazao += i.vazao
            esvaziamento = self.capacidade_atual / soma_vazao
            print(esvaziamento)
            return True

    def atualizar_torneira(self, procurar_torneira, nova_vazao: Torneira):
        for torneira in self.torneiras_saida:
            if nome_torneira is None:
                print("Torneira não encontrada")
                return False               
            else:
                self.torneiras_saida.remove(torneira)
                print("Torneira removida com sucesso!")
                return True
                
        for torneira in self.torneiras_entrada:
            if nome_torneira is None:
                print("Torneira não encontrada")
                return False
            else:
                self.torneiras_entrada.remove(torneira)
                print("Torneira removida com sucesso!")
                return True
        
        try: 
            for i in self.torneiras_saida:
                if i == procurar_torneira:
                    self.vazao = nova_vazao
                    print("vazão atualizada com sucesso")
                    return True
            for i in self.torneiras_entrada:
                if i == procurar_torneira:
                    self.vazao = nova_vazao
                    print("vazão atualizada com sucesso")
                    return True
        except:
            print("torneira não encontrada")
            return False

    
class Menu():
    def __init__(self):
        self.torneira = Torneira(0, 0)
        self.tanque = Tanque(0,0)

    def imprimir_comandos(self):
        print("")
        print("MENU:")
        print("Escolha uma das opções:")
        print("1 - Instalar torneira;")
        print("2 - Abrir Torneira;")
        print("3 - Imprimir o nomes das torneiras;")
        print("4 - Recerregar Reservatorio;")
        print("5 - Remover torneira;")
        print("6 - Calcular tempo de esvaziamento;")
        print("7 - Atualizar a torneira;")
        print("8 - Sair.")
        print("")
        
    def main(self):

        self.imprimir_comandos()
        capacidade_atual = int(input("Digite quantos litros estão no tanque: "))
        capacidade_total = int(input("Digite qual a capacidade total do tanque: "))
        self.tanque = Tanque(capacidade_total, capacidade_atual)
        opcao = int(input("Digite uma opção acima: "))
        '''for i in range(1,8)'''
        while opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if opcao == 1:
                entradaOUsaida = input("A torneira irá entrada ou saida? (True/False): ")
                if entradaOUsaida == "False":
                    entradaOUsaida = False
                elif entradaOUsaida == "True":
                    entradaOUsaida = True
                vazao = int(input("Digite a vazão da torneira instalada:"))
                nome = input("Digite o nome da torneira que vai ser instalada:")
                self.tanque.instalar_torneira(Torneira(vazao, nome), entradaOUsaida)

            elif opcao == 2:
                nome_torneira = input("Digite o nome da torneira que vai ser aberta:")
                tempo_segundo = int(input("Digite quantos segundos a torneira ficará aberta:"))
                self.tanque.abrir_torneira(nome_torneira, tempo_segundo)

            elif opcao == 3:
                self.tanque.imprimir_nome_torneiras()
            elif opcao == 4:
                recarga = int(input("Digite quantos litros vai ser a recarga:"))
                self.tanque.recargar_reservatorio(recarga)

            elif opcao == 5:
                entradaOUsaida = input("A torneira que vai ser removida é de entrada ou de saida: ")
                if entradaOUsaida == "entrada":
                   entradaOUsaida == True
                elif entradaOUsaida == "saida":
                    entradaOUsaida == False
                nome_torneira = input("Digite o nome da torneira que vai ser removida:")
                self.tanque.remover_torneira(nome_torneira, entradaOUsaida)

            elif opcao == 6:
                vazao = int(input("Digite a vazão que vai esvaziar o tanque:"))
                self.tanque.calcular_tempo_esvaziamento(vazao)

            elif opcao == 7:
                nome_torneira = input("Digite o nome da torneira que vai ser atualizada:")
                vazao = int(input("Digite por qual vazao vai ser atualizada: "))
                self.tanque.atualizar_torneira(nome_torneira, Torneira(nova_vazao))

            self.imprimir_comandos()
            opcao = int(input("Digite uma opção acima: "))
            
if __name__ == "__main__":
    menu = Menu()
    menu.main()
