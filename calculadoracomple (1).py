'LIBRERÍA COMPUTACIONAL:Calculadora números complejos'
'Permite operar números complejos de la forma a+bi'

'------------------------Operaciones Básicas--------------------------'
import numpy as np
from numpy import linalg as LA
import math
import sys

#Suma(Permite sumar números complejos)
def suma(a,b):
    c=a[0]+b[0]
    d=a[1]+b[1]
    return impri(c,d)

#Resta(Permite restar números complejos)
def res(a,b):
    c=a[0]-b[0]
    d=a[1]-b[1]
    return impri(c,d)

#Multiplicar(Permite multiplicar números complejos)
def multi(a,b):
    c=a[0]*b[0]-a[1]*b[1]
    d=a[0]*b[1]+a[1]*b[0]
    return impri(c,d)

#División(Permite dividir números complejos) 
def div(a,b):
    c=conju(b)
    e=multi(a,c)
    f=multi(b,c)
    x=f[0]+f[1]
    if x==0:
        print('No se puede dividir por 0')
    else:
        g=e[0]/x
        h=e[1]/x
        return impri(g,h)

#Conjugado(Permite hallar el conjugado de un número complejo)    
def conju(a):
    b=a[1]*-1
    return impri(a[0],b)

#Módulo(Permite hallar el módulo de un número complejo)
def modu(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    return b

#Conversión de representación polar a cartesiana.(Permite la conversión polar a cartesiana de un número complejo)
def pol_carte(a):
    b=a[0]*math.cos(a[1])
    c=a[0]*math.sin(a[1])
    return impri(b,c)

#Conversión de representación cartesiana a polar.(Permite la conversión cartesiana a polar de un número complejo)
def carte_pol(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    c=math.atan2(a[1],a[0])
    return impri(b,c)

#Fase(Permite hallar la fase de un número complejo)
#La fase se halla teniendo en cuenta el cuadrante en donde se encuentran las coordenadas
def fase(num):
    f1=math.atan(num[1]/num[0])
    if num[0]<0 and num[1]<0:
        return(180+math.degrees(f1))
    elif num[0]<0:
        return (180+math.degrees(f1))
    elif num[1]<0:
        return(360+ math.degrees(f1))
    else:
        return(math.degrees(f1))
    
'---------------------Impresión números complejos-------------------------'

#Imprimir(Permite mostrar el resultado de un número complejo concatenado en una lista)
def impri(a,b):
    z=[]
    z.append(a)
    z.append(b)
    return z
'-------------------------------Vectores----------------------------------'

#Adición de vectores.(Permite sumar vectores complejos)
def adicionvectores(a,b):
    for i in range(len(a)):
        a[i]=suma(a[i],b[i])
    return a

#Inverso de un vector complejo.(Permite hallar el inverso aditivo de un vector complejo)
def inversovector(a):
    for i in range(len(a)):
        for j in range(2):
            a[i][j]=a[i][j]*-1
    return a

#Multiplicación escalar de vectores.(Permite multiplicar un escalar por un vector complejo)
def multiescalarvector(a,b):
    for i in range(len(b)):
        b[i]=multi(a,b[i])
    return b

#Multiplicación de vectores.(Permite multiplicar un vectores complejos)
def multivector(a,b):
    l=[]
    for i in range(len(a)):
        l.append(multi(a[i],b[i]))
    while len(l)>1:
        l[0]=suma(l[0],l[-1])
        l.pop()
    return l[0]

#Producto interno.(Permite hallar el producto interno entre vectores complejos)
def productointerno(a,b):
    l=[]
    for i in range(len(a)):
        l.append([])
        a[i]=conju(a[i])
    for i in range(len(a)):
        c=multi(a[i],b[i])
        l[i]=c
    while len(l)>1:
        l[0]=suma(l[0],l[-1])
        l.pop()
    return l[0]

#Norma de vector.(Permite hallar la norma de un vector complejo)
def normavector(v1):
    suma=0
    for i in range(len(v1)):
        suma+=(v1[i][0]**2)+(v1[i][1]**2)
    norma=math.sqrt(suma)
    return (norma)

#Distancia entre vectores.(Permite hallar la distancia entre vectores complejos)
def distanciaVector(a,b):
    c=0
    d=0
    if len(a)!= len(b):
        raise ValueError('los vectores deben tener el mismo tamaño')
    else:
        for i in range(len(a)):
            c+=(a[i][0]-b[i][0])**2
            d+=(a[i][1]-b[i][1])**2
        dis=math.sqrt(c+d)
    return (dis)

#Resta de vectores.(Permite restar vectores complejos)
def restavectores(a,b):
    l=[]
    for i in range(len(a)):
        l.append([])
    for i in range(len(a)):
        l[i]=res(a[i],b[i])
    return l

'---------------------------------Matrices---------------------------------'

#Adición de matrices.(Permite sumar matrices complejas)
def adicionmatriz(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=suma(a[i][j],b[i][j])
    return a

#Resta de matrices.(Permite restar matrices complejas)
def restarmatriz(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=res(a[i][j],b[i][j])
    return a

#Inverso de matrices.(Permite hallar el inverso aditivo de una matriz compleja)
def inversomatriz(a):
    for i in range(len(a)):
        a[i]=inversovector(a[i])
    return a

#Multiplicación escalar de matrices.(Permite multiplicar un escalar por una matriz compleja)
def multiescalarmatriz(a,b):
    x=[]
    for i in range(len(b)):
        l=[]
        x.append(l)
        for j in range(len(b[0])):
            l.append([])
    for i in range(len(b)):
        for j in range(len(b[i])):
            x[i][j]=multi(a,b[i][j])
    return x

#Matriz transpuesta.(Permite hallar la transpuesta de una matriz compleja)
def matriztranspuesta(a):
    x=[]
    for i in range(len(a[0])):
        l=[]
        x.append(l)
        for j in range(len(a)):
            l.append([])
    for k in range(len(a)):
        for m in range(len(a[k])):
            x[m][k]=a[k][m]
    return x

#Matriz conjugada.(Permite hallar la conjugada de una matriz compleja)
def matrizconjugada(a):
    x=[]
    for i in range(len(a)):
        l=[]
        x.append(l)
        for j in range(len(a[i])):
            l.append([])
    for i in range(len(a)):
        for j in range(len(a[0])):
            x[i][j]=conju(a[i][j])
    return x

#Matriz adjunta.(Permite hallar la adjunta o daga de una matriz compleja)
def matrizadjunta(a):
    b=matrizconjugada(a)
    c=matriztranspuesta(b)
    return c

#Multiplicación de matrices.(Permite multiplicar dos matrices complejas)
def multimatriz(a,b):
    z='Error. Las matrices no tienen dimensiones compatibles'
    if len(a[0])!=len(b):
        return z
    else:
        
        x=[]
        for i in range(len(a)):
            l=[]
            x.append(l)
            for j in range(len(b[0])):
                l.append([])
                
        c=matriztranspuesta(b)
        for k in range(len(a)):
            for m in range(len(c)):
                x[k][m]=multivector(a[k],c[m])
        return x
            
#¿Matriz unitaria?(Permite revisar si la matriz compleja ingresada es unitaria)
def matrizunitaria(a):
    e=unitaria(len(a),len(a[0]))
    b=multimatriz(a,matrizadjunta(a))
    for i in range(len(b)):
        for j in range(len(b[i])):
            c=redondeo(b[i][j])
            b[i][j]=c        
    f='Es unitaria'
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j]!= e[i][j]:
                f='No es unitaria'
                break
    return f

#Matriz unitaria(Permite crear una matriz unitaria con las dimensiones de la matriz ingresada)
def unitaria(b,c):
    x=[]
    for i in range(b):
        l=[]
        x.append(l)
        for j in range(c):
            l.append([])
    for i in range(b):
        for j in range(c):
            if i==j:
                x[i][j]=[1,0]
            else:
                x[i][j]=[0,0]
    return x

#¿Matriz hermitiana?(Permite revisar si la matriz conpleja ingresada es hermitiana)
def matrizhermitaña(a):
    b=matrizadjunta(a)
    c='Es hermitaña'
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]!= b[i][j]:
                c='No es hermitaña'
                break
    return c

#Producto tensor.(Permite realizar el producto tensor de matrices complejas)
def productotensor(a,b):
    x=[]
    c=len(a)*len(b)
    d=len(a[0])*len(b[0])
    for i in range(c):
        l=[]
        x.append(l)
        for j in range(d):
            l.append([])
    for i in range(c):
        for j in range(d):
            e=i//len(b)
            f=j//len(b[0])
            g=multiescalarmatriz(a[e][f],b)
            m=i%len(b)
            n=j%len(b[0])
            x[i][j]=g[m][n]
    return x
#return x,len(x),len(x[0]
'-------------------------------Redondeo------------------------------------'

#Redondeo(Permite Redondear números complejos)
def redondeo(a):
    l=[]
    b=round(a[0])
    c=round(a[1])
    l.append(b)
    l.append(c)
    return l


'-------------------------------sistema cuantico-----------------------------------'

def ensamble(M,V,M2,V2,t):
    # Vector de estado inicial
    VE = productotensor(V, V2)

    #Matriz estado inicial
    ME = productotensor(M, M2)


    # Ciclo para el cálculo de las acciones
    for i in range(t):
        VE = multimatriz(ME, VE)
    print('Vector estado final')
    print(VE)
    print(' ')
    print('Sistema')
    for i in range(len(VE)):
        a= '*'*round((VE[i][0][0]*100))
        print(i,a)

#sistema doble rendija cuantico y probabilistico

def rendija(nren,nblan,vector):
    
    paredes=nren+1
    matrizlen=(nblan*paredes)+(2*nren)+1
    matriz=[]
    #se crea la matriz adyacente y se llena de ceros
    
    for i in range(matrizlen):
        l=[]
        for j in range(matrizlen):
            l.append([0,0])
        matriz.append(l)
        
    #Llena las probabilidades de las rendijas
        
    for i in range(nren+1):
        for j in range(nren+1):
            if i==0:
                matriz[i][j]=[0,0]
            else:
                matriz[i][0]=[1/(nren)**(1/2),0]
                
    #Llena las diagonales de 1
                    
    for i in range(nren+1,matrizlen):
        for j in range(nren+1,matrizlen):
            if i==j:
                matriz[i][j]=[1,0]

    #Llena las probabilidades de los blancos
                
    n=1
    ini=nren+1
    while n<nren+1:
        m=0
        for i in range(ini,len(vector)+ini):
            matriz[i][n]=vector[m][0]
            m+=1
        n+=1
        ini=ini+nblan+1
    #multiplica las matrices    
    c=multimatriz(matriz,matriz)
    #se crea el vector inicial
    v=[]
    for i in range(matrizlen):
        if i==0:
            v.append([[1,0]])
        else:
            v.append([[0,0]])
    #multiplica el vector inicial por la matriz despues de dos clicks
    x=multimatriz(c,v)
            
    print("Matriz:")
    print(" ")
    print(matriz)
    print(" ")
    print('Matriz dos clicks:')
    print(" ")
    print(c)
    print(" ")
    print('vector final:')
    print(" ")
    print(x)

    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j]=multi(x[i][j],conju(x[i][j]))
            
    print('Vector estado final probabilistico')
    print(x)
    print(' ')
    print('Sistema')
    for i in range(len(x)):
        a= '*'*round(x[i][0][0]*100)
        print(i,a)
    
##Determinista

def determinista(m,v,t):
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = multimatriz(m, v)
    print('Vector estado final')
    print(v)
    print(' ')
    print('Sistema')
    for i in range(len(v)):
        a= '*'*(v[i][0][0])
        print(i,a)

##Probabilistico

def probabilistico(m,v,t):
    
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = multimatriz(m, v)
    print('Vector estado final')
    print(v)
    print(' ')
    print('Sistema')
    for i in range(len(v)):
        a= '*' * round((v[i][0][0]*10))
        print(i,a)

##Cuántico

def cuantico(m,v,t):
    for t in range(t):
        v = multimatriz(m, v)
    print('Vector estado final cuantico')
    print(v)
    print(' ')
    print('Sistema')
    for i in range(len(v)):
        a= '*' * round((v[i][0][0]*10))
        print(i,a)
    
    # Ciclo para el cálculo de las acciones
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = multi(m[i][j],conju(m[i][j]))
    for i in range(len(v)):
        for j in range(len(v[0])):
            v[i][j] = multi(v[i][j],conju(v[i][j]))

    print(" ")
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = multimatriz(m, v)
    print('Vector estado final probabilistico')
    print(v)
    print(' ')
    print('Sistema')
    for i in range(len(v)):
        a= '*' * round((v[i][0][0]*10))
        
        print(i,a)

##Sistema y sus dinamicas

def sistemadinamica(dinamica,matriz,vector,click):
    if dinamica == 0:
        a=False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (matriz[i][j][1]!=0 and (matriz[i][j][0]!=1 or (matriz[i][j][0]!=0))):
                    a=True
        if a==False:            
            determinista(matriz,vector,click)
        else:
            print('No es clásica')
            
        
    elif dinamica == 1:
        a=False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j][1]!=0 and matriz[i][j][0]==1 or matriz[i][j][0]==0:
                    a=True 
        if a==False:            
            probabilistico(matriz,vector,click)
        else:
            print('No es probabilistica')

    elif dinamica == 2:
        a=False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (matriz[i][j][0]!=0 or matriz[i][j][0]!=1) and (matriz[i][j][1]!=0 or matriz[i][j][1]!=1):
                    a=True
        if a==True:            
            cuantico(matriz,vector,click)
        else:
            print('No es cuantico')

'--------------------------Probabilidad del sistema de estar en una posición--------------'


#Probabilidad de posición.(Permite hallar la probabilidad del sistema en esa posición)
def probabipos(a,z):
    b=normavector(a)
    e=modu(a[z])**2/(b)**2
    return e

def probabilidadPosiciones(vk,n):
    l=[]
    z=[]
    for i in range(len(vk)):
        l.append(vk[i][0])
        z.append(vk[i][0])
    for i in range(len(l)):
        z[i]=probabipos(l,i)   
    for j in range(n):
        grafico= '*' * round(z[j]*100)
        print(j,grafico)
    return z
     
#Nomalizar vector.(Permite normalizar un vector ket)
def normaket(a):
    z=[]
    b=normavector(a)
    for i in range(len(a)):
        z.append([])
        z[i]=diviket(a[i],b)
    return z

#Divsion para normalizar.(Permite retornar un numero complejo dividido por la norma del vector)
def diviket(a,b):
    l=[]
    c=a[0]/b
    d=a[1]/b
    l.append(c)
    l.append(d)
    return l

#Amplitud(retorna un vector)
def amplitudtransicion(a,b):
    c=normaket(a)
    d=normaket(b)
    e=productointerno(c,d)
    print('La amplitud de transición del ket es:')
    return e

'punto 2'


def varianza_valor(m1,vk):
    l=[]
    for i in range(len(vk)):
        l.append(vk[i][0])
    a=normaket(l)
    ver=matrizhermitaña(m1)
    if (ver=='Es hermitaña'):
        for i in range(len(vk)):
            vk[i][0]=a[i]
        print('Valor esperado:')
        print(vEsperado(m1,vk))
        print('Varianza')
        print(varianza(m1,vk))

#m1=[[[2,0],[1,1]],[[1,-1],[3,0]]]'''
#vk=[[[1/math.sqrt(2),0]],[[0,1/math.sqrt(2)]]]'''
def vEsperado(m1,vk):
    a=multimatriz(m1,vk)
    newA=[]
    for i in range(len(a)):
        newA.append(a[i][0])

    newV=[]
    for i in range(len(vk)):
        newV.append(vk[i][0])
    return (productointerno(newA,newV))


def varianza(m1,vk):
    valor= vEsperado(m1,vk)
    result=multiescalarmatriz(valor,unitaria(len(m1),len(m1[0])))
    resta= restarmatriz(m1,result)
    mcuadrada= multimatriz(resta,resta)

    return(vEsperado(mcuadrada,vk))

#observable = [[0,0,0,0,0],[0,1,0,0,0],[0,0,2,0,0],[0,0,0,3,0],[0,0,0,0,4]]
#[[0.+0.j,0.+-1j/2,0.+-1j,-7/2+0.j],[0.+1j/2,0.+0.j,0.+7j/2,0.+-1j],[0.+1j,7/2+0.j,0.+0.j,0.+-1j/2],[-7/2+0.j,0.+1j,0.+1j/2,0.+0.j]]

def valoresPropios(observable):
    A = np.array(observable)
    w, v = LA.eig(A)
    print('Vectores propios')
    for x in v:
      print(x)    
    print('Valores propios')
    print(w)
