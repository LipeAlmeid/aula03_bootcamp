# Exercicio 1 - Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário

quantidade = float(input("Digite a quantidade: "))
preco = float(input("Digite o preco: "))

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos") 

# Exercicio 2 - Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

temperatura = float(input("Digite a temperatura: "))

if temperatura < 18: 
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")

# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje e nossa terceira aula do bootcamp em python"

palavras = texto.split()

print(palavras)

contagem_de_palavras = {}

# percorrer todas as palavras dentro de palavra e checar se ela ja esta no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] + 1
    else:
        contagem_de_palavras[palavra] = 1


