#! /usr/bin/env python
# -*- coding: utf-8 -*-
# int () przeksztalca angument na liczbę całkowitą int
# DRY - don't repeat yourself

def hello():
    print("witaj, jestem Python!")
    
def witaj():
    imie = input("Jak masz na imię?")
    print("witaj",imie,"!")
    
def suma(l1, l2):
    print("Suma:"),a + b)
    
    

def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    print(a)
    print(b)
    #print("suma:",a+b)
    suma(a, b)
    print("różnica:",a-b)
    print("iloczyn:",a*b)
    print("iloraz:",a/b)
    hello()
    witaj()
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
