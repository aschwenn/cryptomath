# Implementation of Pollard's rho algorithm for factoring integers

from ..Primality.primes import *
from math import floor, log
from ..Algorithms import FastPower, GCD
from random import randint

def PollardP_1(n, b=0):
  '''
  Finds a nontrivial factor of n using Pollard's p-1 algorithm\n
  Inputs:
    integer n
    (optional) smoothness bound b, should be < 10000
  Output:
    integer f (a single factor) (-1 indicates a failure to find a factor)
  '''

  # https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm

  TRIAL_As = 100
  
  # Performs computation of Pollard's p-1
  # returns factor, current product (m), and last prime used in product
  def pollardInternal(n, b, m=1, startPrime=2):
    # Compute m = product of qi^(logqi B) where qi are primes <= b
    if startPrime == 2:
      i = -1
    else:
      i = smallPrimes.index(startPrime) # starting point to grab primes
    while smallPrimes[i] < b:
      i += 1
      m *= smallPrimes[i] ** floor(log(b, smallPrimes[i]))
    endPrime = smallPrimes[i]
    # pick 'a' coprime to n, can always use 2
    g = GCD(FastPower(2, m, n) - 1, n)
    if g == 1 or g == n:
      for i in range(TRIAL_As):
        # Pick another a coprime to n
        x = randint(3, n)
        gx = GCD(x,n)
        if gx != 1:
          return gx
        g = GCD(FastPower(x, m, n) - 1, n)
        if g > 1 and g < n:
          return g, m, endPrime
      return -1, m, endPrime
    else:
      return g, m, endPrime

  if n % 2 == 0:
    return 2
  if b > 0 and b < 10000:
    factor, product, endPrime = pollardInternal(n, b)
    return factor
  elif b > 10000:
    # ERROR
    # try to use a smaller b...
    return -1
  else:
    # No bound is defined, try different bounds to get a factor
    multiplier = 10000 if (n > 10000) else n
    product = 1
    endPrime = 2
    for i in range(50,0,-5):
      factor, product, endPrime = pollardInternal(n, floor(multiplier / i), product, endPrime)
      if factor > 1:
        return factor

    factor, product, endPrime = pollardInternal(n, 10000, product, endPrime)
    if factor > 1:
      return factor

  return -1

def Pollard(n):
  '''
  Finds a nontrivial factor of n using Pollard's rho algorithm\n
  Input:
    integer n
  Output:
    integer f (a single factor) (-1 indicates a failure to find a factor)
  '''

  def poly(x):
    return (x ** 2 + 1) % n

  x = 2
  y = 2
  g = 1
  while g == 1:
    x = poly(x)
    y = poly(poly(y))
    g = GCD(abs(x - y), n)
  if g == n:
    return -1
  return g

def FactorSmall(n):
  '''
  Returns a list of the factors of n, where n is assumed to be less than 10^50\n
  Input:
    integer n
  Output:
    list of integers f
  '''
  print('Function FactorSmall(n) not yet implemented')
  return []

def PrimeFactorizationSmall(n):
  '''
  Returns a list of the prime factorization of n, giving factors and exponents, where n is assumed to be less than 10^50\n
  Input:
    integer n
  Output:
    list of tuples of integers (factor, exponent)
  '''
  print('Function PrimeFactorizationSmall(n) not yet implemented')
  return []