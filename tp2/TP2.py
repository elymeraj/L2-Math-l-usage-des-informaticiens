from ficOutil import inverse
from ficOutil import trouve
from ficOutil import trouveN
from ficOutil import trouvePhi
from ficOutil import testerE
from ficOutil import chiffrer
from ficOutil import dechiffrer
from ficOutil import cryptMes


print("***************************TP2 CODE RSA***************************")
print("*            TRAVAILLE PAR:                                      *")
print("*                           Eldis YMERAJ --> #22015179           *")
print("*                           Zied JERBI   --> #22013944           *")
print("******************************************************************")
print("")
print("")
print("")
# exercice 1      
# exercice 1.1
print("===========================EXERCICE 1===========================")
N, E, D, C = 391, 151, 7, 17
print("1.1 Alice va obtenir nombre: ", dechiffrer(17, 391, 7))  
# exo 1.1

p,q = trouve(N)
print("1.2 Les nombres p et q sont: ", p, q)

print("1.3 phi de N: ", trouvePhi(p, q))
print("===========================EXERCICE 2===========================")

N, E, D = 221, 11, 35
M = 112
C = chiffrer(M, E, N)
print("2.1(a) Le message chiffree est C = ", C)
print("2.1(b) Le cryptogramme C dechiffree est M' =  ", dechiffrer(C, D, N))
p, q = 53, 71
phi = trouvePhi(p, q)
print("2.2(a)       N = ", trouveN(p, q))
print("         phi(N) = ", phi)
E = 307
phi = 3640
print("2.2(b) Est-ce que E est acceptable? ", testerE(E, phi))
phi = 3640
D = inverse(E, phi)
print("       Le nombre correspondant est D = ", D)
print("2.2(c) Les elements qui constituent le cle publique sont E et N = , on a deja trouve.")
print("E = ", E)
print("N = ", N)
print("       Les elements qui constituent le cle privee sont D et N")
print("D = ", D)
print("===========================EXERCICE 3===========================")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'RSA'
print("Chiffrage de message RSA est: ", cryptMes(message))











