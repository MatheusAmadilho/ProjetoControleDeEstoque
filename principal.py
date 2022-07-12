from modulomenu import * #importando todas as funçoes desse modulo para criaçao do menu.
from funcoes import * #importando todas as funçoes desse modulo para alteraçao de itens dentro do estoque.
import json #além de ser uma forma de armazemanto, ainda é uma biblioteca com a mesma funçao de um arquivo.txt, usada para persistencia dos dados.
import os  #O módulo OS trás muitas funções para interagir com o sistema de arquivos, facilitando a criaçao do arquivo,json e sua procura no sistema.


file = f'{os.getcwd()}/arquivo.json' #função OS para pesquisar em todos arquivos do PC por um arquivo.json.
if not os.path.isfile(file): #função OS, caso não existe um caminho que leve ao arquivo.json.
    with open('arquivo.json', 'w') as f: #criação do arquivo.json, com opçao de escrever no mesmo, "apelidando" de f"
        f.write(json.dumps([])) #converte o array, objeto Python em um objetivo Json, o array é essencial para o funcionamento do json.
        f.close() #fechamento do arquivo. 


estoque = open('arquivo.json') #variavel que recebe o arquivo.json aberto.
estoque_como_string = estoque.read() #usamos o read nele para transformar o arquivo.json em uma string.json.
estoque_atual = json.loads(estoque_como_string) #usamos o json.loads para transformar essa string em um objeto Python, assim se pode manipular e iterar sobre ele.
estoque.close() #fechamento do arquivo.



while True: 
    resposta = menu(['Cadastrar produtos', 'Alterar dados dos produtos cadastrados', 'Excluir um produto', 'Registrar entrada de estoque', 'Registrar saída de estoque','Consultar a quantidade de produtos em estoque', 'Consultar preços e venda e de compra dos produtos em estoque', 'Sair do sistema'])
    if resposta == 1:
        cadastro(estoque_atual) #a variavel estoque_atual vai começar a receber os inputs por meio de funções moduladas. 
        estoque_str = json.dumps(estoque_atual) #nova variavel para receber o json.dumps, que vai converter a variavel estoque_atual(ObjetoPython) em um string.json.
        escreve_arquivo('arquivo.json', estoque_str) #função para receber dois parametros, o nome do arquivo, e a variavel que possui os dados a serem armazenados.
        print(estoque_atual)
    elif resposta == 2:
        alterar(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    elif resposta == 3:
        excluir(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)  
    elif resposta == 4:
        entrada(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)  
    elif resposta == 5:
        saida(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)  
    elif resposta == 6:
        quantidade(estoque_atual) #não existe a necessidade da funçao de esrecever arquivo, já que serve somente para consulta.
    elif resposta == 7:
        consulta(estoque_atual)
    elif resposta == 8:
        encerramento()
    else:
        print ('ERRO: por favor, digite o número de uma opção do menu: ') #else para caso o numero digitado não esteja entre 1 a 8. 