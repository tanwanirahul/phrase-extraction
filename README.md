phrase-extraction
=================

A simple project to extract semantically valid phrases from a text based on movies corpus. 


How does it work?
===================

The project is based on movies corpus taken from http://www.ark.cs.cmu.edu/movie$-data/. From the development data (data/movies-data-dev.txt in this repo) we first calculate BIGrams, TRIGrams, QUADGrams and their collocation score based on [PMI](http://en.wikipedia.org/wiki/Pointwise_mutual_information "PMI"). The NGrams and their collocation score for this corpus is available in data directory with filenames bigrams.txt, trigrams.txt and quadgrams.txt.

Classification is based on the PMI score. For a given NGram, we check to see if the NGram is present in what we have computed from corpus and if the min PMI scoring criteria for the given NGram is met.


How to Use?
=============
1. Install the dependencies
    pip install -r requirements.txt

2. Run the main.py program in src with --repl option.
    ./main.py --repl
3. The repl allow you to type a text and find out the valid NGram phrases.

In addition to --repl, the main script also allow you to recompute the BIGrams, TRIGrams and QUADGrams and their collocations score, in case you decide to update the development corpus. This is being supported with --prepare option.
    ./main.py --prepare
