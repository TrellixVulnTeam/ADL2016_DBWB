from collections import defaultdict
import numpy as np


class Vocab(object):
    def __init__(self):
        self.word_to_index = {}
        self.index_to_word = {}
        self.word_freq = defaultdict(int)
        self.total_words = 0
        self.unknown = '<unk>'
        self.add_word(self.unknown, count=0)

        emb_lines = open("RVNN_EMBEDDING.txt","r").readlines() ###
        emb_words = []
        word2vec_embedding_list = []                
        for line in emb_lines:
            line = line.strip()
            temp_word = line.split(" ")[0] 
            emb_words.append(temp_word)
            temp_emb = line.split(" ")[1:] 
            temp_emb = np.array(temp_emb)            
            word2vec_embedding_list.append(temp_emb)
        word2vec_embedding = np.array(word2vec_embedding_list)
        word2vec_embedding = word2vec_embedding.astype(float)
        self.emb_words = emb_words 
        self.emb_numpymatrix = word2vec_embedding

    def add_word(self, word, count=1):
        if word not in self.word_to_index:
            index = len(self.word_to_index)
            self.word_to_index[word] = index
            self.index_to_word[index] = word
        self.word_freq[word] += count

    def construct(self, words):
        for word in words:
            self.add_word(word)
        self.total_words = float(sum(self.word_freq.values()))
        print '{} total words with {} uniques'.format(self.total_words, len(self.word_freq))

    def encode(self, word):
        if word not in self.word_to_index:
            word = self.unknown
        return self.word_to_index[word]

    def decode(self, index):
        return self.index_to_word[index]

    def emb_wordtoindex(self, word):
        words = self.emb_words 
        index = words.index(word)
        return index

    def __len__(self):
        return len(self.word_freq)
