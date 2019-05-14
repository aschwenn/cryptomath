#Elliptic Curve objects with corresponding functions

#Until I figure out importing, I'm just going to copy ExtendedEuclidean into here
#from ..Algorithms import ExtendedEuclidean
def ExtendedEuclidean(a, b):
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

#Point Object
class Point:
    def __init__(self, x, y, inf = False):
        self.x = x
        self.y = y
        self.inf = inf

    def set(self, otherPoint):
        self.x = otherPoint.x
        self.y = otherPoint.y
        self.inf = otherPoint.inf

    def set(self, x, y, inf = False):
        self.x = x
        self.y = y
        self.inf = inf

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)

    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)

    def __mul__(self, multiplicand):
        return Point(self.x * multiplicand, self.y * multiplicand)

    def __truediv__(self, quotient):
        return Point(self.x / quotient, self.y / quotient)

#Elliptic Curve of form y^2 = x^3 + Ax + B
class EllipticCurve:
    def __init__(self, A, B, N = 0):
        if (4*(A**3) + 27*(B**2)) == 0:
            
            raise ValueError('Error: 4A^3 + 27B^2 = 0 (Curve isn\'t non-singular)')
        self.A = A
        self.B = B
        self.N = N

    def checkPoint(self, point):
        #Check y^2 = x^3 + Ax + B
        if N == 0:
            return (point.y**2) == (point.x**3 + A*point.x + B)
        else:
            return ((point.y**2) % N) == ((point.x**3 + A*point.x + B) % N) 

    def addPoint(self, firstPoint, secondPoint):
        #Check if points lie on the curve
        if ~self.checkPoint(firstPoint):
            raise ValueError('First point not on the curve: ({}, {})'.format(firstPoint.x, firstPoint.y))
        if ~self.checkPoint(secondPoint):
            raise ValueError('Second point not on the curve: ({}, {})'.format(secondPoint.x, secondPoint.y))


        #Points at the same X-coordinate
        if firstPoint.x == secondPoint.x:
            if firstPoint.y == -secondPoint.y:
                return Point(0, 0, True) #Point at infinity
            elif firstPoint.y == secondPoint.y:
                slopeNum = (3 * (firstPoint.x ** 2) + self.A)
                slopeDen = 2 * y
                if N == 0: #Non-Modular Curve
                    slope = slopeNum / slopeDen
                else: #Modular Curve
                    _dummy1, invSlopeDen, _dummy2 = ExtendedEuclidean(N, slopeDen % N) 
                    slope = (slopeNum * invSlopeDen) % N
        else:
            return Point(0, 0)





    def doublePoint(self, firstPoint):
        return self.addPoint(firstPoint, firstPoint)

    
