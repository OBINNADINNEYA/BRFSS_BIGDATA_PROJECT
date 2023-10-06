#!/usr/bin/env python
# coding: utf-8

# Extracting the description and response meaning from the pdf document provided for BRFSS 2021 DATA

# In[1]:


# importing required modules
from PyPDF2 import PdfReader
import re
  
# creating a pdf reader object
reader = PdfReader('./2021-BRFSS-Questionnaire.pdf')
  
# printing number of pages in pdf file
#print(len(reader.pages))
  


# In[2]:


pages_text = []

for x in list(range(0,116)):
    
    page = reader.pages[x]
  
    # extracting text from page
    text = page.extract_text()
    
    #save the text in dict
    pages_text.append(text)


# In[3]:


#returning the page text with variable
def get_text(col):
    for text in pages_text[4:]:
        if col in text:
            return text

def extract_description(text, variable_name):
    if text is None:
        return None
    
    # Adjusted regex pattern to capture from the last full stop (.) before the variable name or the beginning
    # of the string, and then continue capturing until the next potential variable or end of the text
    pattern = r"(?:.*?\.)?\s*[^\.]*?" + re.escape(variable_name) + r".*?(?=[A-Z]+\d*\.|$)"
    
    matches = re.search(pattern, text, re.DOTALL)  # re.DOTALL ensures that '.' matches newline characters too

    if matches:
        description = "description of " + variable_name + ": " + matches.group(0).strip()
        return description
    else:
        return None



# In[4]:


#get_text('GENHLTH')


# In[5]:


import pandas as pd 


# In[6]:


df = pd.read_csv("./MMSA2021_Validation_1.csv")


# In[7]:


df.columns


# In[8]:


description_dict = {}
for col in list(df.columns):
    description_dict[col] = extract_description(get_text(col), col)


# In[9]:


#len(description_dict)



# In[11]:


#description_dict


# In[12]:


#getting information from second pdf file 

# creating a pdf reader object
reader = PdfReader('./2021-calculated-variables-version4-508.pdf')
  
# printing number of pages in pdf file
#print(len(reader.pages))  


# In[13]:


#creating a list of the page text

pages_text = []

for x in list(range(0,41)):
    
    page = reader.pages[x]
  
    # extracting text from page
    text = page.extract_text()
    
    #save the text in dict
    pages_text.append(text)


# In[14]:


#returning the page text with variable/col
def get_text(col):
    for text in pages_text[3:]:
        if col in text:
            return text

def extract_column_description(text, column_name):
    # Regex pattern to extract the text starting from "column_name is derived from" 
    # to just before "SAS Code"
    pattern = re.escape(column_name + " is derived from") + r".*?(?=SAS Code:)"
    
    matches = re.search(pattern, text, re.DOTALL)  # re.DOTALL makes . match newline characters too

    if matches:
        return matches.group(0).strip()
    else:
        return None


# In[15]:


variables_list = [
    'RENTHOM1', 'NUMHHOL3', 'NUMPHON3', 'CPDEMO1B', '_STSTR', '_IMPSEX',
    'CAGEG', '_RFHLTH', '_PHYS14D', '_MENT14D', '_HLTHPLN', '_HCVU652',
    '_TOTINDA', '_RFHYPE6', '_CHOLCH3', '_RFCHOL3', '_MICHD', '_LTASTH1',
    '_CASTHM1', '_ASTHMS1', '_DRDXAR3', '_LMTACT3', '_LMTWRK3', '_PRACE1',
    '_MRACE1', '_HISPANC', '_RACE', '_RACEG21', '_RACEGR3', '_RACEPRV',
    '_SEX', '_AGEG5YR', '_AGE65YR', '_AGE80', '_AGE_G', 'WTKG3', '_BMI5',
    '_BMI5CAT', '_RFBMI5', '_EDUCAG', '_INCOMG1', '_SMOKER3', '_RFSMOK3',
    '_CURECI1', 'DRNKANY5', '_RFBING5', '_DRNKWK1', '_RFDRHV7', '_FLSHOT7',
    '_PNEUMO3', '_AIDTST4', 'FTJUDA2_', 'FRUTDA2_', 'GRENDA1_', 'FRNCHDA_',
    'POTADA1_', 'VEGEDA2_', '_MISFRT1', '_MISVEG1', '_FRTRES1', '_VEGRES1',
    '_FRUTSU1', '_VEGESU1', '_FRTLT1A', '_VEGLT1A', '_FRT16A', '_VEG23A',
    '_FRUITE1', '_VEGETE1', '_MMSA', '_MMSAWT', 'SEQNO', 'MMSANAME'
]

for col in variables_list:
    description_dict[col] = extract_description(get_text(col), col)


# In[16]:


description_dict = description_dict

