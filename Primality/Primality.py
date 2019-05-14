# Probablistic primality testing

from ..Algorithms import FastPower
from math import log10, log, floor
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
def MillerRabin(n, warnings=False):
  '''
  Performs the Miller-Rabin Test on possible prime n\n
  Input:
    integers n
    boolean warnings (optional, show warnings)
  Outputs:
    boolean m (false if composite, true if "probably prime")
  '''
  #https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Accuracy
  
  # If the generalized Riemann hypothesis is true, Miller-Rabin can be made deterministic
  if not n > 1:
    raise Exception('MillerRabin(n): n must be strictly greater than 1')
  # Express as n = 2^r*d + 1
  np = n - 1
  r = 0
  while np % 2 == 0:
    r += 1
    np = np // 2
  d = np
  
  witnessRange = min([n-2, floor(2*(log(n)**2))])
  aIndex = 0
  while smallPrimes[aIndex] < witnessRange:
    x = FastPower(smallPrimes[aIndex], d, n)
    if x == 1 or x == n-1:
      # Failure to find a witness
      aIndex += 1
      if aIndex == len(smallPrimes):
        if warnings:
          print('List of small primes for Miller-Rabin bases has been exhausted for n=' + str(n))
          print('The result is probabalistically determined to be prime.')
        return 1
      continue
    else:
      for i in range(r - 1):
        x = FastPower(x, 2, n)
        if x == n-1:
          # Failure to find a witness
          aIndex += 1
          if aIndex == len(smallPrimes):
            if warnings:
              print('List of small primes for Miller-Rabin bases has been exhausted for n=' + str(n))
              print('The result is probabalistically determined to be prime.')
            return 1
          continue
    return 0
  return 1

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