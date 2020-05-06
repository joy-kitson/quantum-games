#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
#from qiskit.providers.ibmq import least_busy
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider1 = IBMQ.load_account()


# In[2]:


provider = IBMQ.get_provider(hub='ibm-q')
provider.backends()


# In[3]:


backend = provider.get_backend('ibmq_16_melbourne')
backend


# In[4]:


provider.backends(simulator=False, operational=True)


# In[5]:


provider.backends(filters=lambda x: x.configuration().n_qubits >= 10
                                    and not x.configuration().simulator
                                    and x.status().operational==True)


# In[ ]:




