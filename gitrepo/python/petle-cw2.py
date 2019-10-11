#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle-cw2.py



def main(args):
    
    n =int(input("Podaj liczbę: "))
    while n < 1:
        print("Błędne dane!")
        n =int(input("Podaj liczbę: ")) 
       
    m =int(input("Podaj liczbę: "))
    while m <= n:
        print("Błędne dane!")
        m =int(input("Podaj liczbę: "))       
    for liczba in range(n, m + 1):
        
        print(liczba, " ", end ="")
    
    return 0
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
