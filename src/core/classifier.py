'''
Created on 09-Nov-2014

@author: Rahul

@summary: Classifies whether the Ngram is a valid phase.
'''
from common import settings
from common.utils import load_ngrams_score

BIGRAMS = {}
TRIGRAMS = {}
QUADGRAMS = {}


def is_valid(ngram_scores_data, ngram, min_score):
    '''
        For a given ngram, returns if the ngarm is valid based on min score.
    '''
    ngram = tuple(ngram.split(' '))
    score = ngram_scores_data.get(ngram, None)
    if (score is not None) and score >= min_score:
        return True
    return False


def is_valid_bigram(bigram):
    '''
        Checks if the given bigram is valid.
    '''
    return is_valid(BIGRAMS, bigram, settings.MIN_BI_GRAMS_SCORE)


def is_valid_trigram(trigram):
    '''
        Checks if the given trigram is valid.
    '''
    return is_valid(TRIGRAMS, trigram, settings.MIN_TRI_GRAMS_SCORE)


def is_valid_quadgram(quadgram):
    '''
        Checks if the given quadgram is valid.
    '''
    return is_valid(QUADGRAMS, quadgram, settings.MIN_QUAD_GRAMS_SCORE)


# Load the scores for BI-Grams, Tri-Grams, and Quad-Grams.
def load_ngrams_data():
    '''
        Loads the NGrams scores.
    '''
    BIGRAMS.update(load_ngrams_score(settings.VALID_BI_GRAMS_FILE))
    TRIGRAMS.update(load_ngrams_score(settings.VALID_TRI_GRAMS_FILE))
    QUADGRAMS.update(load_ngrams_score(settings.VALID_QUAD_GRAMS_FILE))
