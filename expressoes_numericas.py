from math import pi

### Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?Quantos segundos há em 3 horas, 23 minutos e 17 segundos?

min = 60 * 60
hora = 60 * min
resultado = (hora * 3) + (min * 23) + 17
print(f'Em 3h23m17s há {resultado} segundos.')


### Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?

print(f'\nSe você correr 65km em 3h23m17s, a velocidade média será de {65000 / resultado:.2f} m/s.')



### Resolva essa expressão

expressao = (100 - 413 * (20 - 5 * 4)) / 5

print(f'\nResultado da expressão: {expressao}.')



### Enivaldo quer ligar três capacitores, de valores:

c1 = 10
c2 = 22
c3 = 6.8

capacitancia_paralelo = c1 + c2 + c3
capacitancia_serie = 1 / ((1/c1) + (1/c2) + (1/c3))
print(f'\nSe Enivaldo ligar os capacitores em paralelo o valor resultante seré de {capacitancia_paralelo:.2f} e se ligar em série será de {capacitancia_serie:.2f}.')



### Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e compraram alguns itens:
#75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
#2 pacotes de macarrão: R$ 8,73 cada
#1 pacote de Molho de tomate: R$ 3,45
#420g Cebola: R$ 5,40/kg
#250g de Alho: R$ 30/kg
#450g de pães franceses: R$ 25/kg
#Calcule quanto ficou para cada um.

cerveja = 75 * 2.2
macarrao = 2 * 8.73
molho = 3.45
cebola = (5.40 * 42) / 100
alho = (30 * 25) / 100
total = cerveja + macarrao + molho + cebola + alho

print(f'\nO valor total da compra ficou em R$ {total:.2f}, ficando R$ {total/5:.2f} para cada um.')



### Krissia gosta de bolinhas de queijo. Ela quer saber quantas bolinhas de queijo dá para colocar dentro de um pote de sorvete de . Ela pensou assim:

# Um pote de sorvete tem dimensões 15 cm x 10 cm x 13 cm. Uma bolinha de queijo é uma esfera de raio r = 1.2 cm. O fator de empacotamento ideal é 0.74,
# mas o pote de sorvete tem tamanho comparável às bolinhas de queijo, aí tem efeitos de borda, então o fator deve ser menor. Mas as bolinhas de queijo são
# razoavelmente elásticas, então empacota mais.
# Esse valor parece razoável. Sabendo que o volume de uma esfera de raio é o volume do pote de sorvete é  e o fator de empacotamento
# é a fração de volume ocupado pelas bolinhas de queijo. Ou seja,  do pote de sorvete vai ser ocupado pelas bolinhas de queijo.
#Ajude a Krissia descobrir quantas bolinhas de queijo cabem no pote de sorvete!

raio = 1.2
volume_uma_esfera = 4/3 * (pi * (raio ** 3))
volume_pote = 15 * 10 * 13 * 0.74
res = int(volume_pote / volume_uma_esfera)
print(f'\nCabem {res} bolinhas de queijo no pote de sorvete.')