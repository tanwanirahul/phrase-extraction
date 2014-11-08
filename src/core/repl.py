'''
Created on 09-Nov-2014

@author: Rahul
'''
from core.classifier import load_ngrams_data, is_valid_bigram, is_valid_trigram,\
    is_valid_quadgram
from common.utils import get_ngrams


def evaluate(text):
    valid_phrases = [bigram for bigram in get_ngrams(text, 2) if is_valid_bigram(bigram)]  # @IgnorePep8
    valid_phrases.extend([trigram for trigram in get_ngrams(text, 3) if is_valid_trigram(trigram)])  # @IgnorePep8
    valid_phrases.extend([quadgram for quadgram in get_ngrams(text, 4) if is_valid_quadgram(quadgram)])  # @IgnorePep8
    return valid_phrases


def print_results(results):
    '''
        Prints the results.
    '''
    print "\n\nValid Phrases:\n"
    for i, result in enumerate(results):
        print "%s. %s" % (i + 1, result)


def repl():
    '''
        Read the text.
        Evaluate the text to find NGrams.
        Print the valid NGram phrases.
        Loop.
    '''
    load_ngrams_data()
    print "Welcome to REPL. Enter text to find the valid NGram phrases."

    while True:
        text = raw_input('\n\nText: ')
        results = evaluate(text)
        print_results(results)
