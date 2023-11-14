mx=800
my=600
m=50
#размер рабочей области и масштаб

from tkinter import *

from tkinter import messagebox

from dataclasses import dataclass

from data_class import Point,Result

from endfunc import endfunc

messagebox.showinfo('info','Условие:На плоскости задан треугольник (тремя точками) и множество точек. Найти такие две точки множества, что отрезок между ними отсекает у треугольника треугольник наибольшей площади.В качестве ответа вывести площадь найденного треугольника и выделить этот треугольник, найденные две точки и две точки пересечения отрезка со сторонами исходного треугольника.Первые 3 введённые точки-вершины треугольника, все последующие-точки плоскости. Координаты по х от -8 до 8, по y от -6 до 6(только целые числа)')
vvod=Tk()
vvod.title("ввод точек")

x=StringVar()
y=StringVar()

x_label=Label(vvod, text="Введите значение точки х:")
y_label=Label(vvod, text="Введите значение точки у:")

x_label.grid(row=0, column=0)
y_label.grid(row=1, column=0)

x_entry=Entry(vvod, width=10)
y_entry=Entry(vvod, width=10)

x_entry.grid(row=0,column=1, padx=5, pady=5)
y_entry.grid(row=1,column=1, padx=5, pady=5)

Vertex=[]#for solving
Vertexr=[]#for rendering
Listp=[]#for solving
Listpr=[]#for rendering

def input():
    if len(Vertex)<=2:
        Vertex.append(Point(float(x_entry.get()),-float(y_entry.get())))
        Vertexr.append(Point(float(x_entry.get())*m+mx//2,-float(y_entry.get())*m+my//2))
    else:
        Listp.append(Point(float(x_entry.get()),-float(y_entry.get())))
        Listpr.append(Point(float(x_entry.get())*m+mx//2,-float(y_entry.get())*m+my//2))

    x_entry.delete(0, END)
    y_entry.delete(0, END)
    




def rendering_axes(x,y,m,canv):
    canv.create_line(x//2,y,x//2,0,arrow=LAST)
    canv.create_line(0,y//2,x,y//2, arrow=LAST)

    for i in range(0,max(x,y),m):
        canv.create_line(i,(y//2)-5, i,(y//2)+5)
        canv.create_line((x//2)-5,i, (x//2)+5,i)
        if i//50<=8 and i!=0:
            canv.create_text(i+x//2,y//2+15,text = str(round(i//m,1)),font =("Verdana 9", 8), fill = 'black')                        
        elif 8<i//50<=16:
            canv.create_text(-(x//2-i),y//2+15,text = str(round(-(x-i)//m,1)),font =("Verdana 9", 8), fill = 'black')
        if i//60<=12 and i!=0:
            canv.create_text(x//2-12,i+y//2,text = str(round(-i//m,1)),font =("Verdana 9", 8), fill = 'black') 
            canv.create_text(x//2-12,i,text = str(round((300-i)//m,1)),font =("Verdana 9", 8), fill = 'black')
        canv.create_text(x//2-10,y//2+10,text = str(0),font =("Verdana 9", 8), fill = 'black')
        

def rendering_triangle(vertex,canv):
    canv.create_polygon(vertex[0].x,vertex[0].y,vertex[1].x ,vertex[1].y, vertex[2].x, vertex[2].y, fill="green")
    canv.create_oval(vertex[0].x,vertex[0].y,vertex[0].x,vertex[0].y, width=3)
    canv.create_oval(vertex[1].x,vertex[1].y,vertex[1].x,vertex[1].y, width=3)
    canv.create_oval(vertex[2].x,vertex[2].y,vertex[2].x,vertex[2].y, width=3)


def rendering_points(t,canv):
    for i in range(len(t)):
        canv.create_oval(t[i].x,t[i].y,t[i].x,t[i].y, width=3)

def highlighting_result(Result,canv,mx,my):
    canv.create_oval(Result.A.x,Result.A.y,Result.A.x,Result.A.y, width=5)
    canv.create_oval(Result.B.x,Result.B.y,Result.B.x,Result.B.y, width=5)
    canv.create_oval(Result.C.x,Result.C.y,Result.C.x,Result.C.y, width=5)
    canv.create_oval(Result.D.x,Result.D.y,Result.D.x,Result.D.y, width=5)
    canv.create_oval(Result.Vertex.x,Result.Vertex.y,Result.Vertex.x,Result.Vertex.y, width=5)

    canv.create_polygon(Result.Vertex.x,Result.Vertex.y,Result.C.x,Result.C.y,Result.D.x,Result.D.y, fill="yellow")

    #canv.create_text(x//2,y,text="S="+Result.S,font =("Verdana 9", 8), fill = 'black')
    canv.create_line(Result.B.x,Result.B.y,Result.A.x,Result.A.y)


def converting_result_for_rendering(result,m,mx,my):
    Ax=result.A.x*m+mx//2
    Ay=result.A.y*m+my//2

    Bx=result.B.x*m+mx//2
    By=result.B.y*m+my//2

    Cx=result.C.x*m+mx//2
    Cy=result.C.y*m+my//2

    Dx=result.D.x*m+mx//2
    Dy=result.D.y*m+my//2

    Px=result.Vertex.x*m+mx//2
    Py=result.Vertex.y*m+my//2


    return Result(result.S,Point(Ax,Ay),Point(Bx,By),Point(Cx,Cy),Point(Dx,Dy),Point(Px,Py))

def converting_result(result):
    Ay=-result.A.y

    By=-result.B.y

    Cy=-result.C.y

    Dy=-result.D.y

    Py=-result.Vertex.y

    return Result(result.S,Point(result.A.x,Ay),Point(result.B.x,By),Point(result.C.x,Cy),Point(result.D.x,Dy),Point(result.Vertex.x,Py))

def rendering():
    #Points=input()
    #breakpoint()
    geoma=Tk()
    geoma.title('рабочее пространство')
    canv=Canvas(geoma, width=mx, height=my)
    RESULT=endfunc(Vertex,Listp)    
    canv.pack()
    RESULTR=converting_result_for_rendering(RESULT,m,mx,my)
    rendering_axes(mx,my,m,canv)
    rendering_triangle(Vertexr,canv)
    rendering_points(Listpr,canv)
    highlighting_result(RESULTR,canv,mx,my)
    Final_Result=converting_result(RESULT)
    print(Final_Result)



input_button=Button(vvod, text='Ввод', command=input)
input_button.grid(row=3,column=0)
exit_button=Button(vvod, text='закончить ввод', command=rendering)
exit_button.grid(row=3,column=1)
vvod.mainloop()
