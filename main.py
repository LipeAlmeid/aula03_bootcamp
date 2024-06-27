import time

# IF ELSE 

x = int(input("Please enter an integer: "))

if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
   print('Zero')
elif x == 1:
    print('Single')
else:
   print('More')


# FOR / WHILE 

lista_de_alunos = ["rafael", "Fábio", "luciano"]

for aluno in lista_de_alunos:
    print(aluno)



condicao = True 

while condicao:
   Print("Execute minha ETL")
   time.sleep(5)
  