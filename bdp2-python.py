
# coding: utf-8

# In[17]:


# Valores numericos
2+3


# In[18]:


3/2


# In[20]:


3 + 5j


# In[21]:


#S Strings
"hola"


# In[23]:


'El dijo: "Ser o no ser"'


# In[25]:


"hola" + " " + "amigo"


# In[28]:


# Asignación
a = 19
b,c = 2,3
b+c


# In[ ]:


# Listas


# In[15]:


# Valores booleanos
True and False


# In[14]:


not True


# In[13]:


False or True


# In[38]:


#Listas y tuplas
"""Las tuplas y las listas ambas son conjuntos ordenados de elementos: 
las tuplas se demarcan con paréntesis y las listas con corchetes. 
"""
una_lista = [1, 2, 3.0, 4 + 0j, "5"]
una_tupla = (1, 2, 3.0, 4 + 0j, "5")
print(una_lista)
print(una_tupla)
print(una_lista == una_tupla)


# In[39]:


tupla_sin_parentesis = 2,5,6,9,7
type(tupla_sin_parentesis)


# In[ ]:


# Listas son mutables
una_lista[1] = 333


# In[ ]:


# Tuplas son inmutables
una_tupla[1] = 333


# In[35]:


# Sets
mi_set = {1,2,3}


# In[36]:


set_2 = {4,5}


# In[37]:


mi_set.union(set_2)


# In[29]:


# dict
released = {"iphone" : 2007, "iphone 3G" : 2008, "iphone 3GS" : 2009, "iphone 4" : 2010, "iphone 4S" : 2011, "iphone 5" : 2012}


# In[30]:


released["iphone"]


# ## Practice

# In[1]:


# TODO
def xor(b1, b2):
    if b1 == b2:
        return False
    else:
        return True


# In[2]:


xor(True, True)


# In[45]:


# TODO
def fibonnaci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        fib_n_1 = fibonnaci(n-1)
        return fib_n_1 + fibonnaci(n-2)


# In[56]:


fibonnaci(6)


# In[53]:


# TODO iterativo
def fibonnaci_iter(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    fib_n2 = 0
    fib_n1 = 1
    fib_n = 0
    for index in range(n-1):
        fib_n = fib_n1 + fib_n2
        print(fib_n)
        fib_n2 = fib_n1
        fib_n1 = fib_n
    return fib_n


# In[55]:


fibonnaci_iter(6)


# ### Módulos
# * NumPy (fundamental para el cálculo científico en Python; eficientes arrays multidimensionales...)
# * Matplotlib (fácil visualización en 2D)
# * Pandas (basado en NumPy, flexibles estructuras de datos: Dataframe; carga y visualización de datos)
# * SciPy (basado en NumPy, software para matemática/ciencia/ingeniería: integración numérica, optimización)
# * Sklearn (Scikit-Learn. Basado en NumPy, SciPy y Matplotlib; simple y eficientes métodos para ML/Data-Mining)
# * ...
# 
# ### Trabajo con NumPy
# 
# Los arrays Numpy son una alternativa a las listas de Python 
# 
# Algunas de las ventajas de los arrays NumPy:
# * eficiencia
# * facilidad de uso 
# * permite cálculos a través de todo el array
# 

# In[57]:


# Creación de Arrays NumPy
import numpy as np
values = [2,3,4,1,8,2]
np_values = np.array(values)


# In[58]:


# Operaciones sobre los elementos
print(np_values**2/4)
print(np.exp(np_values))
print(np.log10(np_values))


# In[59]:


# Subsetting
print(np_values > 3)
print(np_values[np_values>3])


# In[60]:


# Creación de Dataframes
import pandas as pd
data = {'año': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'equipo': ['BCN', 'BCN', 'BCN', 'ATM', 'ATM', 'RMA', 'RMA', 'RMA'],
        'ganados': [11, 8, 10, 15, 11, 6, 10, 4],
        'perdidos': [5, 8, 6, 1, 5, 10, 6, 12]}
futbol = pd.DataFrame(data, columns=['año', 'equipo', 'ganados', 'perdidos'])
print(futbol)


# In[61]:


type(futbol)
#dir(futbol)
#help(futbol)


# In[62]:


# Inspeccion del Dataframe
futbol.info()


# In[63]:


# Estadisticas descriptivas
futbol.describe()


# In[64]:


# Primeros tres Registros
futbol.head(3)


# In[65]:


# Ultimos dos Registros
futbol.tail(2)


# In[66]:


# Subconjunto de Registros
futbol[1:3]


# In[67]:


# Subconjunto de filas y columnas
futbol[['ganados', 'perdidos']][2:4]


# In[68]:


# Filtros
futbol[futbol.ganados<10]


# In[69]:


# Creacion de nuevo Dataframe
data2 = {'año': [2011, 2012, 2013, 2014],
        'nro_equipos': [19, 20, 21, 22]}
df2  = pd.DataFrame(data2, columns=['año', 'nro_equipos'])
df2


# In[70]:


# Mezcla (inner join)
pd.merge(futbol, df2)


# In[80]:


# Joins: left, right, outer, inner
pd.merge(futbol, df2, on='año', how='outer')


# In[72]:


# Transposición del Dataframe
futbol.T


# In[73]:


# Producto de Matrices
df3 = futbol[["ganados", "perdidos"]]
print(df3)
df3.T.dot(df3)


# In[75]:


# Reading and Writing Data Files
data = pd.read_csv('ejventas/Advertising.csv', index_col=0)
data
#.head()
data.to_csv('Advertising3.csv', sep=';')


# In[81]:


from os import listdir
from os.path import isfile, join
mi_path="./"
for archivo in listdir(mi_path):
    print(archivo)

