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
   
    
def prostokat2(a, b, znak, znak2):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(znak, end='')
            else:
                print(znak2, end='')
        print()
    pass
    
    
def choinka1(h, znak):
    for i in range(h):
        for j in range(h):
            print(znak)
        
def choinka2(h, znak):    
         
         
def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    znak = input("podaj znak")
    znak2 = input("podaj znak2")
    h = input("podaj wysokość")
     
    prostokat1(a, b, znak)
    print(" ")
    prostokat2(a, b, znak, znak2)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
