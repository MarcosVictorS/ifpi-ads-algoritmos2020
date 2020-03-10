def print_twice(funcao,valo):
    funcao(valo)
    funcao(valo)


def do_four(funcao, valor):
    print_twice(funcao,valor)
    print_twice(funcao,valor)


def main():
    hori = " "
    hori += "- " * 4
    horizontal = f"+{hori}+{hori}+{hori}+{hori}+"

    ver = " "
    ver += "  " * 4
    vertical = f"|{ver}|{ver}|{ver}|{ver}|"

    print(horizontal)
    do_four(print,vertical)
    print(horizontal)
    do_four(print,vertical)
    print(horizontal)
    do_four(print,vertical)
    print(horizontal)
    do_four(print,vertical)
    print(horizontal)


main()

# DeusExToin
# mcpsquatro
# magolocao12345