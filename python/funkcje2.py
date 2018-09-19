#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sumuj(a, b):
    """
    funkcja zwraca sumę dwóch podanych liczb 
    """
    return a + b
    
def roznica(a, b):
    """
    funkcja zwraca roznice roznice podanych liczb 
    """
    return a - b
    
def iloczyn(a, b):
    """
    funkcja zwraca iloczyn dwóch podanych liczb 
    """
    return a * b
    
def iloraz(a, b):
    """
    funkcja zwraca iloraz dwóch podanych liczb 
    """
    return a / b
    
def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    
    print(sumuj(a, b))
    print(roznica(a, b))
    print(iloczyn(a, b))
    print(iloraz(a, b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
