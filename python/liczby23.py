#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py

def liczby2():
    ile = 0 
    for i in range(1, 10):
        for j in range(10):
            if i != j: 
                print("{}{} ".format(i, j), end="")
                ile = ile + 1 
    return ile
    
    
def liczby3():
    ile = 0 
    for i in range(1, 10):
        for j in range(10):
            for k  in range(10):
                if i != j and i != k and j != k: 
                    print("{}{}{} ".format(i, j, k), end="")
                ile = ile + 1 
    return ile
        
        
def main(args):
    liczby3
    print("/n/nLiczb 2-cyfrowych:", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
