'''
Created on 08-Nov-2014

@author: Rahul

@summary: Holds all the re-usable utility/helper functions.
'''
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from common import settings
import csv


def get_corpus_words():
    '''
        Returns all the words from corpus.
    '''
    reader = PlaintextCorpusReader(settings.CORPUS_ROOT,
                                   settings.CORPUS_FILES_GLOBB)
    if reader:
        return reader.words()
    return []


def save_ngrams_score(ngrams_scores, out_file):
    '''
        Saves the given ngrams_scores to the specified output file.
    '''
    def preformat(ngrams_score):
        '''
            Returns the tuple of the form ('ngram', score).
        '''
        return (' '.join(ngrams_score[0]).encode('utf-8'), ngrams_score[1])

    rows = [preformat(ngrams_score) for ngrams_score in ngrams_scores]
    write_csv(out_file, rows)


def write_csv(csv_file, rows):
    '''
        Writes the given rows to a csv file.
    '''
    with open(csv_file, 'wb') as ofile:
        writer = csv.writer(ofile, delimiter=',')
        writer.writerows(rows)


def read_csv(csv_file):
    '''
        Reads the given csv file and returns the records.
    '''
    with open(csv_file, 'rb') as ifile:
        reader = csv.reader(ifile, delimiter=',')
        for row in reader:
            yield row
