def do_twice(funcao, valor):
    funcao(valor)
    funcao(valor)


def p(h):
    print(h)


def main():
    do_twice(p,5)


main()