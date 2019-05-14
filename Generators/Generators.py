# Number generators

from ..Primality import MillerRabin
from random import randint

#TODO
def GenerateProbablePrime(length, truerandom=True):
  '''
  Generates a random prime number of a specified binary length
  Input:
    integer length
  Output:
    integer p
  '''
  x = randint(2 ** (length - 1), 2 ** (length) - 1)
  while True:
    if truerandom:
      x = randint(2 ** (length - 1), 2 ** (length) - 1)
    else:
      if x + 2 > (2 ** (length) - 1):
        x = randint(2 ** (length - 1), 2 ** (length) - 1)
      else:
        x = (x+2) if (x%2!=0) else (x+1)
    if MillerRabin(x):
      return x
