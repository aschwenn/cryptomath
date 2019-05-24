# cryptomath
Mathematical cryptography algorithms implemented in Python

### Usage
Usage documentation will come later once the project is more complete, but for now, here's a basic overview:

Create a python script in the directory above this library and use `import cryptomath` to import the entire library. From here, any completed functions can be accessed by referencing the library and function name, such as `gcd = cryptomath.GCD(123,943)`, or `gcd, x, y = cryptomath.ExtendedEuclidean(123, 10007)`.
To import only a specific module within the library, such as `Factorization`, you may use `from cryptomath import Factorization`. Then, the library will not need to be referenced, only the function names, such as `fact = PrimeFactorization(1234)`. Similarly, you may import only one function of a module, which can be done with `from cryptomath.Polynomials import JacobiSymbol`.

### Usable Functions
These are functions which have been finalized and can be effectively used:

##### Basic Algorithms
`Euclidean(a, b)`, Alias: `GCD(a, b)`
Find the GCD of a, b using the Euclidean Algorithm
  Inputs:
    integers a, b
  Outputs:
    integer GCD
`ExtendedEuclidean(a, b)`
If the GCD of a, b is 1, find x, y such that ax + by = 1
  Inputs:
    integers a, b
  Outputs:
    integers GCD, x, y
`ModularInv(a, n, prime)`
Computes the modular inverse of a mod n\n
  Inputs:
    integers a, n
    (optional) boolean prime
  Outputs:
    integer aInv

##### Misc
`HammingWeight(x)`
Determines the Hamming Weight of an integer, or the number of 1s in the binary representation of that number
  Input:
    integer x
  Output:
    integer h

### Dev notes
* SHOULD ADD: check that inputs are integers in every function
* Use 'secrets' instead of 'random' for cryptographically secure random number generation: https://docs.python.org/3/library/secrets.html
* On parallelization of random number generation: https://ieeexplore.ieee.org/document/5547156

### Possible algorithms to implement

##### Basic
* Euclidean - done
* Extended Euclidean - done
* Fast-Powering - done
* Modular Inverse - done
* Chinese Remainder Theorem - done
* Totient function - done

##### Polynomials
* Jacobi/Legendre Symbols - done
* Tonneli-Shanks - done
* Hensel's Lemma
* Modular Quadratic Solver
* 3 mod 4 Square Root Shortcut - done

##### Primality Tests
* Fermat Test - done
* Euler's Criterion - done
* Solovay-Strassen - done
* Miller-Rabin - done

##### Ciphers
* Rabin Cipher
* Affine Cipher

##### Discrete Logs
* Pohlig-Hellman
* Shanks Babystep-Giantstep

##### Generators
* Primitive Roots
* Large Primes - done
* Sophie Germain Strong Primes

##### Cryptosystems
* McEliece Public Key
* El Gamal
* RSA
* Merkle-Hellman
* Koblitz (elliptic Curves)

##### Factoring
* Quadratic Sieve
* Lenstra's Algorithm (elliptic curves)
* Pollard's p-1 - done

##### Secret Sharing
* Blakely (hyperplanes)
* Shamir (points)

##### Zero-knowledge Protocols
* Basic
* Fiege-Fiat-Shamir

##### Elliptic Curves
* Check if Point is on a Curve
* Add Points
* Point-Scalar Multiplication
* Diffie-Hellman
* RSA
* El Gamal
