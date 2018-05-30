from base64 import b64encode


def hex2bytearray(s):
    """convert a hex-encoded string to bytearray"""
    return(bytearray.fromhex(s))

def bytearray2hex(b):
    """convert a bytearray to a hex-encoded string"""
    return(b.hex())

def print_bytearray(b):
    """print a bytearray as an ascii-encoded string, replacing non-ascii with string escape code"""
    print(b.decode('ascii', 'replace'))

def hex2base64(s):
    """convert a hex-encoded string to a base64-encoded bytes object"""
    return(b64encode(hex2bytearray(s)))

def xor(x,y):
    """xor 2 buffers of equal length

    raises ValueError if buffers are not equal in length
    """
    if len(x) != len(y):
        raise ValueError('Buffer lengths not equal. lenths = {}, {}'.format(len(x), len(y)))
    return(bytearray(b[0] ^ b[1] for b in zip(bytearray(x),bytearray(y))))
