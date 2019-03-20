while True:
    try:
        n = int(input("Entre com um número: "))
    except ValueError as erro:
        print(erro)