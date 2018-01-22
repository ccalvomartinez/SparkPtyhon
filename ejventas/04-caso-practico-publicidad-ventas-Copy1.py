
# coding: utf-8

# ![](static/python.jpg)

# In[2]:


#from sklearn import datasets, linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('/home/jovyan/work/ejventas/Advertising.csv', index_col=0)
data.head()


# In[3]:


# 200 registros x 4 campos
data.shape


# In[4]:


# Visualización Relación entre Features y el Output usando Scatterplots
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='TV', y='Sales', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='Radio', y='Sales', ax=axs[1])
data.plot(kind='scatter', x='Newspaper', y='Sales', ax=axs[2])


# ### Preguntas a explorar
# 
# 1. Existe relación entre la publicidad y las ventas?
# 4. Cuál es el efecto de cada tipo de publicidad sobre las verntas?
# 5. Dado un determinado gasto en publicidad, podemos predecir las ventas?

# In[6]:


# Regresión Lineal Simple
# creacion X e y
feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales

# creacion y ajuste del modelo
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# intercepto y coeficientes
print (lm.intercept_)
print (lm.coef_)


# In[7]:


# Ploting resultados
plt.scatter(X, y,  color='black')
plt.plot(X, lm.predict(X), color='blue')


# In[8]:


# Utilizando el modelo para predecir: si gastamos 100 en TV, cuál sería las Ventas?
lm.predict(100)


# ### Regresión Lineal Múltiple

# In[10]:


# Creando X e y
features = ['TV', 'Radio', 'Newspaper']
X = data[features]
y = data.Sales

# Creacion y entrenamiento del modelo
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

# intercepto y coeficientes
print (lm.intercept_)
print (lm.coef_)


# In[14]:


# Regresión No-lineal
X2 = data[['TV']].assign(TV2 = lambda x: x*x)
#print(X2)
y = data.Sales
# creacion y ajuste del modelo
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X2, y)

# intercepto y coeficientes
print (lm.intercept_)
print (lm.coef_)


# In[15]:


# Ploting resultados
plt.scatter(X2.TV, y,  color='black')
plt.scatter(X2.TV, lm.predict(X2), color='blue')


# In[16]:


X2 =data[['TV']].assign(TV2 = lambda x: x*x)
X2_test = X2[-50:]
y = data.Sales
y_test = y[-50:]
# Ploting resultados
plt.scatter(X2_test.TV, y_test,  color='black')
plt.scatter(X2_test.TV, lm.predict(X2_test), color='red')


# In[17]:


# Coeficientes, Error Cuadrático Medio y Score Varianza Explicada (1 es predicción perfecta)
print('Coefficients: \n', lm.coef_)
print("Mean squared error: %.2f" % np.mean((lm.predict(X2) - y) ** 2))
print('Variance score: %.2f' % lm.score(X2, y))


# ### PRACTICA: modelo de regresión que mejore los modelos anteriores?! 

# In[18]:


X = data[['Radio', 'Newspaper']]
X_train = X[:-50]
y = data.Sales
y_train = y[:-50]

X_test = X[-50:]
y_test = y[-50:]
#y_tests


# In[19]:


# Nuestro modelo
# creacion y ajuste del modelo
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)

# intercepto y coeficientes
print lm.intercept_
print lm.coef_

# Coeficientes, Error Cuadrático Medio y Score Varianza Explicada (1 es predicción perfecta)
print('Coefficients: \n', lm.coef_)
print("Mean squared error: %.2f" % np.mean((lm.predict(X_test) - y_test) ** 2))
print('Variance score: %.2f' % lm.score(X_test, y_test))

# Ploteo resultados
plt.scatter(X_test.Radio, y_test,  color='black')
plt.plot(X_test.Radio, lm.predict(X_test), color='blue')


# In[20]:


get_ipython().system('dir')


# In[21]:


get_ipython().system('pwd')

