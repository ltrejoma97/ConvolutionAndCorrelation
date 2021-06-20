#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt


# In[60]:



 
# Funcion para desarrollar la convolucion a partir de 2 listas
def convolucion(a, b):

    # Stores the size of arrays
    n, m = len(a), len(b)
 
    # Guarda la convolucion
    c = [0] * (n + m - 1)
 
    # Recorriendo los dos arreglos
    for i in range(n):
        for j in range(m):
             
            #Operacion de convolucion
            c[i + j] += (a[i] * b[j])
    #Retorna la convolucion
    return c

     


# In[88]:


A = [-7, -5, 3, 1]
B = [5, 2, 1, -2]
     
listConvolucion =  convolucion(A, B)


# In[61]:


#Crea el intervalo para graficar
x_list=[0,1,2,3,4,5,6]
x = np.array(x_list)


# In[62]:


#Convertir la lista a un array 
arrayConvolucion = np.array(listConvolucion)


# In[ ]:





# In[121]:




plt.plot(x, arrayConvolucion, 'bo', color = 'black')
plt.xlabel('t')
plt.ylabel('x*y')
plt.title('x*y vs t')
plt.show()
#primera convolucion


# In[86]:


#Para correlacionar
#Se convierten las listas en Arrays,
#los cuales son una estructura 
#de data definida adentro de la libreria numpy.
aArray=np.array(A)
bArray=np.array(B)

#Ademas se utilizo la funcion de correlate, la cual esta
#definida tambien en la libreria numpy.
#En los parametros tenemos las funciones a correlacionar 
#asi como el argumenteo 'full' el cual hace referencia al tipo de dato 
#Que tendra cada uno de los elementos del array de salida
correlation=np.correlate(aArray, bArray, "full")


# In[124]:


#Se importa la libreria matplotlib
import matplotlib.pyplot as plt

#Se geberan los graficos a partir de las salidas de los codigos anteriores
#Se le pasa a la funcion plot, un array x con valores cualesquiera para el tiempo
#Se le pasa el array correspondiente a la correlacion o a la convolucion
#generado con los codigos anteriores
plt.plot(x,correlation, 'bo', color = 'black')
plt.xlabel('t')
plt.ylabel('corr(x,y)')
plt.title('corr(x,y) vs t')
plt.show()


# In[ ]:


#Segundo ejercicio correlacion


# In[89]:


bModificada=[-2,1,2,5]


# In[96]:


segundaConvolucion=convolucion(A,bModificada)

#Conversion a array

arraySegundaConvolucion= np.array(segundaConvolucion)
arraySegundaConvolucion


# In[123]:


#Graficando la segunda convolucion

plt.plot(x,arraySegundaConvolucion, 'bo', color= 'black')
plt.xlabel('t')
plt.ylabel('x*ymodificada')
plt.title('x*ymodificada vs t')

plt.show()


# In[97]:


#D Autocorrelacion


# In[116]:


aArray=np.array(A)


autoCorrelation=np.correlate(aArray, aArray, "full")


# In[122]:


#Graficando autocorrelacion2

plt.plot(x,autoCorrelation,'bo', color ='red')
plt.xlabel('t')
plt.ylabel('corr(x,x)')
plt.title('corr(x,x) vs t')
plt.show()


# In[100]:


#E autocorrelacion


# In[102]:


bArray=np.array(B)
autoCorrelationB=np.correlate(bArray,bArray,'full')


# In[111]:


#Graficando autocorrelation

plt.plot(x,autoCorrelationB,'bo')
plt.xlabel('t')
plt.ylabel('corr(x,x)')
plt.title('corr(x,x) vs t')
plt.show()


# In[ ]:




