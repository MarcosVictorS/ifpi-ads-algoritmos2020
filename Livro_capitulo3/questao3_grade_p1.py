def p(h):
    print(h)


def do_twice(funcao,valo):
    funcao(valo)
    funcao(valo)


def do_four(funcao, valor):
    do_twice(funcao,valor)
    do_twice(funcao,valor)


def main():
    hori = " "
    hori += "- " * 4
    horizontal = f"+{hori}+{hori}+"

    ver = " "
    ver += "  " * 4
    vertical = f"|{ver}|{ver}|"

    print(horizontal)
    do_four(p,vertical)
    print(horizontal)
    do_four(p,vertical)
    print(horizontal)


main()

# DeusExToin
# mcpsquatro
# magolocao12345