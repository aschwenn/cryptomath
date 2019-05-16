# Polynomial operations in modular arithmetic

from ..Algorithms import GCD
from ..Primality import IsPrime
from ..Factorization import PrimeFactorizationSmall
from math import sqrt, floor
from ..Algorithms import FastPower

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

      # (-3/n) gives +1 for n = 1 mod 6, -1 for n = 5 mod 6
      elif a == n - 3:
        if n % 6 == 1:
          return 1
        elif n % 6 == 5:
          return -1

      # (5/n) gives +1 for n = 1,9 mod 10, -1 for n = 3,7 mod 10
      elif a == 5:
        if n % 10 == 1 or n % 10 == 9:
          return 1
        elif n % 10 == 3 or n % 10 == 7:
          return -1
      
      # if a,n odd, (a/n) gives -(n/a) if a,n = 3 mod 4, (n/a) otherwise
      elif a % 2 == 1:
        if a % 4 == 3 and n % 4 == 3:
          return LegendreSymbol(n, a) * -1
        else:
          return LegendreSymbol(n, a)

      # (ab/n) = (a/n)(b/n)
      elif not IsPrime(a):
        factorization = PrimeFactorizationSmall(a)
        parts = []
        for fac in factorization:
          if fac[1] % 2 == 0:
            # factor is a square, symbol is 1
            continue
          else:
            for i in range(fac[1]):
              parts.append(fac[0])
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
    factorization = PrimeFactorizationSmall(n)
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

def TonelliShanks(a, n):
  '''
  Performs the Tonelli-Shanks algorithm to find modular square roots for a mod n\n
  Inputs:
    integers a, n
  Output:
    integers x1, x2
  '''
  if JacobiSymbol(a, n) == -1:
    # There are no square roots for a mod n
    raise Exception('JacobiSymbol(): ' + str(a) + ' does not have square roots mod ' + str(n))
  s = 0
  m = n - 1
  while m % 2 == 0:
    m = m // 2
    s += 1
  # Select z such that (z/p) = -1
  z = 2
  while JacobiSymbol(z, n) == 1:
    z += 1
  # Set initial values
  e = s
  c = FastPower(z, m, n)
  x = FastPower(a, (m + 1) // 2, n)
  t = FastPower(a, m, n)
  while e != 0:
    print('e:',e,'t:',t)
    # Find the smallest i < e such that t^(2^i) = 1 mod n
    i = 1
    while FastPower(t, 2 ** i, n) != 1:
      i += 1
    # Set values
    b = FastPower(2, e - i - 1, n)
    x = b * x % n
    c = FastPower(b, 2, n)
    t = t * c % n
    e = i
  return x, n-x

def ModSquareRoots(a, n):
  '''
  If a is a quadratic residue mod n, return its square roots\n
  Inputs:
    integers a, n
  Output:
    integers r1, r2
  '''
  if JacobiSymbol(a, n) == -1:
    # There are no square roots for a mod n
    raise Exception('ModSquareRoots(): ' + str(a) + ' does not have square roots mod ' + str(n))

  # Check for 3 mod 4 (1 mod 8 and 7 mod 8) shortcut
  if n % 4 == 3:
    x = FastPower(a, (n + 1) // 4, n)
    return x, n-x

  # Check for 5 mod 8 shortcut
  if n % 8 == 5:
    k = n // 8
    if FastPower(a, (n - 1) // 4, n) == 1:
      x = FastPower(a, k + 1, n)
    else:
      x = FastPower(2, 2 * k + 1, n) * FastPower(a, k + 1, n)
      x = x % n
    return x, n-x

  # If 1 mod 8, perform Tonelli-Shanks
  if n % 8 == 1:
    return TonelliShanks(a, n)

  # Hensel's Lemma?

  return 0, 0