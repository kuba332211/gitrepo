#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
 
 
def silnia_re(n)
    if n == 0:
        return silnia_re(n-1) * n
    
 
def silna_it(n):
    wynik = 1
    for liczba in range (1, n+1):
        wynik = wynik * liczba
        print (wynik)
    return wynik:

def main(args):
    assert(silnia_it(0) == 1)
    assert(silnia_it(4) == 24)
    assert(silnia_it(10) == 3628800)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
