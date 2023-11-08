'''codigos para correção'''
from crud import *
import time



api = open("./api.json", "r")
objeto = json.load(api)


def corrigir_tipo_pergunta(tipo, pergunta):
    while True:
        try:
            valor = tipo(input(f"{pergunta} "))
            return valor
        except (TypeError, ValueError):
            print("Valor incorreto passado")
def ler_dicionario(valor):
    if type(valor) == dict:
        for key, i in valor.keys():
            print(f"{key} : {valor[i]}")
            ler_dicionario(valor[i])
    elif type(valor) == list:
        for i in range(len(valor)):
            print(f"{i} - {valor[i]}")
            ler_dicionario(valor[i])

def bubble_sort(lista):
    for n in range(len(lista)):
        acumulador = 0
        for j in range(len(lista) - n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)
    return lista

def binary_search(lista,alvo):
    inicio = 0
    fim = len(lista)
    chute = (inicio + fim)//2
    while True:
        if alvo < lista[chute]:
            fim = chute
        elif alvo > lista[chute]:
            inicio = chute
        else:
            break
        chute = (inicio + fim)//2
    return chute

def binary_search_recursivo(lista,alvo,inicio,fim):
    inicio = 0
    fim = len(lista)
    chute = (inicio + fim)//2
    if alvo < lista[chute]:
        fim_novo = chute
        return binary_search(lista,alvo,inicio, fim_novo)
    elif alvo > lista[chute]:
        inicio_novo = chute
        return binary_search(lista,alvo,inicio_novo, fim)
    return chute

def cadastrar_cliente():     
    nome = corrigir_tipo_pergunta(tipo="String", pergunta="Qual seu nome?")
    email = corrigir_tipo_pergunta(tipo="String", pergunta="Qual seu email?")
    cpf = corrigir_tipo_pergunta(tipo="String", pergunta="Qual seu cpf?")
    telefone = corrigir_tipo_pergunta(tipo="String", pergunta="Qual seu telefone?")
    cep = corrigir_tipo_pergunta(tipo="String", pergunta="Qual seu CEP?")
    modelo = corrigir_tipo_pergunta(tipo="String", pergunta="Qual o modelo da sua bicicleta?")
    marca = corrigir_tipo_pergunta(tipo="String", pergunta="Qual sua marca de bicicleta?")
    inserir_em_tabela("clientes", nome, email, cpf, telefone, cep)
    inserir_em_tabela("bicleta", nome, cpf, marca, modelo, cep)

    
def procurar_bicicleta(cpf_cliente):
    valor = consulta_especifica(nome_tabela="clientes", coluna_parametro="cpf" , valor_parametro=cpf_cliente)
    print(valor)
    return valor

def realizar_pergunta(pergunta,afirmacao, negacao):
    conta = input(pergunta).lower()
    tentativa = 0

    while conta != afirmacao and conta != negacao:
        conta = input(f"Resposta inválida, você ainda tem {3 - tentativa} tentativas. Digite {afirmacao}/{negacao}: ").lower()
        tentativa += 1
        if tentativa == 3:
            print("Você excedeu o limite de tentativas. Recomece o processo.")
            break

    return conta

def fazer_login():
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    endereco = input("Digite o seu endereço: ")
    nota_fiscal = input("Digite o número da nota fiscal: ")
    print("Login feito com sucesso!")
    time.sleep(3)
    return email, nome, endereco, nota_fiscal

def criar_conta():
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    endereco = input("Digite o seu endereço: ")
    nota_fiscal = input("Digite o número da nota fiscal: ")
    print("Conta criada com sucesso!")
    time.sleep(3)
    return nome, email, endereco, nota_fiscal

def bem_vindo(nome, bicicleta, endereco, nota_fiscal):
    print(f"Bem-vindo, {nome}!")
    time.sleep(3)
    print(f"A marca da sua bicicleta é {bicicleta['marca']} e o modelo {bicicleta['modelo']}.")
    print(f"Endereço: {endereco}")
    print(f"Número da Nota Fiscal: {nota_fiscal}")

        
api.close()
ler_dicionario(objeto)
