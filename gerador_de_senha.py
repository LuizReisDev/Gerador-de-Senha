#Importação das bibliotecas que usaremos
import random
import string
import os


#Declaração da função de gerar a senha
def gerando_senha (len_pass = 8): #Passamos como parâmetro uma quantidade exata de caractere para a senha, caso não for passado nenhum parâmetro ele gerarará uma senha de 8 dígitos
    ascii_options = string.ascii_letters #Variável que guarda as opções de letras em formato de string
    number_options = string.digits #Variável que guarda as opções de dígitos em formato de string
    punt_options = string.punctuation #Variável que guarda as opções de pontuações em formato de string
    options = ascii_options + number_options + punt_options #Variável que vai concatenar todas as variáveis em uma só

    senha_final = ""
    
    for i in range(0, len_pass):
        digito_criado = random.choice(options) #Ele escolhe um dígito e guarda dentro da variavel "digito"
        senha_final = senha_final + digito_criado #Passando o valor do dígito escolhido e guardado dentro da variavel 'digito_criado' para dentro da variável "senha_final"

    return senha_final #Este return executará somente depois que terminar o laço de repetição "for"


#INTERAÇÃO COM O USUÁRIO    
escolha_do_usuário = input("Quantos dígitos você quer que tenha sua senha?\n") #Usuário responde quantos dígitos ele quer que seja gerado e então guardamos na variável "escolha_do_usuário" que é responsável por guardar esta resposta vinda do usuário

#Verificação do que o usuário digitou
if escolha_do_usuário.isdigit(): #Verificamos se o usuário digitou um número ou não. 
    escolha_do_usuário = int(escolha_do_usuário) #Se ele digitou um número, nós forçamos ele ficar inteiro para garantir que ele ficará guardado como inteiro dentro da variável
else:
    print("Entrada inválida!")
    quit()
    
#Chamando a função para gerar senha
#Chamamos a função de gerar a senha de acordo com o valor que o usuário digitou e passamos o "len_pass" com o valor que o usuário digitou.
#A função retornará a senha final que é a senha montada com a quantidade de dígitos que o usuário escolheu. e guardará dentro desta variável "resposta" que acabamos de criar
resposta = gerando_senha(len_pass = escolha_do_usuário)

print(f"Senha gerada:\n{resposta}\n\n")
os.system("pause") #Comando responsável por parar a execução do programa e não fechar a tela até que o usuário aperte alguma tecla
