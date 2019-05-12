# Polynomial operations in modular arithmetic

#TODO
def JacobiSymbol(a, n):
  '''
  Finds the Jacobi Symbol of an integer a mod n\n
  Inputs:
    integers a, n
  Output:
    integer j in [-1,1]
  '''
  return 0

def IsSquare(a, n):
  '''
  Determines if a is a square mod n\n
  Inputs:
    integers a, n
  Output:
    boolean s
  '''
  return JacobiSymbol(a, n) == 1

#TODO
def SquareRoots(a, n):
  '''
  If a is a quadratic residue mod n, return its square roots\n
  Inputs:
    integers a, n
  Output:
    integers r1, r2
  '''
  if JacobiSymbol(a, n) == -1:
    # There are no square roots for a mod n
    # ERROR
    return null

  # Check for 3 mod 4 shortcut

  # Else, perform Tonneli-Shanks

  # Hensel's Lemma?

  return 0