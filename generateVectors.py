from gensim.models import KeyedVectors

def generateVector(word):
    glove_file = 'path to GloVe txt file'
    #download the txt file for GloVe for whatever type that is desired and then insert path above
    word_vectors = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True)

    return word_vectors[word]