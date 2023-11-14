from dataclasses import dataclass

from math import sqrt

@dataclass
class Point:
    x: float
    y: float
    
def Heron(A,B,C):
    lenght1=sqrt((A.x-B.x)**2+(A.y-B.y)**2)
    lenght2=sqrt((A.x-C.x)**2+(A.y-C.y)**2)
    lenght3=sqrt((C.x-B.x)**2+(C.y-B.y)**2)
    HPerimeter=(lenght3+lenght2+lenght1)/2
    Square=sqrt(HPerimeter*(HPerimeter-lenght1)*(HPerimeter-lenght2)*(HPerimeter-lenght3))
    return (round(Square,3))

A=Point(1,1)
B=Point(3,1)
C=Point(1.5,2.5)
assert Heron(A,B,C)==1.5

A=Point(4,2)
B=Point(6,2)
C=Point(4,4)
assert Heron(A,B,C)==2


