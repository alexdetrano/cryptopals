#!/usr/bin/env python
"""
Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""
import codecs
from base64 import b64encode


def hex2base64(hex_str):
    '''Returns a bytearray of the base64 encoding of a hex encoded string'''
    # codecs.encode adds a newline to end of string so we don't use that
    #return codecs.encode(codecs.decode(hex_str, 'hex'), 'base64').decode()
    return b64encode(codecs.decode(hex_str, 'hex'))


if __name__ == '__main__':
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64_expected =b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    b64_calc = hex2base64(hex_str)
    print(b64_calc)
    assert(b64_calc == b64_expected)
