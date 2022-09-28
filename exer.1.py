def comfor(num1, num2):
    soma = 0
    for c in range(num1, num2 + 1):
        soma += c
    return soma

def comwhile(num1, num2):
    soma = 0
    c = 0
    while c < (num2 - num1) + 1:
        soma += num1 + c
    return soma


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input('Primeiro Número? '))
            break
        except ValueError:
            print('TEM QUE SER UM NÚMERO')
            print()


    while True:
        try:
            num2 = int(input('Segundo Número? '))
            break
        except ValueError:
            print('TEM QUE SER UM NÚMERO')
            print()

    if num1 >= num2:
        print('INVÁLIDO: O número 1 tem que ser menor do que o número 2')
    else:
        print('O número 1 é maior do que o número 2.')

    pergunta = input('O que pretende usar? comfor / comwhile? ')

    soma = comfor(num1, num2)
    print(f'A soma dos 2 números é {soma}.')
