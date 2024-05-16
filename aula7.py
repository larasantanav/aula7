# lista = [1,2,3,4,5,6]
# print(len(lista))
# #verificar o tamanho da minha lista 
# #----------------------

# lista.append(19)
# lista[0] = 10
# print(lista)

# #----------------
# del lista[0]
# print(lista)

# lista.remove(2)
# print(lista)

# #remove é um valor da lista
# #del se  refere a posição da lista

# #------------------------
# #loop esta se repetindo, a lista é o seu limite 
# lista4 = [11,22,33,44,55,66]
# for numero in range(1,10): 
#   print(numero * 2 + 10)

    #iterar é percorrer uma lista
#   senha = 123
#   for numero in range(-3,0):
#     senha5 = int(input('digite a senha'))
#    if senha == senha5:
#     print('acesso permitido')

#   else:
#     print('acesso negado')
#     print('voce tem apenas', numero ,'chances para digitar a senha')


# for n in range(1,6):
#    nome = input('digite seu nome')
#    print("seja bem vindo (a)",  nome, n)

#loop 
# for dado in range(1,11):
#     print('numer: ', dado)



# #1
# for pessoas in range(1,6):
#     print('person'+ str(pessoas))


# #2
# lista_numero = [11,22,33,44,55,66,77,88,99]
# print(lista_numero[2])

# #3
# lista_numero.append(9)
# print(lista_numero)

# #4
# # lista_numero.remove(55)
# # print(lista_numero)

# #5
# carros = ["corolla", "civic", "compass"]
# soma = carros + lista_numero
# print(soma)


# #6
# lista8  = [12,45,45,89,78,3,6,78,87]
# for number in lista8:
#     print(number)

# name = [5,8,7,4,1,5,2,3]
# print(name)


# #7
# senha = 55
# for codigo in range(55,56):
#     #senha55 = int(input('digite o numero'))
#     if senha in lista_numero:
#         print('esta na lista')
#     else:
#         print('nao esta na lista')

# numero = int(input('>>'))
# if numero > 11:
#     print('10 é maior')
# else:
#     print('10 é menor')

import random 
# aleatorio = random.random()
aleatorio = random.randint(1,100)
print(aleatorio)
chute = int(input('numero'))

if aleatorio >= chute:
   print('acertou', aleatorio )

elif aleatorio == chute:
  print('acertouuuuuu', aleatorio)
else:
 print('nao acertou', aleatorio)


 
