def do(funcao, valor):
    funcao(valor)


def p(h):
    print(h)
    print(h)


def main():
    do_twice(p,"@bado")


main()