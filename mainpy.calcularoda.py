while True:


    # informar os numero 
    x = str(input('Informe o primeiro número .')).replace(',','.')

    y = str(input('Informe o segundo número.')).replace(',','.')

    #converte para números decimais 
    x = float(x)
    y = float(y)

    #usuareio escolhe a operação desejada por ele 
    print("Operações disponiveis :\n")
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')
    print('deseja continuar sim ou não ?')

    #operação recebe o input operação desejtada
    op = input('Operação desejada:')
    match op:
        case '+':
            print(f'a soma é {x + y}.')
        case '-':
            print(f'A subtração é: {x - y}.')
        case '*':
            print(f' A multiplicação é: {x * y}.')
        case '/':
            print(f' A Divisão é {x / y}.')
        case '%':
            print(f' O resoto da divisão é { x % y}.')
        case _:
            print('Operação invalida')
            continue   
    # pergunta para o usuario se deseja continuar ou encerrar 
    continuar =input('Deseja continuar (s/n)? ')

    #verifica a opção do usuario 
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print('Opção inválida')
             
