#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pętla-cw1.py


def main(args):
    suma = 0
    
    while suma <= 75:
        liczba = int(input("podaj 1. liczbę"))
        suma = suma + liczba
    print("suma liczb:", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
