from dataclasses import dataclass

from data_class import Point,Line,Segment,Triangle,Tvertex,Case,Result

from mainfunc import mainfunc

def endfunc(Vertex,List):
    #breakpoint()
    A=Vertex[0]
    B=Vertex[1]
    C=Vertex[2]
    results=[]
    List1=List[1:]
    for i in List:
        for j in List1:
            if i!=j and i!=None and j!=None:
                results.append(mainfunc(A,B,C,i,j))

    BS=0
    for i in range(len(results)):
        if results[i]!=None:
            BS=results[i].S
        break
    
    count=0
    for i in range(len(results)):
        if results[i]!=None:
            if BS<results[i].S:
                BS=results[i].S
                count=i
    return results[count]
'''
Vertex=[Point(2,2),Point(2,5),Point(6,2)]
List=[Point(5,4),Point(5,1), Point(1,1), Point(1,0),Point(4,5)]
assert endfunc(Vertex,List)==Result(3.733, Point(1, 0), Point(4, 5), Point(3.379, 3.965), Point(2.2, 2))

Vertex=[Point(4,2),Point(4,5),Point(7,2)]
List=[Point(5,5),Point(5,1), Point(1,1), Point(1,0),Point(4,5)]
print( endfunc(Vertex,List))


Vertex=[Point(4,2),Point(4,5),Point(7,2)]
List=[Point(1,5),Point(5,1), Point(1,1), Point(1,0),Point(4,5)]
print(endfunc(Vertex,List))
'''
