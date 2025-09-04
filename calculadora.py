#operações básicas
operacoes_disponiveis = ['SOM: Soma/Subtração', 'MULT: Multiplicação', 'DIV: Divisão', 'DET: Determinante de Matriz']
matrizes_disponiveis = ['2x2', '3x3']

def soma_subtracao():
    valores = input('Inclua todos os valores que devem estar na operação (separe-os por ;): ')
    valores_separados = valores.split(';')
    valor_total = 0

    for valor in valores_separados:
        valor_total+=int(valor)

    return valor_total

def multiplicao():
    valores = input('Inclua todos os valores que devem ser multiplicados (separe-os por ;): ')
    valores_separados = valores.split(';')
    resultado_total = 1

    for valor in valores_separados:
        resultado_total = float(valor) * resultado_total

    return resultado_total

def divisao():
    valores = input('Inclua todos os valores que devem ser divididos (separe-os por ;): ')
    valores_separados = valores.split(';')
    resultado_total = float(valores_separados[0])

    for i, valor in enumerate(valores_separados):
        if i == 0:
            continue
        else:
            resultado_total = resultado_total/float(valor)

    return resultado_total

def ordem_determinante():
    print('Você deseja calcular o determinante de uma matriz de qual ordem?')

    for ordem in matrizes_disponiveis:
        print(f'=> {ordem}') 

    ordem_matriz = input('Digite o primeiro dígo da ordem que você deseja: ')

    return ordem_matriz

def det_2x2():
    linha_1 = input('Digite os dois números da primeira linha (separe-os com ;): ').split(';')
    linha_2 = input('Digite os dois números da segunda linha (separe-os com ;): ').split(';')

    matriz = [[float(linha_1[0]), float(linha_1[1])], [float(linha_2[0]), float(linha_2[1])]]

    det = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    return det

def det_3x3():
    linha_1 = input('Digite os três números da primeira linha (separe-os com ;): ').split(';')
    linha_2 = input('Digite os três números da segunda linha (separe-os com ;): ').split(';')
    linha_3 = input('Digite os três números da terceira linha (separe-os com ;): ').split(';')

    matriz = [[float(linha_1[0]), float(linha_1[1]), float(linha_1[2])], 
              [float(linha_2[0]), float(linha_2[1]), float(linha_2[2])],
              [float(linha_3[0]), float(linha_3[1]), float(linha_3[2])]]

    det_soma = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1]
    det_diferenca = matriz[0][1]*matriz[1][0]*matriz[2][2] + matriz[0][0]*matriz[1][2]*matriz[2][1] + matriz[0][2]*matriz[1][1]*matriz[2][0]
    det = det_soma - det_diferenca

    return det

def menu():
    print('\nDigite qual operação você deseja realizar:\n')

    for operacao in operacoes_disponiveis:
        print(f'=> {operacao}')

    while True:
        decisao = input('\nDigite a sigla da operação (ou "sair" para encerrar): ')
        match decisao.lower():
            case 'som':
                print(soma_subtracao())
            case 'mult':
                print(multiplicao())
            case 'div':
                print(divisao())
            case 'det':
                ordem_escolhida = ordem_determinante()
                match ordem_escolhida:
                    case '2':
                        print(det_2x2())
                    case '3':
                        print(det_3x3())
            case 'sair':
                print('Calculadora finalizada!')
                break
            case _:
                print('\nOpção inválida. Esolha uma operação existente.\n')

menu()