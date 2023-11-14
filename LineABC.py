from dataclasses import dataclass

from data_class import Point,Line

def LineABC(p1,p2):#определение параметров abc
    #Ax+By+C=0
    A=p2.y-p1.y
    B=p1.x-p2.x
    C=-(A*p1.x+B*p1.y)
    return (Line(A,B,C))

'''A=Point(3,1)
B=Point(6,4)
print (LineABC(A,B))'''
