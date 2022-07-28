import random  # Importa A biblioteca Ramdom para sortear o cliente
from time import sleep
clientes = {}  # Criando Dicionario que irá armazenar os clientes
continuar = True  # Comando para verificar o While

abrirloja = 0
while(abrirloja != 1):
    abrirloja = (int(input('Deseja abrir o caixa ? Digite 1 para SIM, 2 para NÃO.\n')))
    if abrirloja == 1:
        print('Realizando abertura de caixa...')
        sleep(4)
        print('Caixa aberto.')
    else:
        print('Caixa fechado. Não é possivel realizar vendas.')
    
while continuar == True:
# Estrutura que registra o cliente e o número de telefone em um Dicionário
    nomeCliente = input('Infome o nome do cliente: ')
    telefoneCliente = int(input('Informe o telefone do cliente: '))
    clientes[nomeCliente] = telefoneCliente
    cont_registro = input('Deseja continuar registrando clientes? Digite 1 para SIM, 2 para NÃO: ')
# Validador da estrutura de repetição
    if cont_registro == '1':
        continuar = True
    elif cont_registro == '2':
        continuar = False
    else:
        while cont_registro != 'y' and cont_registro != 'n':
            print('Informe Uma Opção valida!')
            cont_registro = input('Deseja continuar registrando clientes? Digite 1 para SIM, 2 para NÃO: ')

# Uso da biblioteca random para sortear o vencedor, Mais em:
'''https://theprogrammingexpert.com/get-random-value-from-dictionary-python/#:~:
text=To%20get%20a%20random%20value%20from%20a%20dictionary,the%20random%20module%20
choice%28%29function%2C%20list%28%29function%20and%20dictionary%20values%28%29function.'''
vencedor_sorteio = random.choice(list(clientes.items()))
# Printando usando o Fstring o item 0 (nome) e o item 1 (telefone) da tupla gerada pelo método random.choice que foi coletada do dicionário
print(f'O Cliente sorteado foi: {vencedor_sorteio[0]}, e seu telefone é :{vencedor_sorteio[1]}')
