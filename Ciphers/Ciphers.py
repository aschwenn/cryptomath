from ..utils import type_assert

# Basic cryptographic ciphers

#TODO
def RabinCipher():
  return 0

# I haven't done enough research on the Rabin cryptosystem yet
# https://en.wikipedia.org/wiki/Rabin_cryptosystem

#TODO
@type_assert(int, int, int, int)
def AffineEncrypt(m: int, a: int, b: int, n: int):
  '''
  Encrypts a message m using the affine cipher: c = am + b mod n\n
  Inputs:
    string m (message)
    integers a, b, n (alphabet length)
  Output:
    string c (ciphertext)
  '''
  print('Function AffineEncrypt(m, a, b, n) not yet implemented')
  return 0

#TODO
@type_assert(int, int, int, int)
def AffineDecrypt(c: int, a: int, b: int, n: int):
  '''
  Decrypts a ciphertext c using the affine cipher: m = (c - b)a^-1 mod n\n
  Inputs:
    string c (ciphertext)
    integers a, b, n (alphabet length)
  Output:
    string m (message)
  '''
  print('Function AffineDecrypt(c, a, b, n) not yet implemented')
  return 0