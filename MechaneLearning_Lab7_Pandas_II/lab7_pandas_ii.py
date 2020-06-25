# -*- coding: utf-8 -*-
"""Lab7_Pandas-II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ezmtbK35OZOqPTWfH3FVRzAgOIcEo8B
"""

#---------------Lab 7 Pandas-II-------------
#---------------------Pickle---------------------
from google.colab import drive 
drive.mount('/content/drive')
# mount '/content/drive' to virtual machine directory for google colab user 
#below where the file is in gdrive, change with your
data_path = "/content/drive/My Drive/Colab Notebooks/"

import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
filename = 'dogs'
outfile = open(data_path+filename,'wb')	# b: binary 
pickle.dump(dogs_dict,outfile)
outfile.close()	# File "dogs" will be created in your google drive

infile = open(data_path+filename,'rb') 
new_dict = pickle.load(infile) 

infile.close()

print(new_dict) 
print(new_dict==dogs_dict) 
print(type(new_dict))

import bz2	# Compressing pickle files 

sfile = bz2.BZ2File(data_path+'smallerfile', 'w')
pickle.dump(dogs_dict, sfile) # zipped file "smallerfile" will be in your google drive

infile = open(data_path+filename,'rb')
new_dict = pickle.load(infile, encoding='latin1')


#--------------Get dataset from website-------
!pip install quandl 
import quandl 
import pandas as pd

# Access to https://www.quandl.com/
# Create account and then you will get your own api key 
# DON'T USE MY API KEY

api_key = 'y2STCX7sevxLxJpHyEXX'
df = quandl.get("FMAC/HPI_TX", authtoken=api_key)
print(df.head())


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states) 
print(fiddy_states[0])