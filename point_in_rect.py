from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    
@dataclass
class Rect:
    l:float
    r:float
    t:float
    b:float


def point(rect,C):#определение того, принадлежит ли точка прямоугольнику, диагональю которого является отрезок
    if rect.l!=rect.r and rect.t!=rect.b:
        if rect.l<=C.x<=rect.r and rect.b<=C.y<=rect.t:
            return True
        else:
            return False

    elif rect.l==rect.r and C.x==rect.l and rect.b<=C.y<=rect.t:
        return True

    elif rect.t==rect.b and C.y==rect.t and rect.l<=C.x<=rect.r:
        return True

    elif rect.l==rect.r and rect.t==rect.b and C.x==rect.l and C.y==rect.t:
        return False
    
    else:
        return False

#1.1-1.9
A=Point(5,4)
B=Point(2,1)
C=Point(4,2)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

A=Point(5,4)
B=Point(2,1)
C=Point(6,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(1,0)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(1,2)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False
    
A=Point(5,4)
B=Point(2,1)
C=Point(3,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(6,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(3,0.5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(6,0)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,4)
B=Point(2,1)
C=Point(1,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#вертикальный отрезок(3)
A=Point(3,1)
B=Point(3,4)
C=Point(3,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

#вертикальный отрезок(4)
A=Point(3,4)
B=Point(3,1)
C=Point(3,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

#вертикальный отрезок(3)
A=Point(3,1)
B=Point(3,4)
C=Point(4,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#вертикальный отрезок(4)
A=Point(3,4)
B=Point(3,1)
C=Point(4,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#горизонтальный отрезок(5)
A=Point(3,4)
B=Point(1,4)
C=Point(2,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#горизонтальный отрезок(6)
A=Point(1,4)
B=Point(3,4)
C=Point(2,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#горизонтальный отрезок(5)
A=Point(3,4)
B=Point(1,4)
C=Point(2,4)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

#горизонтальный отрезок(6)
A=Point(1,4)
B=Point(3,4)
C=Point(2,4)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

#7.1-7.9
A=Point(2,1)
B=Point(5,4)
C=Point(4,2)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

A=Point(2,1)
B=Point(5,4)
C=Point(6,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(1,0)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(1,2)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(3,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(6,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(3,0.5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(6,0)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,1)
B=Point(5,4)
C=Point(1,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#8.1-8.9
A=Point(2,4)
B=Point(5,2)
C=Point(3,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

A=Point(2,4)
B=Point(5,2)
C=Point(1,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(3,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(6,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(6,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(6,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(3,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(1,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(2,4)
B=Point(5,2)
C=Point(1,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

#9.1-9.9
A=Point(5,2)
B=Point(2,4)
C=Point(1,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(1,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(3,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(6,5)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(6,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(1,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(6,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(3,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False

A=Point(5,2)
B=Point(2,4)
C=Point(3,3)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==True

A=Point(2,2)
B=Point(6,2)
C=Point(2,1)
rect=Rect(min(A.x,B.x),max(A.x,B.x),max(A.y,B.y),min(A.y,B.y))
assert point(rect,C)==False
