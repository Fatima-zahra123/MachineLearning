import pandas as pd
from numpy import inf
# indice de calcule de desordre
Data_train = pd.read_csv(
    "C:/Users/user/OneDrive/Bureau/S2/ML/TDs/td7/donneesAD.csv")


def GINI(S):
    S = array(S)
    clonne_des_classes = list(S[:, -1])
    classes = list(set(S[:, -1]))
    k = len(classes)
    s = 0
    for i in range(k):
        pi = clonne_des_classes.count(classes[i]/len(S[:, -1]))
        s += pi**2
    return 1-s


def Mesure_desorde(S, numero_colon_attribut):
    Bonne_mesure_desorde = + inf
    Bonne_valeur_de_repartition = 0
    classes = list(set(S[:, -1]))
    valeurs_attribut = list(set(S[:, numero_colon_attribut]))
    valeurs_attribut.sort()
    Gauche = []
    Droite = []

    for i in range(len(valeurs_attribut)-1):
        v = valeurs_attribut[i]
        Gauche.clear()
        Droite.clear()
        for e in S:
            val_attribut_pour_e = e[numero_colon_attribut]
            if val_attribut_pour_e <= v:
                Gauche.append(e)
            else:
                Droite.append(e)
        pGau = len(Gauche)/len(S)
        pDr = len(Droite)/len(S)
        mesure = (pGau)*GINI(Gauche)+(pDr)*GINI(Droite)
        if mesure < Bonne_mesure_desordre:
            Bonne_mesure_desordre = mesure
            Bonne_valeur_de_repartition = v
    return(Bonne_mesure_desordre, Bonne_valeur_de_repartition)


def meilleur_attribut_meilleure_valeur(S):
    meilleur_attribut = 0
    meilleure_val = 0
    meilleure_mesure = + inf

    for num_attribut in range(len(S[0])-1):
        mesure, valeur = Mesure_desordre(S, num_attribut)
        if mesure < meilleure_mesure:
            meilleure_val = valeur
            meilleure_mesure = mesure
            meilleur_attribut = num_attribut
    return meilleur_attribut, meilleure_val


print(meilleur_attribut_meilleure_valeur(Data_train))
