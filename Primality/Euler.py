# Primality testing based on Euler's Criterion

from ..Polynomials import JacobiSymbol

def EulerTest(a, n):
  '''
  Performs the Euler Test to see if Euler's Criterion holds such that a^((n-1)/2) is congruent to the Jacobi Symbol of a mod n\n
  Inputs:
    integers a, n
  Output:
    boolean e (false if composite, true if "probably prime")
  '''
  e = FastPower(a, (n-1)/2, n) == JacobiSymbol(a, n)
  return e

#TODO
def SolovayStrassenTest(n, tries=10):
  '''
  Performs the Solovay-Strassen Test on possible prime n\n
  Inputs:
    integers n, tries (optional, default: 10)
  Outputs:
    boolean s (false if composite, true if "probably prime")
  '''
  return 0