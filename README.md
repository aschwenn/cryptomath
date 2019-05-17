# cryptomath
Mathematical cryptography algorithms implemented in Python

### Usage
Usage documentation will come later once the project is more complete, but for now, here's a basic overview:

Create a python script in the directory above this library and use `import cryptomath` to import the entire library. From here, any completed functions can be accessed by referencing the library and function name, such as `gcd = cryptomath.GCD(123,943)`, or `gcd, x, y = cryptomath.ExtendedEuclidean(123, 10007)`.
To import only a specific module within the library, such as `Factorization`, you may use `from cryptomath import Factorization`. Then, the library will not need to be referenced, only the function names, such as `fact = PrimeFactorization(1234)`. Similarly, you may import only one function of a module, which can be done with `from cryptomath.Polynomials import JacobiSymbol`.

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
* Pollard's p-1

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
