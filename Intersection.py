from dataclasses import dataclass

from LineABC import LineABC

from data_class import Point,Line


def intersection(Line1,Line2):
    a1=Line1.A
    b1=Line1.B
    c1=Line1.C
    a2=Line2.A
    b2=Line2.B
    c2=Line2.C
    if (b1!=0) and (b1*a2-b2*a1!=0) and c1!=c2:
        x=round(((b2*c1-b1*c2)/(a2*b1-a1*b2)),3)
        y=round(((-a1*x-c1)/b1),3)
        return Point(x,y)
    elif (b1==0 and b2!=0) and (b1*a2-b2*a1!=0) and not(a1==a2 and b1==b2 and c1==c2):
        x=round(((c2*b1-c1*b2)/(b2*a1-b1*a2)),3)
        y=round(((-a2*x-c2)/b2),3)
        return Point(x,y)

A=Point(3,1)
B=Point(6,4)
C=Point(4,5)
D=Point(7,2)
Line1=LineABC(A,B)
Line2=LineABC(C,D)
assert intersection(Line1,Line2)==Point(5.5,3.5)

A=Point(5,4)
B=Point(1,0)
C=Point(6,2)
D=Point(2,5)
Line1=LineABC(A,B)
Line2=LineABC(C,D)
assert intersection(Line1,Line2)==Point(4.286,3.286)
