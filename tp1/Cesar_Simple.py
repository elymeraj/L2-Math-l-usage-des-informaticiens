message = 'hello'
cle=6
mode='cryptage'  #'cryptage' ou 'decryptage'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
traduction=''
lettre=message[1]
message = message.upper()
for lettre in message:
    num=alphabet.find(lettre)
    if mode=='cryptage':
        num= num + cle
        lettre=alphabet[num%26]
        traduction=traduction+lettre
    else:
        if num-cle<0:
            lettre=alphabet[num-cle+26]
        lettre=alphabet[num-cle]
        traduction=traduction+lettre
print(traduction)


