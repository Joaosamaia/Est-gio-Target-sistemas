def inverter_string(string):
    string_invertida = ''
    #loop que lê cada caractere da string e concatena ele a variavel string_invertida 
    for i in string:
        string_invertida = i + string_invertida
    return string_invertida

#loop que obtem o input do texto desejado, com tratamento de erro
while True:
    try:
        texto = input('Digite o texto desejado: ')
        texto_invertido = inverter_string(texto)
        print("Texto original:", texto)
        print("Texto invertido:", texto_invertido)
        break
    except (KeyboardInterrupt, ValueError):
        print('\nPor favor, digite um texto válido.')
