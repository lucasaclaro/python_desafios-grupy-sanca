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