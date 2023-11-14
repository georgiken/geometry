from dataclasses import dataclass

from LineABC import LineABC

from point_in_rect import point

from Intersection import intersection

from data_class import Point,Segment, Line, Triangle, Rect

def SIT(tr,p1,p2):#segment intersection triangle
    rectL=Rect(min(p1.x,p2.x),max(p1.x,p2.x),max(p1.y,p2.y),min(p1.y,p2.y))
    abcL=LineABC(p1,p2)
    
    rect1=Rect(min(tr.AB.A.x, tr.AB.B.x),max(tr.AB.A.x, tr.AB.B.x),max(tr.AB.A.y, tr.AB.B.y),min(tr.AB.A.y, tr.AB.B.y))
    abcS1=LineABC(tr.AB.A,tr.AB.B)
    C1=intersection(abcL,abcS1)
    
    rect2=Rect(min(tr.BC.A.x, tr.BC.B.x),max(tr.BC.A.x, tr.BC.B.x),max(tr.BC.A.y, tr.BC.B.y),min(tr.BC.A.y, tr.BC.B.y))
    abcS2=LineABC(tr.BC.A,tr.BC.B)
    C2=intersection(abcL,abcS2)

    rect3=Rect(min(tr.AC.A.x, tr.AC.B.x),max(tr.AC.A.x, tr.AC.B.x),max(tr.AC.A.y, tr.AC.B.y),min(tr.AC.A.y, tr.AC.B.y))
    abcS3=LineABC(tr.AC.A,tr.AC.B)
    C3=intersection(abcL,abcS3)

    #breakpoint()
    if C1!=None and C2!=None and C1!=C2:
        if point(rect1,C1)==True and point(rectL,C1)==True and point(rect2,C2)==True and point(rectL,C2)==True:
            return Segment(C1,C2)

    if C1!=None and C3!=None and C1!=C3:
        if point(rect1,C1)==True and point(rectL,C1)==True and point(rect3,C3)==True and point(rectL,C3)==True:
            return Segment(C1,C3)

    if C2!=None and C3!=None and C2!=C3:
        if point(rect2,C2)==True and point(rectL,C2)==True and point(rect3,C3)==True and point(rectL,C3)==True:
            return Segment(C3,C2)

    else:
        return None


A=Point(7,1)
B=Point(6,6)
C=Point(9,3)
D=Point(8,5)
E=Point(8,1)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)== Segment(Point(8,2),Point(8,4))

A=Point(4,3)
B=Point(6,6)
C=Point(9,3)
D=Point(6,2)
E=Point(9,5)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)== Segment(Point(7,3),Point(8,4))

A=Point(4,4)
B=Point(6,4)
C=Point(6,2)
D=Point(5,1)
E=Point(7,1)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)== None

A=Point(1,1)
B=Point(3,1)
C=Point(1,3)
D=Point(3,3)
E=Point(5,5)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)== None

A=Point(2,2)
B=Point(2,4)
C=Point(4,2)
D=Point(4,4)
E=Point(1,1)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)== Segment(Point(2,2),Point(3,3))

A=Point(4,2)
B=Point(4,5)
C=Point(7,2)
D=Point(3,1)
E=Point(6,4)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)==Segment(Point(4,2),Point(5.5,3.5))

A=Point(2,2)
B=Point(2,5)
C=Point(6,2)
D=Point(5,4)
E=Point(1,0)
AB=Segment(A,B)
BC=Segment(B,C)
AC=Segment(A,C)
tr=Triangle(AB,BC,AC)
assert SIT(tr,D,E)==Segment(Point(3,2),Point(4.286,3.286))
