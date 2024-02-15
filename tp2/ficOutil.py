import math, numpy

def pgcd(a, b):
    while b!=0:
        a, b= b, a % b
    return a

def inverse(a,m):
    if pgcd(a,m)==1: 
        u1,u2,u3,=1,0,a
        v1,v2,v3 = 0,1, m
        while v3!=0:
            q=u3//v3
            u1, u2, u3, v1, v2, v3=v1, v2, v3, (u1-q*v1), (u2-q*v2), (u3-q*v3)
             
        return (u1%m)

def estPremier(Nb):
    if Nb < 2:
        return False
    i=2
    while i<int(math.sqrt(Nb)+1) and Nb%i !=0:
        i=i+1
        if i == int(math.sqrt(Nb)):
            return True
                        
def LPremiers(Nb):
   liste=[int]*Nb
   j=0
   for i in range(2, int(math.sqrt(Nb)+1)):
       if estPremier(i):
           liste[j]=i
           j=j+1
   return (liste)

def trouve(Nb):
    liste= LPremiers(Nb)
    i=0
    while i<numpy.size(liste):
        if Nb%liste[i]==0 and estPremier(Nb/liste[i]):
            return(liste[i],Nb/liste[i])
        i=i+1
        
def trouveN(p, q):
    return p*q

def trouvePhi(p, q):
    return (p-1) * (q-1)

def testerE(E, phi): # on teste si E est inferieur a phi
    if(E< phi and pgcd(phi, E)==1):
        return True
    else:
        return False
    
def trouveD(E, phi):
    return inverse(E, phi)
        
def chiffrer(M, E, N):
    if(M < N):
        return pow(M, E, N)
    else:
        print("M est superieur a N donc on peut pas chiffrer le message!")

 
def dechiffrer(C, N, D):
        return pow(C, D, N)
    
def cryptMes(message):
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  message = 'RSA'
  charCodee = []
  for char in message:
    charCodee.append(alphabet.index(char.upper()))
  return charCodee
    