# Factoring numbers using various techniques

from .Pollard import Pollard
from .Lenstra import Lenstra
from .QuadraticSieve import QuadraticSieve
from math import log10, floor
from ..Primality import IsPrime

#TODO
def PrimeFactorization(n):
  '''
  Returns a list of the prime factorization of n, giving factors and exponents
  Input:
    integer n
  Output:
    list of tuples of integers (factor, exponent)
  '''
  print('Function PrimeFactorization(n) not yet implemented')
  return []

#TODO
def Factors(n, dup=False):
  '''
  Returns a list of the factors of n
  Input:
    integer n
    (optional) dup - include duplicate factors
  Output:
    list of integers f
  '''
  # Using the following link for guidance...
  # https://stackoverflow.com/questions/2267146/what-is-the-fastest-factorization-algorithm

  if IsPrime(n):
    return [n]

  def FactorRecursive(n):
    length = floor(log10(n))
    #print('Recursive: factoring ' + str(n) + ', ' + str(length) + ' digits')

    if length <= 21:
      # Use Pollard's
      factor = Pollard(n)
    elif length <= 50:
      # Use Lenstra's
      factor = Lenstra(n)
    elif length <= 100:
      # Use Quadratic Sieve
      factor = QuadraticSieve(n)
    else:
      # Use General Number Field Sieve
      print('Number is too big to factor')
      return []

    if factor == -1:
      # ERROR
      # Failure to find a factor
      return []

    factor2 = n // factor
    if IsPrime(factor2):
      #print('Result: ' + str(factor) + ',' + str(factor2) + ', both prime')
      return [factor, factor2]
    else:
      #print('Result: ' + str(factor) + ',' + str(factor2) + ', not both prime')
      return [factor] + FactorRecursive(factor2)

  factors = FactorRecursive(n)
  factors.sort()

  if dup:
    return factors

  factors2 = []
  for f in factors:
    if not f in factors2:
      factors2.append(f)

  return factors2