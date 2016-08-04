"""Spelling detection program by Peter Norvig

http://norvig.com/spell-correct.html
"""

import collections
import re

def words(text):
    """Get all the words.
    
    Gets all the strings that contain only the letters of the alphabet.

    Parameters
    ----------
    text : str
        The text to be searched upon.

    Returns
    -------
    list
        A list of words.
    """
    return re.findall('[a-z]+', text.lower())

# Simple model: get the counts of words.
def train(features):
    """Create a frequency model.

    Parameters
    ----------
    features : list
        List of words found in a text.

    Returns
    -------
    collections.defaultdict
        Map of each word with its freqency.
    """
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(open('big.txt').read()))
"""Sample space of words"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    """Get all strings at edit distance of 1 from `word`.

    Parameters
    ----------
    word : str
        The word which we have to correct.

    Returns
    -------
    set
        List of words that are at edit distance of 1 to `word`.
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    """Get all strings at edit distance of 2 from `word`.

    Return only those strings that are in our corpus.

    Parameters
    ----------
    word : str
        The word which we have to correct.

    Returns
    -------
    set
        List of words that are at edit distance of 2 to `word`.
    """
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    """Return words that are part of our corpus.

    Parameters
    ----------
    words : iterable
    
    Returns
    -------
    set
        List of words that are in our corpus.
    """
    return set(w for w in words if w in NWORDS)

# This is the main program people will call
def correct(word):
    """Correct the given word.

    For MNK, we got more hits with edit distance of 1
    rather than with edit distance of 2.

    Of all the possible choices of corrections, chooses
    the word with more frequency in our corpus.

    Parameters
    ----------
    word : str
        The word which we have to correct.

    Returns
    -------
    str
        The corrected word
    """
    # We get words with max edit distance two.
    # candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]

    # We only want the words with max edit distance one.
    candidates = known([word]) or known(edits1(word)) or [word]
    return max(candidates, key=NWORDS.get)
