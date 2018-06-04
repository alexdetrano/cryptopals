#!/usr/bin/env python
"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""
from utils import *

if __name__ == '__main__':
    my_str ='1c0111001f010100061a024b53535009181c'
    key ='686974207468652062756c6c277320657965'
    expected ='746865206b696420646f6e277420706c6179'
    calc = xor_eq_len(hex2bytes(my_str), hex2bytes(key))
    print_bytes(calc)
    assert(expected == bytes2hex(calc))

