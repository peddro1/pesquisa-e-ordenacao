echo "# pesquisa-e-ordenacao" >> README.md 


import time
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
mpl.use('Agg')
  
def desenhaGrafico(x,y2,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y2, label = "número de operações")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
   
def desenhaGrafico2(x,y,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph2.png')
   



def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)        
    return lista
  
x2 = [10000,20000,50000,100000]
y = []
y2= []
  
def sort(array):
    r=0
    inicio = timeit.default_timer()
    for final in range(len(array), 0, -1):
        
        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current], array[current + 1] = array[current + 1], array[current]
                r=r+1
    fim = timeit.default_timer()
    y.append('%f' %(fim - inicio))
    y2.append(r)
    

for i in range(4):
    array = geraLista(x2[i])
  

    sort(array)
    print(y)
    print(y2)


desenhaGrafico(x2,y2)

desenhaGrafico2(x2,y)






