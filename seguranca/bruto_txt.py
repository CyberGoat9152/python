#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
def md5(p):
    m = hashlib.new('md5')
    m.update(p.encode('utf-8'))
    return m.hexdigest()





a = open("pao.txt", "w")
dic = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9")
for l1 in dic:
    for l2 in dic:
        for l3 in dic:
            for l4 in dic:
                for l5 in dic:
                    for l6 in dic:
                        for l7 in dic:
                            for l8 in dic:
                                print(l1+l2+l3+l4+l5+l6+l7+l8)
                                a.write(+l1+l2+l3+l4+l5+l6+l7+l8+";\n")
a.close()
exit()
            
