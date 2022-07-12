def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite o número de uma opção do menu.')
            continue
        except (KeyboardInterrupt):
            print('Usuario não digitou um número do menu')
            return 0
        else:
            return n
        

def linha(tam=60):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu(lista):
    cabeçalho("CONTROLE DE ESTOQUE")
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Escolha a função desejada: ')
    return opc