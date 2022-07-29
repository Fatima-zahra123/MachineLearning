import pandas


def Entropie(S):
    classes_distinctes = set(S[:, -1])
    classes = list(S[:, -1])
    s = 0
    for c in classes_distinctes:
        p = classes.count(c)/len(classes)
        s += p*log2(p)
    return(-1.0*s)


def Gain_d_information(S, numero_colon_attribut):
    classes = list(set(S[:, -1]))
    valeurs_attribut = list(set(S[:, numero_colon_attribut]))
    Si = [[]for i in range(len(valeurs_attribut))]
    for e in S:
        e = list(e)
        val_attribut_pour_e = e[numero_colon_attribut]
        numero_sous_ensemble = valeurs_attribut.index(val_attribut_pour_e)
        Si[numero_sous_ensemble].append(e)
    Si = array(Si)
    som = 0
    for sous_ensemble in Si:
        som += (len(sous_ensemble)/len(S))*Entropie(sous_ensemble)
    return(Entropie(S)-som)


data = pandas.read_csv("C:/Users/user/OneDrive/Documents/dataset.csv")
data
print(Gain_d_information(data, 0))
