# Primality testing based on Euler's Criterion

from ..Polynomials import JacobiSymbol
from ..Algorithms import FastPower
from random import randint

def EulerTest(a, n):
  '''
  Performs the Euler Test to see if Euler's Criterion holds such that a^((n-1)/2) is congruent to the Jacobi Symbol of a mod n\n
  Inputs:
    integers a, n
  Output:
    boolean e (false if composite, true if "probably prime")
  '''
  e = FastPower(a, (n-1)//2, n) == JacobiSymbol(a, n)
  return e

def SolovayStrassenTest(n, tries=10):
  '''
  Performs the Solovay-Strassen Test on possible prime n\n
  Inputs:
    integers n, tries (optional, default: 10)
  Outputs:
    boolean s (false if composite, true if "probably prime")
  '''
  # Use EulerTest to test random integers from 2 to n
  if tries > n - 2:
    # There aren't enough possible values to try which are coprime to n
    # ERROR
    return None
  for i in range(tries):
    if not EulerTest(randint(2, n+1), n):
      # Found a witness for the compositeness of n
      return False

  return True