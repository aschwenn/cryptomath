# Probablistic primality testing

from ..Algorithms import FastPower

def FermatTest(a, p):
  f = FastPower(a, p-1, p)
  return f == 1