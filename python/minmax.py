#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
import random 

def losuj(ile, lmin, lmax):
    lista = []
    for i in range (ile):
        lista.append(random.randint(lmin, lmax))
    print (lista)
    return(lista)
    
def minmax():
    ile = int(input("ile liczb podasz? "))
    min = max = int(input("podaj liczbę: "))
    for i in range(ile - 1):
        liczba = int(input("podaj liczbę: "))
        if min > liczba:
            min = liczba
        if max < liczba:
            max = liczba
    return min, max
    
    
def minimum(liczby):
    najm = liczby[0]
    for i in liczby:
        if najm > i:
            najm = i
    return najm 
    
    
    def maximum(liczby):
    najw = liczby[0]
    for i in liczby:
        if najw < i:
            najm = i
    return najw 
    
def main(args):
    # ~min, max = minmax()
    # ~print("Najmniejsza:",min)
    # ~print("Największa:",max)
    losuj (20, 0, 50)
    print('Najmniejsza: ', minimum(liczby))
    print('Największa: ', (liczby))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
