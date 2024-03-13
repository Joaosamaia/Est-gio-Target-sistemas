def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci(n - 1)
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        return sequencia
    
#loop que obtem o input do numero desajdo, com tratamento de erro
while True:
    try:
        n = int(input('Digite o número desejado: '))
        break
    except:
        print('Digite um número inteiro.')

print(fibonacci(n))
