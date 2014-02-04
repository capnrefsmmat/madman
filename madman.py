import nltk
from nltk.tag.simplify import simplify_wsj_tag
import random
import Markov

class Madman(object):
    # Only these parts of speech may be replaced with madlibs.
    allowed_parts = {"ADJ", "ADV", "N", "NP", "V", "VD", "VG", "VN"}

    # Do not replace these words.
    skiplist = {"are", "is"}

    madlib_prob = 0.3
    
    def __init__(self, brain, cacheDir="cache/"):
        self.load(brain, cacheDir)

    def load(self, brain, cacheDir):
        print cacheDir + brain
        self.brain = Markov.MarkovChain(cacheDir + brain + "-fwd", 1, False)

    def madlib(self, text):
        """Take a sentence and madlibify it, returning the result text."""

        tagged_text = nltk.pos_tag(nltk.tokenize.word_tokenize(text))
        simplified = [(word, nltk.tag.simplify.simplify_wsj_tag(tag))
                      for word, tag in tagged_text]

        new_text = [simplified[0][0], simplified[1][0]]
        for i in range(2, len(simplified)):
            word, pos = simplified[i]
            if pos in self.allowed_parts and word not in self.skiplist and \
               random.random() <= self.madlib_prob:
               word = self.replace_word(word, pos, simplified[i-2:i])

            new_text.append(word)

        return " ".join(new_text)

    def replace_word(self, word, pos, context):
        """Devise a fun replacement for a word using two words of context."""

        words = self.brain.getNextWords([context[0][0], context[1][0]])

        if len(words) == 0:
            return word

        weightedWords = dict()
        for word, num in words.iteritems():
            weightedWords[word] = num
            
        # do a weighted random selection from the words
        rand = random.randint(0, sum(weightedWords.values()))
        pos = 0
        for word, weight in weightedWords.items():
            pos += weight
            if rand <= pos:
                return word
