
# coding: utf-8

# In[2]:


print('Hola Clase! Les dio tiempo a cenar? A mi no.')


# local[2] El 2 indica el número de cores que se utilizan

# In[1]:


import pyspark
sc = pyspark.SparkContext('local[2]')


# In[33]:


data = sc.textFile('/home/jovyan/work/ejventas/Advertising.csv')
get_ipython().system('pwd')


# In[34]:


data


# In[35]:


data.count()


# In[36]:


type(data)


# #### Calcular la media de longitudes de las líneas de un fichero
# 1. Método sencillo

# In[37]:


longitudes = data.map(lambda linea: len(linea))
longitudes.take(3)


# In[38]:


# Filtrar las líneas vacías (ponemos mayor que dos para evitar líneas con sólo espacios o caracteres raros)
longitudes_filtradas = longitudes.filter(lambda lon: lon > 2)


# In[39]:


total_lineas = longitudes_filtradas.reduce(lambda a, b: a+b)
media = total_lineas / longitudes_filtradas.count()
print("Total líneas:", total_lineas)
print("Media:", media)


# 2. Método con AGGREGATE

# In[42]:


res = longitudes_filtradas.aggregate((0,0), lambda acc, x: (acc[0]+x, acc[1] +1), lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]))

print(res[0]/res[1])


# _______________________________________________________

# In[45]:


def accParticiones(acc, x):
     return acc + x

def accTotal(acc1, acc2):
    return acc1 + acc2

res2 = longitudes_filtradas.aggregate(0, accParticiones, accTotal)

print(res2)


# In[2]:


rdd = sc.parallelize([1, 2, 3, 4, 5])


# In[3]:


rdd.reduce(lambda a, b: a + b)


# In[5]:


rdd.fold(1, lambda a, b: a + b)

