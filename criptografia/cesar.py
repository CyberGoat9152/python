#-*- coding: utf-8 -*-
key = int(input("Write the key of cesar [1~26]: "))
text = input("Write the message for criptograph: ").lower()
newText = ""
for leter in text:
    if leter != " ":
        if (ord(leter) + key) <= 122:
            newText += chr(ord(leter) + key)
        else:
            rest = ord(leter) + key -122 + 96
            newText += chr(rest)
    else:
        newText += " "
print("Cesar message:\n{}".format(newText))