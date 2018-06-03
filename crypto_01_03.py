#!/usr/bin/env python
"""
Single-byte XOR cipher

The hex encoded string:

    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
"""
from utils import *
from pprint import pprint
from collections import namedtuple
from operator import attrgetter

if __name__ == '__main__':
    ct='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    Guess = namedtuple('Guess', 'key_guess plaintext score')
    scores = []
    for k in range(0,256):
        pt = xor_single_byte(hex2bytes(ct), k)
        scores.append(Guess(k, pt, score_text(pt, 'bc')))
    scores = sorted(scores, key=attrgetter('score'), reverse=True)
    for k in scores[0:5]:
        print('key=0x{:2x}|{:2} score={:6.6} pt={}'.format(k.key_guess, chr(k.key_guess), k.score, k.plaintext.decode()))



        
        
