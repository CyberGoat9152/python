#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from hashlib import md5
from sys import argv
from os import system
def encodes( senha ):
    senhanova = md5()
    senhanova.update( senha.encode( 'UTF-8' ) )
    return senhanova.hexdigest()
def exibe():
    system('clear')
    strload = "\tSenha digitada:\t{}\n\tSenha Gerada:\t{} ".format(argv[1], encodes(argv[1]) )
    mard = ''
    mard = '+'+'-'*( len(strload) - 10 )+'+'
    print(mard)
    print(strload)
    print(mard)

def main():
    exibe()

if __name__ == "__main__":
    main()
