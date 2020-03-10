def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
def main():
    do_twice(print_spam)
main()