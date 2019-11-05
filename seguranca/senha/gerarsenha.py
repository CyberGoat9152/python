#!/usr/bin/env python
#-*- coding: utf-8 -*-
from hashlib import md5
from sys import argv

def encode( senha ):
    senhanova = md5()
    senhanova.update( senha )
    return senhanova.hexdigest()
def exibe():
    print("Senha digitada:\t{}\nSenha Gerada:\t{}".format(argv[1], encode(argv[1]) ) )

def main():
    exibe()

if __name__ == "__main__":
    main()
