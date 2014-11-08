'''
Created on 08-Nov-2014

@author: Rahul

@summary: Loads the corpus data, calculates chunks (BiGram, TriGram and
          QuadGram), scores these chunks and save them into a file.
'''
from nltk.metrics.association import BigramAssocMeasures, TrigramAssocMeasures, \
    QuadgramAssocMeasures
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder, \
    QuadgramCollocationFinder
from common import settings
from common.utils import get_corpus_words, save_ngrams_score


def find_collocation_score(finder, scoring_func):
    '''
        Chunks the corpus data, and finds collocation scores.
    '''
    finder = finder.from_words(get_corpus_words())
    finder.apply_freq_filter(settings.NGRAM_MIN_FREQ)
    return finder.score_ngrams(scoring_func)


def score_and_save(finder, scoring_func, out_file):
    '''
    '''
    ngram_scores = find_collocation_score(finder, scoring_func)
    save_ngrams_score(ngram_scores, out_file)


def score_and_save_bigrams():
    '''
        Compute Bi-Grams and the collocation score for each, and save them.
    '''
    score_and_save(BigramCollocationFinder, BigramAssocMeasures.pmi,
                   settings.VALID_BI_GRAMS_FILE)


def score_and_save_trigrams():
    '''
        Compute Tri-Grams and the collocation score for each, and save them.
    '''
    score_and_save(TrigramCollocationFinder, TrigramAssocMeasures.pmi,
                   settings.VALID_TRI_GRAMS_FILE)


def score_and_save_quadgrams():
    '''
        Compute Quad-Grams and the collocation score for each, and save them.
    '''
    score_and_save(QuadgramCollocationFinder, QuadgramAssocMeasures.pmi,
                   settings.VALID_QUAD_GRAMS_FILE)


def score_and_save_ngrams():
    '''
        Score bi-grams, tri-grams and quad-grams and save them into a file.
    '''
    print "Processing BI Grams..."
    score_and_save_bigrams()
    print "Processing TRI Grams..."
    score_and_save_trigrams()
    print "Processing QUAD Grams..."
    score_and_save_quadgrams()
