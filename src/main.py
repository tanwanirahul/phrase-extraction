'''
Created on 08-Nov-2014

@author: Rahul

@summary: The main file for the project.
          Firstly, calculates the PMI scores for Bi, Tri and Quad grams.
          Then waits for the user's input.
          Lastly, for the given text, computes Ngrams and also the
          classification as valid or invalid phrase.
'''
from core.chunker import score_and_save_ngrams

if __name__ == '__main__':
    score_and_save_ngrams()
