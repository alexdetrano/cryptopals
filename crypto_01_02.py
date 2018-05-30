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
def hex2bytearray(s):
    """convert a hex-encoded string to bytearray"""
    return(bytearray.fromhex(s))

def bytearray2hex(b):
    """convert a bytearray object to a hex-encoded string"""
    return(b.hex())

def print_bytearray(b):
    """print a bytearray as an ascii-encoded string, replacing non-ascii with string escape"""
    print(b.decode('ascii', 'replace'))

def xor(x,y):
    """xor 2 buffers of equal length

    raises ValueError if buffers are not equal in length
    """
    if len(x) != len(y):
        raise ValueError('Buffer lengths not equal. lenths = {}, {}'.format(len(x), len(y)))
    return(bytearray(b[0] ^ b[1] for b in zip(bytearray(x),bytearray(y))))

if __name__ == '__main__':
    my_str ='1c0111001f010100061a024b53535009181c'
    key ='686974207468652062756c6c277320657965'
    expected ='746865206b696420646f6e277420706c6179'
    calc = xor(hex2bytearray(my_str), hex2bytearray(key))
    print_bytearray(calc)
    assert(expected == bytearray2hex(calc))

