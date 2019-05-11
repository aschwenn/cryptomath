# Functions using Fermat's Theorem

# Test to see if the package is set up correctly...

def FermatTest(a, p):
  # Naive implementation, fix later
  f = a ** (p-1) % p
  return f == 1