#!/usr/bin/env python
"""Detect single-character XOR

One of the 60-character strings 
in this file has been encrypted 
by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
import pdb
from utils import *
from pprint import pprint
from collections import namedtuple
from operator import attrgetter, itemgetter


class Guess(object):
    def __init__(self, k, pt, score, line_no):
        self.k = k
        self.pt = pt
        self.score = score
        self.line_no = line_no

    def __str__(self):
        s =f'{str(self.k):>4} {str(self.pt):<50} {str(self.score):>4.4} {str(self.line_no):>3}'
        return s

    def __repr__(self):
        return self.__str__()


# TODO: sort final max score list by scores
# right now it works but I have to look through results
if __name__ == '__main__':
    n = 5
    with open('files/4.txt', 'r') as f:
        guess = {}
        max_scores = []
        for line_no, l in enumerate(f):
            l = l.strip()
            scores = []
            for k in range(0,256):
                pt = xor_single_byte(hex2bytes(l), k)
                #scores.append([pt, score_text(pt,'bc')])
                scores.append(Guess(k, pt, score_text(pt, 'bc'), line_no))

            # find highest ranking scores for each key guess
            max_scores.append(sorted(scores, key=attrgetter('score'), reverse=True)[0:2])
            #max_scores.append(sorted(scores, key=itemgetter(1), reverse=True)[0:2])
        
pprint(max_scores)
#pprint(sorted(max_scores, key=itemgetter(1)))






        
        
