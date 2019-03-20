while True:
    try:
        n = int(input("Entre com um número: "))
    except ValueError:
        print("O valor informado não é um número")