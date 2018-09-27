#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    while a >= b:
        print ("Błąd")
        b = int(input("podaj 2. liczbę"))
    if a >= b:
        print ("Błędne dane!")
        exit(0)
    for i in range(a, b+1):
        if i % 2 == 0: 
            print(i)
        else:
            print("liczba nieparzysta")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
