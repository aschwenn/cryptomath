# cryptomath
Mathematical cryptography algorithms implemented in Python

### Dev notes
* I haven't implemented exception handling yet, so everywhere I'll want to raise an exception is marked with an 'ERROR' comment
* Use 'secrets' instead of 'random' for cryptographically secure random number generation: https://docs.python.org/3/library/secrets.html
* On parallelization random number generation: https://ieeexplore.ieee.org/document/5547156

### Possible algorithms to implement

##### Basic
* Euclidean - done
* Extended Euclidean - done
* Fast-Powering - done
* Modular Inverse - done
* Chinese Remainder Theorem - done
* Totient function

##### Polynomials
* Jacobi/Legendre Symbols - done
* Tonneli-Shanks
* Hensel's Lemma
* Modular Quadratic Solver
* 3 mod 4 Square Root Shortcut

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
