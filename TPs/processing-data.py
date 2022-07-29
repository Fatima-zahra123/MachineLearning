from nltk.corpus import stopwords
import string
import nltk

nltk.download('stopwords')
nltk.download('wordnet', quiet=True)


def nettoyage(corpus_ensemble_documents):

    for i in range(len(corpus_ensemble_documents)):
        corpus_ensemble_documents[i] = corpus_ensemble_documents[i].lower()
    for i in range(len(corpus_ensemble_documents)):
        for c in string.punctuation:
            x = corpus_ensemble_documents[i].replace(c, ' ')
            corpus_ensemble_documents[i] = x
    stopwords_anglais = stopwords.words('english')
    for i in range(len(corpus_ensemble_documents)):
        L = corpus_ensemble_documents[i].split()
        for mot in L:
            if mot in stopwords_anglais:
                while mot in L:
                    L.remove(mot)
        corpus_ensemble_documents[i] = " ".join(L)
        return(corpus_ensemble_documents)


nettoyage("m")
