
# coding: utf-8

# In[1]:


from pyspark import SparkContext
sc = SparkContext("local[2]")


# In[42]:


customers_raw = sc.textFile("customers.txt")
print(customers_raw.take(5))
products_raw = sc.textFile("products.txt")
print(products_raw.take(5))
sales_raw = sc.textFile("sales.txt")
print(sales_raw.take(5))


# ### Buscar el 20% de los clientes que más han comprado
# #### A mi manera

# In[54]:


sales = sales_raw.filter(lambda linea: not "customer" in linea).map(lambda linea: (int(linea.split(",")[0]), int(linea.split(",")[2])))
sales.take(3)
sales_count = sales.groupByKey().map(lambda x: (x[0], len(x[1].data)))
mejores_sales = sc.parallelize(sales_count.takeOrdered(3, lambda x: -x[1]))
sales_count.takeOrdered(3, lambda x: -x[1])


# In[47]:


customers_name = customers_raw.filter(lambda linea: not "id" in linea).map(lambda linea: (int(linea.split(",")[0]), linea.split(",")[1]))
customers_name.collect()


# In[45]:


mejores_clientes = mejores_sales.join(customers_name)
mejores_clientes.collect()


# #### Resuelto en clase

# In[71]:


linea0cust = sc.parallelize(["id,name,sex"])
linea0sales = sc.parallelize(["customer,product,amount"])
linea0prod = sc.parallelize(["id,name"])


# In[72]:


cust_split = customers_raw.subtract(linea0cust).map(lambda linea: linea.split(","))
sales_split = sales_raw.subtract(linea0sales).map(lambda linea: linea.split(",")).map(lambda row: [row[0], row[1], int(row[2])])
products_split = products_raw.subtract(linea0prod).map(lambda linea: linea.split(","))


# In[73]:


n20pcust = int(cust_split.count()*2/10)
print("20% de clientes:", n20pcust)


# In[74]:


customer_pair = cust_split.map(lambda row: (row[0], (row[1], row[2])))
customer_pair.take(3)


# In[75]:


sales_pair = sales_split.map(lambda row: (row[0], row[2]))
sales_pair.take(2)


# In[80]:


sales_per_cust = sales_pair.join(customer_pair).map(lambda x: (x[1][1][0], 1))


# In[85]:


sales_per_cust.reduceByKey(lambda a, b: a + b).map(lambda x: (x[1], x[0])).top(n20pcust)


# ### Acumuladores

# In[49]:


acc = sc.accumulator(0)
noacc = 0

def sum(x):
    global noacc
    acc.add(x)
    noacc = noacc + 1

sc.parallelize([1, 2, 3, 4, 5, 6]).foreach(sum)
print("Acumulador:", acc.value)
print("No acumulador:", noacc)

