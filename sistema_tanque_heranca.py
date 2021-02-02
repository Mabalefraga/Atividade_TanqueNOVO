class Torneira(object):
    def __init__(self, vazao: float, nome: str):
        self.vazao = vazao
        self.nome = nome

    def modificar_vazao(self, nova_vazao:float):
        self.vazao = nova_vazao

class Torneiras_Saida(Torneira):
    def __init__(self, torneiras_saida):
        super().__init__(vazao = float, nome = str)
        self.torneiras_saida = []

    def vazao_saida(self):
        self.vazao = vazao * -1

    def instalar_torneira(self,nova_torneira: Torneira, saida=True)->bool:
        if saida == False:
            for torneira in self.torneiras_saida:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_saida.append(nova_torneira)
            print('Nova torneira de saida adicionada com sucesso!')  
        return True

    def remover_torneira(self, nome_torneira):
        for torneira in self.torneiras_saida:
            if nome_torneira == torneira.nome:
                if nome_torneira is None:
                    print("Torneira não encontrada")
                    return False               
                else:
                    self.torneiras_saida.remove(torneira)
                    print("Torneira removida com sucesso!")
                    return True

    def atualizar_torneira(self, nome_torneira, vazao):
        try: 
            for torneira in self.torneiras_saida:
                if torneira.nome == torneira.nome:
                    torneira.vazao = vazao
                    return True
        except:
            return False


class Torneiras_Entrada(Torneira):
    def __init__(self, torneiras_entrada):
        super().__init__(vazao = float, nome = str)
        self.torneiras_entrada = [] 

    def vazao_entrada(self):
        self.vazao = vazao

    def instalar_torneira(self,nova_torneira: Torneira, saida=True)->bool:
        if saida == False:
            pass
        else:
            for torneira in self.torneiras_entrada:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_entrada.append(nova_torneira)
            print('Nova torneira de entrada adicionada com sucesso!')
        return True

    def remover_torneira(self, nome_torneira):
        for torneira in self.torneiras_entrada:
            if nome_torneira is None:
                print("Torneira não encontrada")
                return False
            else:
                self.torneiras_entrada.remove(torneira)
                print("Torneira removida com sucesso!")
                return True
    
    def atualizar_torneira(self, nome_torneira, vazao):
        try: 
            for torneira in self.torneiras_entrada:
                if torneira.nome == torneira.nome:
                    torneira.vazao = vazao
                    return True
        except:
            return False

class Tanque:

    def __init__(self, capacidade_maxima: float, capacidade: float):
        self.capacidade_max = capacidade_maxima
        self.capacidade_atual = capacidade
        self.historico = []
        self.list_torneiras_saida = []
        self.list_torneiras_entrada = []

    def addTorneira_entrada(self, nova_torneira = Torneira):
        for torneira in self.list_torneiras_entrada:
            if nova_torneira.nome == torneira.nome:
                return False
        self.list_torneiras_entrada.append(nova_torneira)
    
    def addTorneira_saida(self, nova_torneira = Torneira):
        for torneira in self.list_torneiras_saida:
            if nova_torneira.nome == torneira.nome:
                return False
        self.list_torneiras_saida.append(nova_torneira)

    def remvTorneira_entrada(self,nome_torneira):
        for torneira in self.list_torneiras_entrada:
            if nome_torneira is None:
                return False
            else:
                self.list_torneiras_entrada.remove(torneira)
                return True

    def remvTorneira_saida(self,nome_torneira):
        for torneira in self.list_torneiras_saida:
            if nome_torneira is None:
                return False
            else:
                self.list_torneiras_saida.remove(torneira)
                return True

    def abrir_torneira(self, nome_torneira, tempo_segundos, entradaOUsaida):
        if entradaOUsaida == True:
            for torneira in self.list_torneiras_entrada:
                if nome_torneira == torneira.nome:
                    if torneira.nome == torneira.nome:
                        if self.capacidade_atual + torneira.vazao*tempo_segundos <= self.capacidade_max:
                            self.capacidade_atual += torneira.vazao*tempo_segundos
                            print("Torneira de entrada:Água adicionada ao reservatório :)")
                            print("O tanque possui", self.capacidade_atual,"litros.")
                            return True
                        else:
                            self.capacidade_atual = self.capacidade_max
                            print("Torneira de entrada:A água acabou transbordando, você desperdiçou água!")
                            return True
        else:
            for torneira in self.list_torneiras_saida:
                if torneira.nome == torneira.nome:
                    if self.capacidade_atual >= torneira.vazao*tempo_segundos:
                        self.capacidade_atual -= torneira.vazao*tempo_segundos
                        print("Torneira de saida: Água retirada do reservatório :)")
                        print("O tanque possui", self.capacidade_atual,"litros.")
                        return True
                    else:
                        self.capacidade_atual = 0
                        print("Torneira de saida: A água acabou antes do tempo :(")
                        return True
            return False            
        
    def recargar_reservatorio(self, recarga):
        if self.capacidade_atual + recarga <= self.capacidade_max:
            self.capacidade_atual += recarga
            print('Tanque recarregado com sucesso')
            print("O tanque possui", self.capacidade_atual,"litros.")
        else:
            print("A recarga não pode ser concluída")
            
    def calcular_tempo_esvaziamento(self, nome_torneira):
        soma_vazao = 0
        for torneira in self.list_torneiras_saida:
            if nome_torneira == torneira.nome:
                if torneira.vazao == torneira.vazao:
                    soma_vazao += torneira.vazao
                    esvaziamento = self.capacidade_atual / soma_vazao
                    print(f"Demorou {esvaziamento} segundos para esvaziar o tanque.")
                    return True
    
    def atualizar_torneira(self, nome_torneira, vazao, entradaOUsaida):
        if entradaOUsaida == True:
            try: 
                for torneira in self.list_torneiras_entrada:
                    if torneira.nome == torneira.nome:
                        torneira.vazao = vazao
                        print("Vazão da torneira de entrada atualizada com sucesso")
                        print(f'O nome da torneira de entrada é {torneira.nome} e sua vazão agora é {torneira.vazao} l/s' )
                        return True
            except:
                print("Torneira não encontrada")
                return False
        else:
            try: 
                for torneira in self.list_torneiras_saida:
                    if torneira.nome == torneira.nome:
                        torneira.vazao = vazao
                        print("Vazão  da torneira de saida atualizada com sucesso")
                        print(f'O nome da torneira de saida é {torneira.nome} e sua vazão agora é {torneira.vazao} l/s')
                        return True
            except:
                print("Torneira não encontrada")
                return False
        
    def imprimir_nome_torneiras(self):
        print("Torneiras:")
        for torneira in self.list_torneiras_entrada:
            print(f'O nome da torneira de entrada é {torneira.nome} e sua vazão é {torneira.vazao} l/s' )
        for torneira in self.list_torneiras_saida:
            print(f'O nome da torneira de saida é {torneira.nome} e sua vazão é {torneira.vazao} l/s' )

class Menu():
    def __init__(self):
        self.torneira = Torneira(0, 0)
        self.torneira_entrada =  Torneiras_Entrada(Torneira)
        self.torneira_saida =  Torneiras_Saida(Torneira)
        self.tanque = Tanque(0,0)

    def imprimir_opcao(self):
        print("")
        print("1 - Torneira de Entrada")
        print("2 - Torneira de Saida")
        print("")

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
        capacidade_atual = int(input("Digite quantos litros estão no tanque: "))
        capacidade_total = int(input("Digite qual a capacidade total do tanque: "))
        self.tanque = Tanque(capacidade_total, capacidade_atual)
        self.imprimir_comandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao in [1, 2, 3, 4, 5, 6, 7, 8]:
            if opcao == 1:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                while opcao in [1, 2]:
                    if opcao == 1: 
                        vazao = int(input("Digite a vazão da torneira instalada:"))
                        nome = input("Digite o nome da torneira que vai ser instalada:")
                        entradaOUsaida = True
                        self.torneira_entrada.instalar_torneira(Torneira(vazao, nome), entradaOUsaida)
                        self.tanque.addTorneira_entrada(Torneira(vazao, nome))
                        break
                    elif opcao == 2:
                        vazao = int(input("Digite a vazão da torneira instalada:"))
                        nome = input("Digite o nome da torneira que vai ser instalada:")
                        entradaOUsaida = False
                        self.torneira_saida.instalar_torneira(Torneira(vazao, nome), entradaOUsaida)
                        self.tanque.addTorneira_saida(Torneira(vazao, nome))
                        break

            elif opcao == 2:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                if opcao == 1: 
                    nome_torneira = input("Digite o nome da torneira que vai ser aberta:")
                    tempo_segundo = int(input("Digite quantos segundos a torneira ficará aberta:"))
                    entradaOUsaida = True
                    self.tanque.abrir_torneira(nome_torneira, tempo_segundo, entradaOUsaida)
                elif opcao == 2:
                    nome_torneira = input("Digite o nome da torneira que vai ser aberta:")
                    tempo_segundo = int(input("Digite quantos segundos a torneira ficará aberta:"))
                    entradaOUsaida = False
                    self.tanque.abrir_torneira(nome_torneira, tempo_segundo, entradaOUsaida)

            elif opcao == 3:
                self.tanque.imprimir_nome_torneiras()
                   
            elif opcao == 4:
                recarga = int(input("Digite quantos litros vai ser a recarga:"))
                self.tanque.recargar_reservatorio(recarga)

            elif opcao == 5:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                print("")
                while opcao in [1, 2]:
                    if opcao == 1: 
                        nome_torneira = input("Digite o nome da torneira que vai ser removida:")
                        self.torneira_entrada.remover_torneira(nome_torneira)
                        self.tanque.remvTorneira_entrada(nome_torneira)
                        break
                    elif opcao == 2:
                        nome_torneira = input("Digite o nome da torneira que vai ser removida:")
                        self.torneira_saida.remover_torneira(nome_torneira)
                        self.tanque.remvTorneira_saida(nome_torneira)
                        break

            elif opcao == 6:
                print("P.S: O tanque só será esvaziado se tiver uma torneira de sai")
                nome = input("Digite o nome da torneira que vai esvaziar o tanque:") 
                self.tanque.calcular_tempo_esvaziamento(nome)

            elif opcao == 7:
                self.imprimir_opcao()
                opcao = int(input("Digite uma opção acima: "))
                while opcao in [1, 2]:
                    if opcao == 1:
                        nome_torneira = input("Digite o nome da torneira que vai ser atualizada:")
                        vazao_torneira = int(input("Digite por qual vazao vai ser atualizada: "))
                        entradaOUsaida = True
                        self.tanque.atualizar_torneira(nome_torneira, vazao_torneira, entradaOUsaida)
                        self.torneira_entrada.atualizar_torneira(nome_torneira, vazao_torneira)
                        break
                    elif opcao == 2:    
                        nome_torneira = input("Digite o nome da torneira que vai ser atualizada:")
                        vazao_torneira = int(input("Digite por qual vazao vai ser atualizada: "))
                        entradaOUsaida = False
                        self.tanque.atualizar_torneira(nome_torneira, vazao_torneira, entradaOUsaida)
                        self.torneira_saida.atualizar_torneira(nome_torneira, vazao_torneira)
                        break

            elif opcao == 8:
                exit()
            
            print(" ")
            print("############################")
            self.imprimir_comandos()
            opcao = int(input("Digite uma opção acima: "))
            
if __name__ == "__main__":
    menu = Menu()
    menu.main()
