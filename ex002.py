soma = 0
cont = 0
maior = 0
menor = 0

while True:
    numero = int(input('Digite um numero: '))
    if numero != 0:
        soma += numero
        cont += 1
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    else:
        break

media = soma / cont

print(f'A média dos números é {media}.')
print(f'A soma de seus números é igual a {soma}.')
print(f'Seu maior número é {maior}.')
print(f'Seu menor número é {menor}.')
