from random import randint
import time 

contadorcli = 0  # contador de clientes da operação
iniciar = 0


abrirloja = 0
while(abrirloja != 1):
    abrirloja = (
        int(input('Deseja abrir a loja? Digite 1 para SIM, 2 para NÃO.\n')))
    if abrirloja == 1:
        print('Realizando abertura de caixa...')
        time.sleep(4)
        print('Caixa aberto.')
    else:
        print('Loja fechada. Não é possivel realizar vendas.')

iniciar = 0
while(iniciar != 1):
    iniciar = int(input('\nIniciar venda? Digite 1 para SIM, 2 para NÃO.\n'))
    if iniciar == 1:
        print('venda iniciada... \n Adicionado Chocolate em Barra 100GR... \n Adicionado Chocolate Quente...\n')
    else:
        print('Sistema reiniciando...')
    dados = {}
    compra = int(
        input('Cliente finalizou a compra? Digite 1 para SIM, 2 para NÃO.\n'))
    if compra == 1:
        nome = input('Qual o nome do cliente? \n')
        telefone = int(input('Qual o telefone do cliente? \n'))
        continuar = int(
            input('Deseja continuar com a loja aberta? Digite 1 para SIM, 2 para NÃO.'))
        dados[nome] = telefone
        if continuar == 1:
            iniciar = 0
        else:
            print('Fechando caixa...')
            time.sleep(5)
            print('caixa fechado.')
            print(f'Os clientes que realizaram a compra hoje foram: ')
            print(dados)

    else:
        iniciar = 0
        print('Venda cancelada. Reiniciando programa...')
