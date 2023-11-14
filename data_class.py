from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Segment:
    A: Point
    B: Point

@dataclass
class Line:
    A: float
    B: float
    C: float

@dataclass
class Triangle:
    AB: Segment
    BC: Segment
    AC: Segment

@dataclass
class Rect:
    l: float
    r: float
    t: float
    b: float

@dataclass
class Case:
    NormalI: bool #normal intersection
    NoneI: bool #none intersection

@dataclass
class Tvertex:
    TVertex: bool
    Point: Point
    Case: Case

@dataclass
class Result:
    S: float
    A: float
    B: float
    C: float
    D: float
    Vertex: float

