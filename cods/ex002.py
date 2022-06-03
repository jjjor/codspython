flag = True
cont = 0
media = 0

numero = int(input('Digite um número: '))

soma = numero
menorNumero = numero
maiorNumero = numero

if numero == 0:
    flag = False
else:
    cont += 1


while flag:
    numero = int(input('Digite um número: '))
    if numero != 0:
        soma += numero
        cont += 1

        if numero > maiorNumero:
            maiorNumero = numero
        if numero < menorNumero:
            menorNumero = numero
    else:
        flag = False


if soma != 0:
    media = soma / cont


print(f'A soma é: {soma}\nA média é: {media}\nO maior número é: {maiorNumero}\nE o menor número é: {menorNumero}')


