def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    print(sumar(2, 3))
    print(restar(5, 1))
    print(multiplicar(4, 6))

    try:
        print(dividir(10, 2))
        print(dividir(10, 0))
    except ValueError as error:
        print(f"Error: {error}")
