#! /usr/bin/env python
# -*- coding: utf-8 -*-
def cripChines(mensagem):
	s = ""
	for l in mensagem:
		s += chr(ord(l)+30000)
	return s
def descripChines(mensagem):
	s = ""
	for l in mensagem:
		s += chr(ord(l)-30000)
	return s

print("Senha nova: %s"%cripChines(input("Digite a senha: ")))
