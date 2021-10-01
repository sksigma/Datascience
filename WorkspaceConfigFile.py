#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.chdir('C:/Users/Shubham Kansal/Desktop/Python_Directory/ModelDeployment')


# ## Workspace & ResourceGroup

# In[1]:


from azureml.core import Workspace, Dataset, Datastore

ws = Workspace.create(name='Deployment_Workspace',
                      subscription_id='597aaac7-ba77-4b65-a624-d472f5085556',
                      resource_group='TestDeployment',
                      create_resource_group=True,   # True if it does not exist
                      location='eastus',
                      exist_ok= True)

ws.write_config(path=".")


# ## Datastore

# In[2]:


from azureml.core import Datastore

az_store = Datastore.register_azure_blob_container(
           workspace=ws,
           datastore_name="deploydatastore",
           account_name="depstorageact",
           container_name="deploycontainer",
           account_key="JApqGoyp+TkqmCNnJVpQD0BUqQyVbnO8zt1e/vVBbr2/+71iK1+DWMdlUq+b9JX7xwFl+CGdZ8x08hpCZrdBHg==")


# ## Dataset

# In[3]:


from azureml.core import Dataset
az_store = Datastore.get(ws, "deploydatastore")

# -----------------------------------------------------
# Create and register the dataset
# -----------------------------------------------------

# Create the path of the csv file
csv_path = [(az_store, "Dataset/adultIncome.csv")] #path of the file stored in the storage account

# Create the dataset
loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)
# Register the dataset
loan_dataset = loan_dataset.register(workspace=ws,
                                     name="Deploydataset",
                                     create_new_version=True)

***************************************************ConfigurationEnd************************************************************