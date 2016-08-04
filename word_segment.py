"""Word segment program taken from Peter Norvig

http://norvig.com/ngrams/
"""

import collections
import re

from roamanalytics.nlp.resources.sil_english_am import sil_en_am_words as dictionary

#===============================================
# Get (word, count) values from a big text.

def words(text):
    return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(open('big.txt').read()))

#===============================================
# Define helper functions

class Pdist(dict):
    """Probability function.

    A dictionary class which is intialized with
    a corpus and a function that returns low
    probability.

    An object of this class can be called like
    a normal function. It takes a string as parameter
    and returns the probability of that string
    appearing in the corpus.
    """
    def __init__(self, data, N=None, missingfn=None):
        for key, count in data.items():
            self[key] = self.get(key, 0) + count
        self.N = float(N or sum(self.values()))
        self.missingfn = missingfn or (lambda k, N: 1./N)

    def __call__(self, key):
        if key in self:
            return self[key]/self.N
        else:
            return self.missingfn(key, self.N)

def avoid_long_words(word, N):
    return 10./(N * 10**len(word))

N = sum(NWORDS.values())
"""Number of words in the corpus."""

Pw = Pdist(NWORDS, N, avoid_long_words)
"""Gets the probability of a word in corpus.

When called, it gets the probability of the
word in the corpus. If the word does not
exist in the corpus, returns a very low
probability.
"""

def product(numlist):
    """Returns product of a list of numbers.

    Parameters
    ----------
    numlist : iterable

    Returns
    -------
    int
        product of the numbers of the list.
    """
    prod = 1
    for num in numlist:
        prod *= num
    return prod

def memo(f):
    """Decorator for memoization.

    It remembers the function calls and stores the
    values.

    Parameters
    ----------
    f : method

    Returns
    -------
    method
        The method which returns a value if `f` is already
        called or calls `f` and returns the value.
    """
    table = {}
    def fmemo(*args):
        if args not in table:
            table[args] = f(*args)
        return table[args]
    fmemo.memo = table
    return fmemo

#===============================================
# Main functions

def splits(text, L=20):
    """Gets all possible two splits of a string.

    We will only split the string once for each scenario.
    We will stop splitting when the length of first word
    of the split reaches `L`.

    Examples
    --------
    >>> splits('abcde')
    [('a', 'bcde'), ('ab', 'cde'), ('abc', 'de'), ('abcd', 'e'), ('abcde', '')]
    
    Parameters
    ----------
    text : str
        The string we have to split.
    L : int
        Controls the maximum length of first word in the split.

    Returns
    -------
    list
        Get all the split scenarios.
    """
    return [(text[:i+1], text[i+1:]) for i in range(min(len(text), L))]

def Pwords(words):
    """Product of probabilities of each word of `words`.

    Parameters
    ----------
    words : list

    Returns
    -------
    int
        product of probabilities of each word in `words` appearing in
        corpus.
    """
    return product(Pw(w) for w in words)

@memo
def segment(text):
    """Splits a sentence without word stops into readable one.

    We first get the inital splits of `text` where maximum length
    of the first word is 20.

    Now we keep the first word constant and try to `segment` the
    second word.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        Returns the sentence with maximum probability.
    """
    if not text:
        return []

    candidates = ([first] + segment(rem) for first, rem in splits(text))

    return max(candidates, key=Pwords)
