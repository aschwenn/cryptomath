# Important algorithms for cryptography

def Euclidean(a, b):
  '''
  Find the GCD of two numbers using the Euclidean Algorithm\n
  Inputs:
    integers a, b
  Outputs:
    integer GCD
  Runtime: O(log(min(a,b)))
  '''
  if a == 0:
    return b
  return Euclidean(b % a, a)

def GCD(a, b):
  '''
  Find the GCD of two numbers using the Euclidean Algorithm\n
  Alias of Euclidean(a, b)\n
  Inputs:
    integers a, b
  Outputs:
    integer GCD
  Runtime: O(log(min(a,b)))
  '''
  return Euclidean(a, b)

def ExtendedEuclidean(a, b):
  '''
  If the GCD of a, b is 1, find x, y such that ax + by = 1
  Inputs:
    integers a, b
  Outputs:
    integers GCD, x, y
  '''
  x = 0
  y = 1
  u = 1
  v = 0
  while a != 0:
    # same loop as Euclidean

    # Find q, r in b = qa + r
    q, r = b // a, b % a

    # Update a, b
    a, b = r, a

    # Perform backsubstition, update values
    up, vp = x - u * q, y - v * q
    x, y = u, v
    u, v = up, vp
  return b, x, y

def ModularInv(a, n, prime=False):
  '''
  Computes the modular inverse of a mod n
  Inputs:
    integers a, n
    (optional) boolean prime
  Outputs:
    integer aInv
  '''
  if prime:
    # Use Fermat's Theorem shortcut: a^-1 = a^(p-2) mod p
    return FastPower(a, n-2, n)
  else:
    GCD, x, y = ExtendedEuclidean(a, n)
    if GCD == 1:
      return x % n
    else:
      # ERROR: There is no Modular inverse for a mod n
      return null

def FastPower(a, e, n):
  '''
  Computes the exponentiation of a^e mod n by successive squaring
  Inputs:
    integers a, e, n
  Output:
    integer aPow
  '''
  return pow(a, e, n)