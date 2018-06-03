from base64 import b64encode
from string import ascii_lowercase
from collections import Counter, defaultdict
from pprint import pprint


def hex2bytes(s):
    """convert a hex-encoded string to bytearray"""
    return(bytes.fromhex(s))

def bytes2hex(b):
    """convert a bytearray to a hex-encoded string"""
    return(b.hex())

def print_bytes(b):
    """print a bytearray as an ascii-encoded string, replacing non-ascii with string escape code"""
    print(b.decode('ascii', 'replace'))

def hex2base64(s):
    """convert a hex-encoded string to a base64-encoded bytes object"""
    return(b64encode(hex2bytearray(s)))


def xor_eq_len(x,y):
    """xor 2 buffers of equal length

    input buffers must be bytelike objects ie bytes or bytearrays

    raises ValueError if buffers are not equal in length
    """
    if len(x) != len(y):
        raise ValueError('Buffer lengths not equal. lenths = {}, {}'.format(len(x), len(y)))
    
    return(bytearray(a^b for a,b in zip(x,y)))

def xor_single_byte(s, k):
    """xor a string against a single byte"""
    return(bytes([c^k for c in s]))

english_letter_frequency_bad = {
    'E':0.1202,
    'T':0.0910,
    'A':0.0812,
    'O':0.0768,
    'I':0.0731,
    'N':0.0695,
    'S':0.0628,
    'R':0.0602,
    'H':0.0592,
    'D':0.0432,
    'L':0.0398,
    'U':0.0288,
    'C':0.0271,
    'M':0.0261,
    'F':0.0230,
    'Y':0.0211,
    'W':0.0209,
    'G':0.0203,
    'P':0.0182,
    'B':0.0149,
    'V':0.0111,
    'K':0.0069,
    'X':0.0017,
    'Q':0.0011,
    'J':0.0010,
    'Z':0.0070,
}

english_letter_freq = {
    'e':   0.12702,
    't':   0.09056,
    'a':   0.08167,
    'o':   0.07507,
    'i':   0.06966,
    'n':   0.06749,
    's':   0.06327,
    'h':   0.06094,
    'r':   0.05987,
    'd':   0.04253,
    'l':   0.04025,
    'c':   0.02782,
    'u':   0.02758,
    'm':   0.02406,
    'w':   0.02360,
    'f':   0.02228,
    'g':   0.02015,
    'y':   0.01974,
    'p':   0.01929,
    'b':   0.01492,
    'v':   0.00978,
    'k':   0.00772,
    'j':   0.00153,
    'x':   0.00150,
    'q':   0.00095,
    'z':   0.00074,
}

def expected_letter_freq(s):
    """returns a dict containing expected letter frequency for a given string"""
    return({k:v*len(s) for (k,v) in english_letter_freq.items()})

def count_letters(s):
    """returns a dict containing counts of letters in a string"""
    observed_count = {x:0 for x in english_letter_freq}
    for c in s.lower():
        if chr(c) in english_letter_freq:
            observed_count[chr(c)] += 1
    return observed_count

def calculate_bhattacharyya_coeff(s):
    """Calcuate bhattacharyya coeff

    Used to compare how similar two sets of data are.

    See https://en.wikipedia.org/wiki/Bhattacharyya_distance#Bhattacharyya_coefficient
    """
    expected_count = expected_letter_freq(s)
    observed_count = count_letters(s)
    bc = 0
    for letter,cnt in observed_count.items():
        bc += (expected_count[letter] * cnt/expected_count[letter]) ** 0.5
    return bc


def calculate_chi_sq(s):
    """calculate chi squared statistic wrt to english letter frequency

    A larger penalty is applied to strings containing relatively fewer ascii char
    """
    freq_count = english_letter_freq

    # if freq count probabilities true, how many letters can we expect
    expected_count = expected_letter_freq(s)

    # count how many letters we got
    observed_count = count_letters(s)

    # calculate chi sqkjj
    chi_sq = 0
    for c in freq_count:
        chi_sq += ((observed_count[c] - expected_count[c])**2)/expected_count[c]
    return chi_sq

def score_text(s, heuristic):
    if heuristic == 'chi_sq':
        return calculate_chi_sq(s)
    elif heuristic == 'bc':
        return calculate_bhattacharyya_coeff(s)
    else:
        raise ValueError('Unknown scoring heuristic {}'.format(heuristic))

