# Functions relating to primitive roots
from ..Polynomials import JacobiSymbol
from ..Primality import IsPrime
from ..Factorization import Factors
from ..Algorithms import FastPower, GCD

#TODO
def Order(a, n):
  '''
  Computes orda(n), or the smallest integer m such that a^m = 1 (mod n)\n
  Inputs:
    integers a, n
  Output:
    integer ord
  '''

#TODO
def IsPrimRoot(g, p, fact=[]):
  '''
  Computes whether g is a primitive root p, or if Order(g, p) returns p-1
  Inputs:
    integers g, p
    list of integers fact (optional)
  Output:
    boolean pr
  '''
  if JacobiSymbol(g, p) != -1 or g == 0:
    return False
  if IsPrime(p):
    # Usual case
    if len(fact) == 0:
      fact = Factors(p-1)
    for f in fact:
      if FastPower(g, (p-1)//f, p) == 1:
        return False
    return True
  else:
    # Can only be a prim root if the modulo is of the form 
    # p^k or 2p^k with an odd prime

    return False

#TODO
def PrimRoots(p):
  '''
  Find all primitive roots for p
  Input:
    integer p
  Output:
    list of integers
  '''
  # There should be exactly phi(phi(p)) primitive roots
  if IsPrime(p):
    # Find one primitive root
    r = 2
    fact = Factors(p-1)
    while not IsPrimRoot(r, p, fact):
      r += 1
    roots = [r]
    for i in range(p-1):
      if GCD(i, p-1) == 1:
        x = FastPower(r, i, p)
        if not x in roots:
          roots.append(x)
    roots.sort()
    return roots
  else:
    if p == 2:
      return [1]
    elif p == 4:
      return [3]
    # ...
    raise('PrimRoots() function has not yet been completed')
