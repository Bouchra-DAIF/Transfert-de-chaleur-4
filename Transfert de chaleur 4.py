print("Transfert de chaleur ")
T1=input("Entrez la température initiale: ")
T2=input("Entrez la tmpérature finale: ")
R=input("Entrez la résistance: ")
try:
    T1=float(T1)
    T2=float(T3)
    R=float(R)
    Q=(T3-T1)/R
    print("Le flux est", Q)
except:
    print("erreur")