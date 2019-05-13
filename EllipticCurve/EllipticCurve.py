#Elliptic Curve objects with corresponding functions

#Point Object
class Point
    def __init__(self, x, y)
        self.__x = x
        self.__y = y

    def set(self, otherPoint)
        self.__x = otherPoint.__x
        self.__y = otherPoint.__y

    def set(self, x, y)
        self.__x = x
        self.__y = y

    def getX(self)
        return self.__x

    def getY(self)
        return self.__y


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
    def __init__(self, A, B)
        if (4*(A**3) + 27*(B**2)) = 0
            raise ValueError ('Error: 4A^3 + 27B^2 = 0 (Curve isn\'t non-singular)')
        self.__A = A
        self.__B = B

    def addPoint(self, firstPoint, secondPoint)
        if firstPoint.x == secondPoint.y
            if firstPoint.y == -secondPoint.y

            else

    def doublePoint(self, firstPoint)
        return self.addPoint(firstPoint, firstPoint)

    
