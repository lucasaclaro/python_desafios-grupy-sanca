### Supondo que a cotação do dólar esteja em R$3.25, salve esse valor em uma variável e
# utilize-o para calcular quanto você teria ao cambiar R$65.00 para dólares.

dolar = 3.25
valor = 65
conversao = valor / dolar

print(f'Ao cambiar R$ {valor:.2f} com a cotação do dólar em R$ {dolar} eu teria ${conversao:.2f}.')



### Abelindo é um professor muito malvado.
# Ele quer decidir como reprovar Rondinelly, que tirou 8.66, 5.35, 5 e 1, respectivamente, nas provas P1, P2, P3 e P4.
# Para isso, ele pode calcular a nota final usando média aritmética (M.A.), média geométrica (M.G.) ou média harmônica (M.H.).

n1 = 8.66
n2 = 5.35
n3 = 5
n4 = 1
total = n1 + n2 + n3 + n4

media_aritimetica = (n1 + n2 + n3 + n4) / 4
media_geometrica = (total ** (1/4))
media_harmonica = 4 / ((1/n1) + (1/n2) + (1/n3) + (1/n4))
print(f'''\nDadas as notas {n1}, {n2}, {n3} e {n4}, seguem as médias:\n
      Média aritimética: {media_aritimetica:.2f},\n
      Média geométrica: {media_geometrica:.2f},\n
      Média harmônica: {media_harmonica:.2f}.''')


### Dada a frase Python é muito legal., use fatiamento para dar nome às variáveis contendo cada palavra. O resultado final deve ser:

# frase = "Python é muito legal."

pal1 = 'Python'
pal2 = 'é'
pal3 = 'muito'
pal4 = 'legal'
frase = f'{pal1} {pal2} {pal3} {pal4}.'
qtd_letras = len(pal1) + len(pal2) + len(pal3) + len(pal4)
print(frase)

# Qual o tamanho dessa frase? E qual o tamanho de cada palavra?
print(f'O tamanho da frase é de {qtd_letras} letras.')
print(f'O tamanho da palavra "{pal1}" é de {len(pal1)} letras.')
print(f'O tamanho da palavra "{pal2}" é de {len(pal2)} letra.')
print(f'O tamanho da palavra "{pal3}" é de {len(pal3)} letras.')
print(f'O tamanho da palavra "{pal4}" é de {len(pal4)} letras.')
