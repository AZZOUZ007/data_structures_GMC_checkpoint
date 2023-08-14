#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Question 1 

L = [2,3,6]
n = 0
result = 1

for item in L:
    result *= L[n]
    n += 1
print(result)


# In[15]:


# Question 2
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#on commence par définir les fonctions qui font l'affaire:
def dernier_element(k):
    return k[-1]

def sort_tuples(tuple_list):
    sorted_list = sorted(tuple_list, key=dernier_element)
    return sorted_list

SORTED = sort_tuples(sample_list)

print(SORTED)
    


# In[29]:


# Question 3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

def dictionnaire_consolide(dict1, dict2):
    dict3 = {}
    
    for key, value in dict1.items():
        dict3[key] = dict3.get(key, 0) + value
        
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
    
    return dict3

resultat = dictionnaire_consolide(d1,d2)
print(resultat)
        


# In[34]:


# Question 4

def const_dict(N):
    consted_dict = {N : N*N for N in range(1, N+1)}
    return consted_dict
resultat = const_dict(8)
print(resultat)


# In[42]:


# Question 5

tu = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

def fl_element(t):
    return float(t[1])

def s_tuples(tuples_li):
    s_list = sorted(tuples_li, key= fl_element, reverse = True)
    return s_list

resultat = s_tuples(tu)
print(resultat)


# In[59]:


# Question 6

# creation de sets:
set1 = set()
N = 10
for i in range(N+1):
    set1.add(i)
print(set1)


# In[58]:


# iteration des set:
def iter_set(st):
    for item in st:
        print(item)
        


# In[56]:


iter_set(set1)


# In[ ]:




