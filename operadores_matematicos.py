from math import pi
### Calcule o resto da divisão de 10 por 3.

print(f'O resto da divisão de 10 por três é {10 % 3}.')



### Calcule a tabuada do 13.

num = 13
cont = 0
print('\nTabuado do 13:\n')
while True:
    print(f'{num} x {cont} = {num * cont}.')
    cont += 1
    if cont > 10:
        break



### Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas.
### Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

#2 aulas por semana durante 4 meses
#8 aulas por mês e 32 no total
faltas = int((32 * 25) / 100)


print(f'\nDavinir pode faltar {faltas} vezes.')




### Calcule a área de um círculo de raio = 2.

#Fórmula: A = Pi * r²

raio = 2
area = pi * (2**2)
print(f'\nA área de um círculo de raio {raio} é igual a {area:.2f}.')

