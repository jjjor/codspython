x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
n = float(input('Terceiro Número: '))
if n >= x and n <= y:
    print(f'Dentro do intervalo entre {x:.1f} e {y:.1f}.')
else:
    print(f'Fora do intervalo entre {x:.1f} e {y:.1f}.')
