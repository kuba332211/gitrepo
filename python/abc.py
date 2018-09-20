#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    a = int(input("podaj 1. liczbę"))
    b = int(input("podaj 2. liczbę"))
    c = int(input("podaj 3. liczbę"))
    if a > b: 
        if a > c:
            print("maks: ", a)
        else:
            print("maks: ",c)   
        
    else:
        print("liczby równe")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
