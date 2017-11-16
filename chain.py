import re
import numpy as np
from numpy.random import choice
from collections import Counter


class TrigramMarkovChain:

    def __init__(self, file, encoding=None):
        with open(file, 'r', encoding=encoding) as file:
            text = [word for line in file.read().splitlines() for word
                    in re.split("[^a-z'.!?]", line.lower()) if word]

        self.trigram = Counter(zip(zip(text[:-2], text[1:-1]), text[2:]))

    def generate_text(self, length=100):
        sentence = str(choice([' '.join(bi) for bi,_ in self.trigram.keys()],
                              1, p=np.array(
                list(self.trigram.values()))/sum(self.trigram.values()))[0]).split(' ')

        for _ in range(2, length):
            sentence.append(self.next_word(sentence[-2], sentence[-1]))

        return ' '.join(sentence)

    def next_word(self, first, second):
        third, count = [], []
        for trigram in self.trigram:
            if trigram[0] == (first, second):
                third.append(trigram[1])
                count.append(self.trigram[trigram])

        return str(choice(third, 1, p=np.array(count)/sum(count))[0])
