nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print('Média = ', media)

if 7 < media < 9.99:
    print('Aprovado!')
elif media == 10:
    print('Aprovado com distinção!')
else:
    print('Reprovado!')