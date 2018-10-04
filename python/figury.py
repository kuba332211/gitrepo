#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py

def prostokat1(a, b, znak):
    for i in range(a):
        for j in range(b):
            print(znak, end='') 
        print()
    pass
    
def prostokat2(a, b, znak):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1:
                
            print(znak, end='') 
        print()
    pass
        
def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    znak = input("podaj znak")
    
    for i in range(a):
        for j in range(b):
            print(znak, end='') 
        print()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
