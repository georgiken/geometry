from dataclasses import dataclass

from data_class import Point,Segment,Line,Triangle,Case,Result,Tvertex

from LineABC import LineABC

from SIT import SIT

from cases_of_intersection import CI

from determines_of_triangle import biggest_heron

from vertex import vertex

from Heron import Heron

def mainfunc(A,B,C,p1,p2):
    
    Side1=Segment(A,B)
    Side2=Segment(A,C)
    Side3=Segment(B,C)
    tr=Triangle(Side1,Side2,Side3)
    Line=LineABC(p1,p2)
    Tv=CI(Line,A,B,C)
    
    if Tv.Case.NoneI==True:
        return None
    
    if Tv.TVertex==True:
        AD=SIT(tr,p1,p2)
        if AD!=None:
            A=AD.A
            B=B
            C=C
            D=AD.B
            S=biggest_heron(A,B,C,D)
            return Result(S,p1,p2,A,D,Tv.Point)
        else:
            return None

    if Tv.Case.NormalI==True:
        SegmentA=Segment(p1,p2)
        SegmentB=SIT(tr,p1,p2)
        A=vertex(tr,Line)
        if SegmentB!=None:
            B=SegmentB.A
            C=SegmentB.B
            S=Heron(A,B,C)
            return Result(S,p1,p2,B,C,A)
        else:
            return None
        
'''
A=Point(2,2)
B=Point(2,5)
C=Point(6,2)
D=Point(5,4)
E=Point(5,1)
assert mainfunc(A,B,C,D,E)==Result(0.375, Point(5,4),Point(5,1),Point(5,2.75),Point(5,2))

A=Point(4,2)
B=Point(4,5)
C=Point(7,2)
D=Point(5,1)
E=Point(5,5)
assert mainfunc(A,B,C,D,E)==Result(2, Point(5,1),Point(5,5),Point(5,4),Point(5,2))



A=Point(4,2)
B=Point(4,5)
C=Point(7,2)
D=Point(1,1)
E=Point(1,5)
assert mainfunc(A,B,C,D,E)==None

A=Point(4,2)
B=Point(4,5)
C=Point(7,2)
D=Point(3,1)
E=Point(6,4)
assert mainfunc(A,B,C,D,E)==Result(2.25, Point(3,1),Point(6,4),Point(4,2),Point(5.5,3.5))

A=Point(2,2)
B=Point(6,2)
C=Point(2,5)
D=Point(5,4)
E=Point(1,0)
assert mainfunc(A,B,C,D,E)==Result(1.929, Point(5,4),Point(1,0),Point(3,2),Point(4.286,3.286))
'''
