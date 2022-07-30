#Importando as bibliotecas responsáveis
import random
import os

def geracao_de_senha(tam):
    minusc = 'qwertyuiopasdfghjklçzxcvbnm'
    maiusc = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
    numerico = '1234567890'
    caract = '{}[](),.;:/\*-+.^~´`!@#$%&_='

    juncao = minusc + maiusc + numerico + caract

    senha = "".join(random.sample(juncao, tam))

    print(senha) #Exibindo a senha criada na tela para o usuário

    pergunta() #Chamando a função responsável por perguntar ao usuário se ele quer gerar nova senha

def pergunta():
    resp = input("Deseja gerar nova senha? [S/N]")
    tamanho = int(input("Quantos dígitos deve ter sua senha?"))
           
    if (resp == 'S' or resp == 's'):
        geracao_de_senha(tamanho)
    else:
        exit


pergunta()
