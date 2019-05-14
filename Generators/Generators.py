# Number generators

from ..Primality import MillerRabin
import random
import threading

import secrets

possibleNum = 0

count = 0

def genNum(length, lock):
  rand = random.Random()
  rand.seed()
  global possibleNum
  global count
  while not possibleNum:
    x = random.randint(2 ** (length - 1), 2 ** (length) - 1)
    lock.acquire()
    try:
      count += 1
    finally:
      lock.release()
    if MillerRabin(x):
      lock.acquire()
      try:
        possibleNum = x
      finally:
        lock.release()

def GenerateProbablePrime(length):
  '''
  Generates a random prime number of a specified binary length
  Input:
    integer length
  Output:
    integer p
  '''
  global possibleNum
  global count
  possibleNum = 0 # reset
  lock = threading.Lock() # mutex lock to prevent race conditions
  threadNum = 2 # number of threads to spawn to generate number/primality pairs

  # Create list of threads
  threads = [threading.Thread(daemon=True, target=genNum, args=(length,lock)) for i in range(threadNum)]
  # Execute threads concurrently
  [thread.start() for thread in threads]
  [thread.join() for thread in threads]

  print('Count: ' + str(count))

  return possibleNum

def GenerateProbablePrimeNonThreaded(length):
  '''
  Generates a random prime number of a specified binary length, not multithreaded
  Input:
    integer length
  Output:
    integer p
  '''
  count = 0
  while True:
    x = random.randint(2 ** (length - 1), 2 ** (length) - 1)
    count += 1
    if MillerRabin(x):
      print('Count: ' + str(count))
      return x