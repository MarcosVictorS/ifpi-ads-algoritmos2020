def do_twice(funcao,valo):
    funcao(valo)
    funcao(valo)


def p(h):
    print(h)
    print(h)

def do_four(funcao, valor):
    do_twice(funcao,valor)
    do_twice(funcao,valor)


def main():
    do_four(p,5)


main()