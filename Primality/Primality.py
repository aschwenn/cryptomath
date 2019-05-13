# Probablistic primality testing

from ..Algorithms import FastPower
from math import log10
from .primes import *

def FermatTest(a, n):
  '''
  Peforms the Fermat Test to see if Fermat's Little Theorem holds for a^(n-1) = 1 mod n\n
  Inputs:
    integers a, n
  Output:
    boolean f (false if composite, true if "probably prime")
  '''
  f = FastPower(a, n-1, n)
  return f == 1

#TODO
def MillerRabin(n, tries=10, base=[]):
  '''
  Performs the Miller-Rabin Test on possible prime n\n
  Inputs:
    integers n, tries (optional, default: 10)
    integer list base (optional)
  Outputs:
    boolean m (false if composite, true if "probably prime")
  '''
  print('Function MillerRabin(n) not yet implemented')

  #https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Accuracy
  return 0

#TODO
def IsPrime(n):
  '''
  Determines probabalistically if a number is prime\n
  Input:
    integer n
  Outputs:
    boolean p (false if composite, true if "probably prime")
  '''

  if n % 2 == 0 and n != 2:
    return False

  length = log10(n)

  if length < 4:
      # Use lookup table
      if n in smallPrimes:
        return True
      else:
        return False
  else:

    #temporary solution
    return FermatTest(2,n) and FermatTest(3,n) and FermatTest(5,n) and FermatTest(7,n) and FermatTest(11,n)

    base = []
    # Call to Miller-Rabin

    print('Function IsPrime(n) not yet implemented')
    return True