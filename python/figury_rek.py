#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py

import turtle

#def figura(bok, kat, ile):
 #   for i in range(ile): 
  #      turtle.forward(bok)
   #     turtle.right(kat)

def figura_rek(bok, kat, ile): 
def figura_rek(bok, kat, ile):
    turtle.forward(bok)
    turtle.right(kat)
    if ile > 0:        
        figura_rek =(bok, kat, ile - 1, krok)

    
def main(args):
    turtle.setup(800, 600)
    turtle.color('red', 'blue')
    turtle.speed(0)
    turtle.begin_fill()
    
    figura_rek(200, 90, 4, 5)
    
    turtle.end_fill()
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
