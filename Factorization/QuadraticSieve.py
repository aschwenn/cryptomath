# Implementation of the Quadratic Sieve algorithm

from math import exp, floor, sqrt, log10
from ..Primality import IsPrime
from ..Polynomials import JacobiSymbol
from ..Generators import GeneratePrimes

base = []
table = []

def QuadraticSieve(n):
  '''
  Finds a nontrivial factor of n using the Quadratic Sieve algorithm\n
  Input:
    integer n
  Output:
    integer f (a single factor)
  '''
  raise Exception('Function QuadraticSieve() not yet implemented')
  return 0

def NaiveQuadraticSieve(n):
  global base

  # Set bounds for factor base
  B = floor(L(n) ** (1/sqrt(2)))
  # Create factor base
  beta = GeneratePrimes(B)
  # Remove quadratic nonresidues
  base = [b for b in beta if JacobiSymbol(b, n) == 1]
  # Get estimate for values to look around
  x = floor(sqrt(n))
  table = []
  # Begin looking...
  #while True:
  #  y = 


def L(x):
  return exp(sqrt(log10(x) * log10(log10(x))))
