from dataclasses import dataclass

from LineABC import LineABC

from Heron import Heron

from cases_of_intersection import CI 

from data_class import Point,Segment,Line,Triangle

def biggest_heron(A,B,C,D):
    #A-вершина, D-точка перечесения стороны и отрезка
    if Heron(A,B,D)>Heron(A,C,D):
        return Heron(A,B,D)
    else:
        return Heron(A,C,D)
'''
A=Point(2,2)
D=Point(4,2)
C=Point(6,2)
B=Point(4,4)
assert biggest_heron(A,B,C,D)==2

A=Point(2,2)
D=Point(3,2)
C=Point(6,2)
B=Point(4,4)
assert biggest_heron(A,B,C,D)==3
'''
A=Point(4,2)
B=Point(4,5)
C=Point(7,2)
D=Point(5.5,3.5)
assert biggest_heron(A,B,C,D)==2.25
