from ..utils import type_assert

# Important algorithms for cryptography

@type_assert(int, int)
def Euclidean(a: int, b: int):
  '''
  Find the GCD of a, b using the Euclidean Algorithm\n
  Inputs:
    integers a, b
  Outputs:
    integer GCD
  Runtime: O(log(min(a,b)))
  '''
  # Iterative so as to not exceed Python recursion depth
  while a != 0:
    temp = a
    a = b % a
    b = temp
  return b

@type_assert(int, int)
def GCD(a: int, b: int):
  '''
  Find the GCD of a, b using the Euclidean Algorithm\n
  Alias of Euclidean(a, b)\n
  Inputs:
    integers a, b
  Outputs:
    integer GCD
  Runtime: O(log(min(a,b)))
  '''
  return Euclidean(a, b)

@type_assert(int, int)
def ExtendedEuclidean(a: int, b: int):
  '''
  If the GCD of a, b is 1, find x, y such that ax + by = 1\n
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

@type_assert(int, int, bool)
def ModularInv(a: int, n: int, prime: bool=False):
  '''
  Computes the modular inverse of a mod n\n
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
      raise Exception('ModularInv: ' + str(a) + ' does not have an inverse mod ' + str(n))

@type_assert(int, int, int)
def FastPower(a: int, e: int, n: int):
  '''
  Computes the exponentiation of a^e mod n by successive squaring\n
  Inputs:
    integers a, e, n
  Output:
    integer aPow
  '''
  return pow(a, e, n)

@type_assert(int, int, int, int)
def ChineseRemainderThm(a: int, m: int, b: int, n: int):
  '''
  Finds one modular congruency x = c mod mn that is equivalent to the linear congruencies x = a mod m, x = b mod n\n
  Inputs:
    integers a, m, b, n
  Outputs:
    integers c, mn
  '''
  g, s, t = ExtendedEuclidean(m, n)
  c = (b * m * s + a * n * t) % (m * n)
  return c, (m * n)



