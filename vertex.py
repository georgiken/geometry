from dataclasses import dataclass

from LineABC import LineABC

from data_class import Point,Segment,Triangle,Line

def vertex(tr,Line):#определение вершины треугольника после пересечения с прямой
    a=Line.A
    b=Line.B
    c=Line.C
    x1=tr.AB.A.x
    y1=tr.AB.A.y
    x2=tr.AB.B.x
    y2=tr.AB.B.y
    x3=tr.AC.B.x
    y3=tr.AC.B.y

    if a*x1+b*y1+c>0 and a*x2+b*y2+c>0 and a*x3+b*y3+c<0:
        return Point(x3,y3)

    if a*x1+b*y1+c>0 and a*x2+b*y2+c<0 and a*x3+b*y3+c>0:
        return Point(x2,y2)

    if a*x1+b*y1+c<0 and a*x2+b*y2+c>0 and a*x3+b*y3+c>0:
        return Point(x1,y1)

    if a*x1+b*y1+c<0 and a*x2+b*y2+c>0 and a*x3+b*y3+c<0:
        return Point(x2,y2)

    if a*x1+b*y1+c>0 and a*x2+b*y2+c<0 and a*x3+b*y3+c<0:
        return Point(x1,y1)

    if a*x1+b*y1+c<0 and a*x2+b*y2+c<0 and a*x3+b*y3+c>0:
        return Point(x3,y3)

    else:
        return None
