import pyperclip

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789:,.?!@#$%&*=+-;\/><é^€[]{}~'
message = 'Hello'
a =
b =
a1=
a2=
mode ='cryptage'
cle =6
traduction = ''
def pgcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def inverse(a, m):
    #Ca va retourner l'inverse de a%m (a*x %m=1)
    if pgcd(a, m) !=1:
        return None #il n'existe pas mod inverse si a & m ne sont pas premiers entre eux.
    
    #On calcule en utilisant algorithme d'Euclide etendu
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // c'est l'operateur de division d'entiers
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m
 

