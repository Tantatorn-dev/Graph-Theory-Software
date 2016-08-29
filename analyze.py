from collections import Counter
import itertools
import simplejson
import Tkinter

f1 = open('output1.txt', 'r')
myVertex=simplejson.load(f1)
f1.close()

f2 = open('output2.txt', 'r')
myEdge=simplejson.load(f2)
f2.close()

f3 = open('output3.txt', 'r')
v=simplejson.load(f3)
f3.close()

myVertex= [tuple(l) for l in myVertex]
myEdge= [[tuple(i) for i in I] for I in myEdge ]

def delete_duplicates(k):
    k.sort()
    return list(k for k, _ in itertools.groupby(k))


class counter(object):

    def __init__(self,edge,vertex):
        self.edge=edge
        self.vertex=vertex

    def count_vertex(self):
        Vertex=self.vertex
        count_vertex=len(Vertex)
        return count_vertex

    def count_degree(self):
        edge_distribute=[]
        Edge=self.edge
        for m in Edge:
            for n in m:
               edge_distribute.append(n)
        count_degree=dict(Counter(edge_distribute[:]))
        return count_degree


result=counter(myEdge,myVertex)
vertex=result.count_vertex()
degree=result.count_degree()
edge=len(myEdge)


class check_properties(object):

    def __init__(self,edge,vertex,degree,myEdge,myVertex):
        self.edge=edge
        self.vertex=vertex
        self.degree=degree
        self.myEdge=myEdge
        self.myVertex=myVertex

    def check_noLoop(self):
        my_Edge=self.myEdge
        setA=[]
        for item in my_Edge:
            setA.append(set(item))
        if len(setA)!=len(delete_duplicates(setA)):
            return True

    def check_noMultipleedges(self):
        myEdge=self.myEdge
        if len(delete_duplicates(myEdge)) != len(myEdge):
            return True

    def check_simpleGraph(self):
        if check_properties.check_noLoop(self) or check_properties.check_noMultipleedges(self):
            return True



    def check_completeGraph(self):
        e=self.edge
        v=self.vertex
        number=(v*(v-1))/2
        if e==number:
            return True

    def check_regularGraph(self):
        deg=self.degree
        Deg=[]
        for key in deg:
            Deg.append(deg[key])
        Deg=list(set(Deg))
        if len(Deg)==1:
            return True

property=check_properties(edge,vertex,degree,myEdge,myVertex)

def Y_N(i):
    if i:
        return "Yes"
    else:
        return "No"

empty=[]
for key in degree:
    empty.append(degree[key])

root=Tkinter.Tk()

labelVertex=Tkinter.Label(root,text='Vertex')
labelDegree=Tkinter.Label(root,text='Degree')
labelSumDegree=Tkinter.Label(root,text='Sum.Degree')
labelSimpleGraph=Tkinter.Label(root,text='Simple Graph')
labelCompleteGraph=Tkinter.Label(root,text='Complete Graph')
labelRegularGraph=Tkinter.Label(root,text='Regular Graph')

ShowVertex=Tkinter.Label(root,text=v)
ShowDegree=Tkinter.Label(root,text=empty)
ShowSumDegree=Tkinter.Label(root,text=edge)
ShowSimpleGraph=Tkinter.Label(root,text=Y_N(property.check_simpleGraph()))
ShowCompleteGraph=Tkinter.Label(root,text=Y_N(property.check_completeGraph()))
ShowRegularGraph=Tkinter.Label(root,text=Y_N(property.check_regularGraph()))

labelVertex.grid(row=0,column=0)
labelDegree.grid(row=1,column=0)
labelSumDegree.grid(row=2,column=0)
labelSimpleGraph.grid(row=3,column=0)
labelCompleteGraph.grid(row=4,column=0)
labelRegularGraph.grid(row=5,column=0)

ShowVertex.grid(row=0,column=1)
ShowDegree.grid(row=1,column=1)
ShowSumDegree.grid(row=2,column=1)
ShowSimpleGraph.grid(row=3,column=1)
ShowCompleteGraph.grid(row=4,column=1)
ShowRegularGraph.grid(row=5,column=1)

root.mainloop()
