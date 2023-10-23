from ..utils import type_assert

# Implementation of the Pohlig-Hellman discrete logarithm solver


@type_assert(int, int, int)
def PohligHellman(a: int, b: int, n: int):
  '''
  Solves the discrete logarithm a^x = b mod n using Pohlig-Hellman
  Inputs:
    integers a, b, n
  Output:
    integer x
  '''
  print('Function PohligHellman(a, b, n) not yet implemented')
  return None