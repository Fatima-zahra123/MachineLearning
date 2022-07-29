from numpy import *
import pandas
df = pandas.DataFrame([[(0, 1, 'C1')], [0, 0, 'C1'], [1, 1, 'C2'], [
                      1, 0, 'C2']], columns=['A', 'B', 'Classes'])
df = df.to_numpy()


def Entropie(S):
    classes_distinctes = set(S[:, -1])
    classes = list(S[:, -1])
    s = 0
    for c in classes_distinctes:
        p = classes.count(c)/len(classes)
        s += p*log2(p)
    return(-1.0*s)


print(Entropie(df))
