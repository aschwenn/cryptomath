# Polynomial operations in modular arithmetic

from ..Algorithms import GCD
from ..Primality import IsPrime
from ..Factorization import PrimeFactorization
from math import sqrt, floor

#TODO
def JacobiSymbol(a, n):
  '''
  Finds the Jacobi Symbol (a / n) of an integer a mod n\n
  Inputs:
    integers a, n
  Output:
    integer j in [-1,0,1]
  '''

  def LegendreSymbol(a, n):
    iteration = 0
    while True:
      if n % 2 == 0:
        # Undefined for even n
        # ERROR
        return None

      # Reduce a mod n
      a = a % n

      #Debugging
      #iteration += 1
      #print(str(iteration) + ': (' + str(a) + '/' + str(n) + ')')

      # if a is a square, (a/n) gives +1
      s = sqrt(a)
      if s == floor(s):
        return 1

      # (-1/n) = (-1)^((n-1)/2)
      elif a == n - 1:
        return floor((-1) ** ((n-1)/2))

      # (2/n) gives +1 for n = 1,7 mod 8, -1 for n = 3,5 mod 8
      elif a == 2:
        if n % 8 == 1 or n % 8 == 7:
          return 1
        return -1
      
      # if a,n odd, (a/n) gives -(n/a) if a,n = 3 mod 4, (n/a) otherwise
      elif a % 2 == 1:
        if a % 4 == 3 and n % 4 == 3:
          return LegendreSymbol(n, a) * -1
        else:
          return LegendreSymbol(n, a)

      # (ab/n) = (a/n)(b/n)
      elif not IsPrime(a):
        factorization = PrimeFactorization(a)
        parts = []
        for fac in factorization:
          parts.append(fac[0] ** fac[1])
        symbol = 1
        for p in parts:
          symbol *= LegendreSymbol(p, n)
        return symbol

      else:
        # ERROR
        print('This should not be possible...')
        return None

  if GCD(a, n) > 1:
    return 0
  elif n % 2 == 0:
    # Even mods give an undefined Jacobi Symbol
    # ERROR
    return None
  elif not IsPrime(n):
    # For a composite n, the Jacobi symbol is defined as:
    # (a / n) = (a / p1)^e1 * (a / p2)^e2 * ...
    factorization = PrimeFactorization(n)
    symbol = 1
    for factor in factorization:
      symbol *= LegendreSymbol(a, factor[0]) ** factor[1]
    return symbol
  else:
    return LegendreSymbol(a, n)

def IsModSquare(a, n):
  '''
  Determines if a is a square mod n\n
  Inputs:
    integers a, n
  Output:
    boolean s
  '''
  return JacobiSymbol(a, n) == 1

#TODO
def ModSquareRoots(a, n):
  '''
  If a is a quadratic residue mod n, return its square roots\n
  Inputs:
    integers a, n
  Output:
    integers r1, r2
  '''
  print('Function ModSquareRoots(n) not yet implemented')

  if JacobiSymbol(a, n) == -1:
    # There are no square roots for a mod n
    # ERROR
    return None

  # Check for 3 mod 4 shortcut

  # Else, perform Tonneli-Shanks

  # Hensel's Lemma?

  return 0