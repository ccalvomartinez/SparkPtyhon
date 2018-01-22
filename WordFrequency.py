
# coding: utf-8

# In[16]:


import pyspark
sc = pyspark.SparkContext('local[2]')


# In[17]:


all_lines = sc.textFile('/home/jovyan/work/don-quijote.txt')
type(all_lines)


# In[3]:


lines_non_empty = all_lines.filter(lambda line: len(line.strip())>0)
lines_non_empty.count()


# In[4]:


counts = lines_non_empty.flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)


# In[5]:


counts.take(10)


# In[7]:


words = lines_non_empty.flatMap(lambda line: line.split(' ')).map(lambda word: word.strip().strip('.').strip(','))
words.take(10)


# In[10]:


characters = words.flatMap(lambda word: word).map(lambda char: char.lower())
characters.take(10)


# In[15]:


letter_count = characters.map(lambda char: (char, 1)).reduceByKey(lambda a, b: a + b)
letter_count.sortBy(lambda x: x[1], False).collect()

