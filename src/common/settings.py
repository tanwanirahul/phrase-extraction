'''
Created on 08-Nov-2014

@author: Rahul

@summary: Holds the settings/configurations like file names etc.
'''
import os

# ../data directory.
CORPUS_ROOT = os.path.join('..', 'data')

CORPUS_FILES_GLOBB = 'movies-data-dev.txt'


# ../data/<n>grams.txt
VALID_BI_GRAMS_FILE = os.path.join(CORPUS_ROOT, 'bigrams.txt')
VALID_TRI_GRAMS_FILE = os.path.join(CORPUS_ROOT, 'trigrams.txt')
VALID_QUAD_GRAMS_FILE = os.path.join(CORPUS_ROOT, 'quadgrams.txt')

# Min PMI score values for N Gram to be qualified as valid.
MIN_BI_GRAMS_SCORE = 11
MIN_TRI_GRAMS_SCORE = 18
MIN_QUAD_GRAMS_SCORE = 50

NGRAM_MIN_FREQ = 5
