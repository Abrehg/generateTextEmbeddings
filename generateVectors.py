from gensim.models import KeyedVectors

def generateVector(word):
    glove_file = './ ...path to GloVe txt file'
    word_vectors = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True)

    return word_vectors[word]