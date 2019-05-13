#Elliptic Curve objects with corresponding functions

from Algorithms

#Point Object
class Point
    def __init__(self, x, y, inf = False)
        self.__x = x
        self.__y = y
        self.__inf = inf

    def set(self, otherPoint)
        self.__x = otherPoint.__x
        self.__y = otherPoint.__y
        self.__inf = otherPoint.__inf

    def set(self, x, y, inf = False)
        self.__x = x
        self.__y = y
        self.__inf = inf

    def getX(self)
        return self.__x

    def getY(self)
        return self.__y

    def getInf(inf)
        return self.__inf

    def __add__(self, otherPoint)
        return Point(self.__x + otherPoint.x, self.__y + otherPoint.y)

    def __sub__(self, otherPoint)
        return Point(self.__x - otherPoint.x, self.__y - otherPoint.y)

    def __mul__(self, multiplicand)
        return Point(self.__x * multiplicand, self.__y * multiplicand)

    def __truediv__(self, quotient)
        return Point(self.__x / quotient, self.__y / quotient)

#Elliptic Curve of form y^2 = x^3 + Ax + B
class EllipticCurve
    def __init__(self, A, B, m = 0)
        if (4*(A**3) + 27*(B**2)) = 0
            raise ValueError ('Error: 4A^3 + 27B^2 = 0 (Curve isn\'t non-singular)')
        self.__A = A
        self.__B = B

    def addPoint(self, firstPoint, secondPoint)
        if firstPoint.x == secondPoint.x
            if firstPoint.y == -secondPoint.y
                return Point(0, 0, True)
            else if firstPoint.y == secondPoint.y
                slopeNum = (3*(firstPoint.x**2) + self.A)
                if m == 0 #Non-Modular Curve
                    slopeDen = 
                else #Modular Curve





    def doublePoint(self, firstPoint)
        return self.addPoint(firstPoint, firstPoint)

    
