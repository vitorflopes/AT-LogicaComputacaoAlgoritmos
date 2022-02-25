RED = "\033[1;41m"
GREEN = "\033[0;32m"
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"
CYAN  = "\033[1;36m"

def teste_int (msg):
    while True:
        try:
            num = int (input (msg))
            break
        except (ValueError or TypeError):
            print (RED + "Erro! Digite um número inteiro válido" + RESET)
    return num

def teste_float (msg):
    while True:
        try:
            num = float (input (msg))
            break
        except (ValueError or TypeError):
            print (RED + "Erro! Digite um número" + RESET)
    return num

def posição_conta (lista_contas, num_conta):
    cont = -1
    while True: #pode usar um for
        cont = cont + 1
        try: # com for, n usar mais try
            lista_contas[cont].index(num_conta)
            break
        except (ValueError):
            continue
    return (cont)

def clientes_negativos (lista_contas):
    for i in range (len (lista_contas)):
        if (lista_contas [i][2] < 0):
            print (lista_contas [i][0:3])

def clientes_maior_que (lista_contas, num_maior):
    for i in range (len (lista_contas)):
        if (lista_contas [i][2] > num_maior):
            print (lista_contas [i][0:3])

def listar_contas (lista_contas):
    for i in range (len (lista_contas)):
        print (lista_contas [i][0:3])

def grava_contas (lista_contas):
    with open("contas.txt", "w") as arq:
        for lista_conta in lista_contas:
            arq.write(str(lista_conta[0]) + ";" + str(lista_conta[1]) + ";" + str(lista_conta[2]) + "\n")
    print(GREEN + "Alterações gravadas com sucesso!" + RESET)

def linha (tam = 18):
    print (CYAN + "=-" * tam + "=" + RESET)

def cabeçalho (txt):
    linha ()
    print (BLUE + txt.center(36) + RESET)
    linha ()

def opçoes_menu ():
    cabeçalho ("MENU")
    print("[1] Inclusão de Conta\n[2] Alteração de Saldo\n[3] Excluir Conta\n[4] Relatórios\n[5] Sair do Sistema")

def opçoes_menu_relatorio ():
    print ("[1] Listar clientes com saldo negativo\n[2] Listar clientes que têm saldo acima de um determinado valor\n[3] Listar todas as contas")

def txt_para_lista (lista_contas):
    with open("contas.txt", "r") as arq:
        linha = arq.readline()
        while (linha != ""):
            linha = linha.strip("\n")
            linha = linha.split(";")
            linha[0], linha[2] = int(linha[0]), float(linha[2])
            lista_contas.append(linha)
            linha = arq.readline()
    return lista_contas

def add_conta (lista_contas):
    while True:
        num_conta = teste_int ("Digite o número da conta que deseja criar: ")
        if (num_conta in (x[0] for x in lista_contas)):
            print (RED + "Erro! Número da conta já existe" + RESET)
        else:
            break
    while True:
        nome_conta = input ("Digite o nome do proprietário da conta: ")
        if ((len(nome_conta.split())) < 2):
            print (RED + "Erro! O nome deve conter no mínimo dois nomes" + RESET)
        else:
            break
    while True:
        saldo_conta = teste_float ("Digite o saldo da conta: ")
        if (saldo_conta < 0):
            print (RED + "Erro! O saldo da conta não pode ser negativo" + RESET)
        else:
            break
    nova_conta = [num_conta] + [nome_conta] + [saldo_conta]
    lista_contas.append (nova_conta)
    print (GREEN + "Conta criada com sucesso!" + RESET)
    return (lista_contas)

def alterar_saldo (lista_contas):
    while True:
        num_conta = teste_int ("Digite o número da conta que deseja alterar o saldo: ")
        if (num_conta not in (x[0] for x in lista_contas)): # usar posição conta
            print (RED + "Erro! Número da conta inexistente" + RESET)
        else:
            break
    credito_debito = teste_float ("Digite o valor que deseja creditar ou debitar da conta: ")
    linha_conta = posição_conta (lista_contas, num_conta)
    lista_contas [linha_conta][2] = (lista_contas [linha_conta][2] + credito_debito)
    print (GREEN + "Saldo alterado com sucesso!" + RESET)
    return (lista_contas)

def excluir_conta (lista_contas):
    while True:
        cert = 1
        num_conta = teste_int ("Digite o número da conta que deseja excluir: ")
        if (num_conta not in (x[0] for x in lista_contas)): # usar posição conta
            print (RED + "Erro! Número da conta inexistente" + RESET)
            cert = 0
        elif (cert == 1):
            linha_conta = posição_conta (lista_contas, num_conta)
            if (lista_contas [linha_conta][2] != 0):
                print (RED + "Erro! A conta precisa estar com o saldo zerada para exclusão" + RESET)
            else:
                break
    for lista_conta in lista_contas: # remover apartir da posição
        if (lista_conta [0] == num_conta):
            lista_contas.remove (lista_conta)
    print (GREEN + "Conta excluida com sucesso!" + RESET)
    return (lista_contas)

def relatorios (lista_contas):
    while True:
        opçoes_menu_relatorio ()
        escolha_relatorio = teste_int ("Digite uma opção do Menu Relatório: ")
        if (escolha_relatorio == 1):
            cabeçalho ("Clientes com saldo negativo")
            clientes_negativos (lista_contas)
            break
        elif (escolha_relatorio == 2):
            cabeçalho ("Clientes com saldo acima de um determinado valor")
            num_maior = teste_float ("Digite um valor para listar as contas com saldo superior: ")
            clientes_maior_que (lista_contas, num_maior)
            break
        elif (escolha_relatorio == 3):
            cabeçalho ("Todas as contas")
            listar_contas (lista_contas)
            break
        else:
            print ()
            print (RED + "Erro! Digite um valor válido" + RESET)
            print ()

lista_contas = []
lista_contas = txt_para_lista (lista_contas)
while True:
    opçoes_menu ()
    escolha = teste_int ("Digite uma opção do MENU: ")
    if (escolha == 1):
        cabeçalho ("Inclusão de Conta")
        add_conta (lista_contas)
    elif (escolha == 2):
        cabeçalho ("Alteração de Saldo")
        alterar_saldo (lista_contas)
    elif (escolha == 3):
        cabeçalho ("Excluir Conta")
        excluir_conta (lista_contas)
    elif (escolha == 4):
        cabeçalho ("Relatórios")
        relatorios (lista_contas)
    elif (escolha == 5):
        cabeçalho ("Saída do Sistema")
        grava_contas (lista_contas)
        break
    else:
        print (RED + "Erro! Digite um número das opções do menu" + RESET)