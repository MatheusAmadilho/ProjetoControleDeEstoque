from modulomenu import * #importando todas as funçoes desse modulo para utilizaçao das suas funçoes.


def escreve_arquivo(nome, dados): #vai receber dois parametros, o nome do arquivo(arquivo.json) e a variavel que contém meus dados(arquivo_str).
    arquivo = open(nome, 'w+') #abre o arquivo em modo uptade, ou seja, é possivel escrever e ler no mesmo(+), além de evitar a perde de dados(write).
    arquivo.write(dados) #escreve na nossa variavel(estoque_str) para armazenar os dados. 
    arquivo.close() #fecha o arquivo. 


def cadastro(estoque_atual):      
    produtos = {}
    cabeçalho('Cadastrar produtos.')
    produtos['Nome'] = str(input('Digite o nome do produto: ')).lower().strip()
    for k in estoque_atual:
        if k['Nome'] == produtos['Nome']:
            print('Este produto já está no estoque.')
            return
    produtos['Quantidade'] = float(input('Digite a quantidade do produto a ser inserida no estoque: '))
    produtos['Custo'] = float(input('Digite o preço de custo do produto: '))
    produtos['Venda'] = float(input('Digite o preço de venda do produto: '))
    estoque_atual.append(produtos)
    print(estoque_atual)


def alterar(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')
    cabeçalho('Alterar dados dos produtos cadastrados.')     
    item = input('Digite o nome do item que deseja alterar o cadastro: ').lower().strip()
    for i in estoque_atual:
        if item == i['Nome']:
            tipo = input('Digite Nome, Quantidade, Custo ou Venda, para alterar o nome, quantidade em estoque, preço de custo e preço de venda respectivamente do item: ').lower().strip()
            dado_novo = input('Insira o novo dado: ')    
            if item == i['Nome'] and (tipo == 'nome'):
                    i['Nome'] = dado_novo
            elif item == i['Nome'] and (tipo == 'quantidade'):
                    i['Quantidade'] = dado_novo
            elif item == i['Nome'] and (tipo == 'custo'):
                    i['Custo'] = dado_novo
            elif item == i['Nome'] and (tipo == 'venda'):
                    i['Venda'] = dado_novo
    print(estoque_atual)

def excluir(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')
    cabeçalho('Excluir um produto.')
    excluir = input('Digite o produto que deseja deletar do estoque: ').lower().strip()
    for i in estoque_atual:
        if excluir == i['Nome']:
            estoque_atual.remove(i)
    print(estoque_atual)


def entrada(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')    
    cabeçalho('Registrar entrada de estoque.')
    entrada = input('Digite o nome do item que deseja adicionar estoque: ').lower().strip()
    for i in estoque_atual:
        if entrada == i['Nome']:
            entrada_feita = int(input('Digite quanto foi adicionado ao estoque: '))
            i['Quantidade'] += + entrada_feita
    print(estoque_atual)


def saida(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')
    cabeçalho('Registrar saída de estoque.')
    saida = input('Digite o nome do item que deseja retirar estoque: ').lower().strip()
    for i in estoque_atual:
        if saida == i['Nome']:
            saida_feita = int(input('Digite quanto foi retirado do estoque: '))
            i['Quantidade'] += - saida_feita
    print(estoque_atual)


def quantidade(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')
    cabeçalho('Consultar a quantidade de produtos em estoque: ')
    quantidade_total = 0
    for i in estoque_atual:
        quantidade_total += i['Quantidade']
    print(f'A quantidade total de itens em estoque no momento é: {quantidade_total}')
    quantidade_unica = input('Digite o nome do produto que deseja consultar individualmente ou digite S para sair: ').lower().strip()
    if quantidade_unica == 's':
        return
    quantidade_um = 0
    for k in estoque_atual:
        if quantidade_unica == k['Nome']:
            quantidade_um += k['Quantidade'] 
            print(f'A quantidade do produto {quantidade_unica} é de: {quantidade_um}.')
    print(estoque_atual)


def consulta(estoque_atual):
    cabeçalho('Dados são retornados se o produto estiver no estoque!')
    cabeçalho('Consultar preços de venda e de compra dos produtos em estoque: ')
    custo_total = 0
    venda_total = 0
    for i in estoque_atual:
        custo_total += i['Custo'] * i['Quantidade']
        venda_total += i['Venda'] * i['Quantidade']
    print(f'O preço total de CUSTO do estoque é de: {custo_total}, já o preço total de VENDA do estoque é de: {venda_total}.')
    um_preco = input('Digite o nome do produto que deseja consultar individualmente ou digite S para sair: ').lower().strip()
    if um_preco == 's':
        return
    custo_unico = 0
    venda_unica = 0
    for k in estoque_atual:
        if um_preco == k['Nome']:
            custo_unico = k['Quantidade'] * k['Custo']
            venda_unica = k['Quantidade'] * k['Venda']
            print(f'O preço de CUSTO do produto {um_preco} é de: {custo_unico}, já o preço total de VENDA do produto é de: {venda_unica}.')
    print(estoque_atual)


def encerramento():
    cabeçalho('O sistemas foi encerrado.')
    exit()



