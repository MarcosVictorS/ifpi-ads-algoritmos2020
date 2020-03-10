def right_justify(s):
    quant_letra = len(s)
    q = 70 - quant_letra
    espaco = " " * q
    print(f"{espaco}{s}")
def main():
    palavra = input('Digite alguma coisa: ')
    right_justify(palavra)
main()