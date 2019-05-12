# Basic cryptographic ciphers

#TODO
def RabinCipher():
  return 0

# I haven't done enough research on the Rabin cryptosystem yet
# https://en.wikipedia.org/wiki/Rabin_cryptosystem

#TODO
def AffineEncrypt(m, a, b, n):
  '''
  Encrypts a message m using the affine cipher: c = am + b mod n
  Inputs:
    string m (message)
    integers a, b, n (alphabet length)
  Output:
    string c (ciphertext)
  '''
  return 0

#TODO
def AffineDecrypt(c, a, b, n):
  '''
  Decrypts a ciphertext c using the affine cipher: m = (c - b)a^-1 mod n
  Inputs:
    string c (ciphertext)
    integers a, b, n (alphabet length)
  Output:
    string m (message)
  '''
  return 0