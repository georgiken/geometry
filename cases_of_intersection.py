from dataclasses import dataclass

from data_class import Point, Segment, Line, Triangle, Case

from data_class import Tvertex as Tv

from LineABC import LineABC

def CI(Line, A, B, C):
    a = Line.A
    b = Line.B
    c = Line.C
    tr = Triangle(Segment(A,B),Segment(B,C),Segment(A,C))

    if (a*A.x+b*A.y+c == 0 and a*B.x+b*B.y+c == 0) or (a*A.x+b*A.y+c == 0 and a*C.x+b*C.y+c == 0) or (a*B.x+b*B.y+c == 0 and a*C.x+b*C.y+c == 0):
        return Tv(False, None,Case(False,True))
        
    elif a*A.x+b*A.y+c==0 or a*B.x+b*B.y+c==0 or a*C.x+b*C.y+c==0:

        if a*A.x+b*A.y+c==0:
            return Tv(True,A,Case(False,False))

        if a*B.x+b*B.y+c==0:
            return Tv(True,B,Case(False,False))

        if a*C.x+b*C.y+c==0:
            return Tv(True,C,Case(False,False))

    elif (a*A.x+b*A.y+c>=0 and a*B.x+b*B.y+c>=0 and a*C.x+b*C.y+c>=0) or (a*A.x+b*A.y+c<=0 and a*B.x+b*B.y+c<=0 and a*C.x+b*C.y+c<=0):
        return Tv(False,None,Case(False,True))
    
    else:
        return Tv(False,None,Case(True,False))
    

# A=Point(4,2)
# B=Point(2,2)
# C=Point(2,4)
# D=Point(3,4)
# E=Point(3,1)
# Line=LineABC(D,E)
# assert CI(Line,A,B,C)==Tv(False,None,Case(NormalI=True,NoneI=False))
#
# A=Point(4,2)
# B=Point(2,2)
# C=Point(2,4)
# D=Point(4,4)
# E=Point(1,1)
# Line=LineABC(D,E)
# assert CI(Line,A,B,C)==Tv(True,Point(2,2),Case(NormalI=False,NoneI=False))
#
# A=Point(4,2)
# B=Point(2,2)
# C=Point(2,4)
# D=Point(5,2)
# E=Point(5,4)
# Line=LineABC(D,E)
# assert CI(Line,A,B,C)==Tv(False,None,Case(NormalI=False,NoneI=True))
#
# A=Point(4,2)
# B=Point(2,2)
# C=Point(2,4)
# D=Point(0,2)
# E=Point(0,4)
# Line=LineABC(D,E)
# assert CI(Line,A,B,C)==Tv(False,None,Case(NormalI=False,NoneI=True))
#
# A=Point(1,1)
# B=Point(3,1)
# C=Point(1,3)
# D=Point(1,3)
# E=Point(1,1)
# Line=LineABC(D,E)
# assert CI(Line,A,B,C)==Tv(False,None,Case(NormalI=False,NoneI=True))

