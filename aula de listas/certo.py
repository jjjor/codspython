numero = int(input('informe um valor inteiro e positivo: '))
soma = 0
for item in range(2, numero+1):
    if item == 2 or item == 3 or item == 5 or item % 2 != 0 and item // item == 1 and item // 1 == item and item % 3 != 0 and item % 5 != 0:
        print(f'{item} é primo.')
        soma += item

print(f'A soma dos números ímpares é igual a {soma}.')