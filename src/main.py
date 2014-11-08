#! /usr/bin/env python
'''
Created on 08-Nov-2014

@author: Rahul

@summary: The project supports two options:
        1. Repl - Enter into repl to quickly find valid NGram phrases by providing text.
        2. Prepare - Useful to compute NGrams and their collocation score from the development data.
'''
from core.chunker import score_and_save_ngrams
from core.repl import repl

from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description='Find the valid NGram phrases.')

    parser.add_argument('-r', '--repl', help="Enter into the REPL mode",
                        dest='repl', action='store_true')

    parser.add_argument('-p', '--prepare', help="Prepare NGrams and Scores",
                        dest='prepare', action='store_true')

    args = parser.parse_args()

    if args.repl:
        repl()
    elif args.prepare:
        score_and_save_ngrams()
