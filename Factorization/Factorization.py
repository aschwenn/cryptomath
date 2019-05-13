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
def Factor(n):
  '''
  Returns a list of the factors of n
  Input:
    integer n
  Output:
    list of integers f
  '''
  print('Function Factor(n) not yet implemented')

  # Using the following link for guidance...
  # https://stackoverflow.com/questions/2267146/what-is-the-fastest-factorization-algorithm

  def FactorRecursive(n):
    length = floor(log10(n))
    print(length)

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

    factor2 = floor(n / factor)
    if IsPrime(factor2):
      return [factor, factor2]
    else:
      return [factor, Factor(factor2)]

  factors = FactorRecursive(n)
  factors.append(1)
  factors.append(n)
  print(factors)
  factors.sort()

  return factors