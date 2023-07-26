from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

def generateVector(word):
    glove_file = './glove.42B.300d.txt'
    word_vectors = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True)

    return word_vectors[word]