#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
import pandas as pd 
import shutil
import sys
import os
import csv


# In[2]:


def createCsv(myDir):
    
    csvName = 'flower_lables.csv'
    if os.path.exists(csvName):
        os.remove(csvName) 
   
    with open(csvName, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["file"]+["label"])
    
    aux1 = -1
    aux2 = 0
    fileList = []
    
    for root, dirs, files in os.walk(myDir, topdown=False):
        aux1 += 1
        
        for name in files:
            
            if name.endswith('.jpg'):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
                aux2 += 1
                
                with open(csvName, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(["{:04n}".format(aux2)+".jpg"]+["{:01n}".format(aux1)])
    
    return os.path.dirname(os.path.realpath(csvName))+"/"+csvName


# In[3]:


def mergeAndRename(working_dir):
   
    dirName = "flower_images_2_new"
    dirCompleteName = "/home/edoardospinetti/Desktop/Progetto/flower_images_2_new/"
    aux = 0
    
    if os.path.exists(dirName):
            shutil.rmtree(dirName) 

    os.mkdir(dirName)

    for root, dirs, files in os.walk(working_dir):
            
            for filename in files:
                if filename.endswith('.jpg'):
                    aux += 1
                    fullName = os.path.join(root, filename)
                    shutil.copy(fullName, dirCompleteName)

                    newFullName = os.path.join(dirCompleteName, filename)
                    new_dst_file_name = os.path.join(dirCompleteName, "{:04n}".format(aux)+".jpg")
                    os.rename(newFullName, new_dst_file_name)
    
    return dirCompleteName


# In[4]:


def MakeFitDataset(working_dir):
   
    auxdirName = "flower_images_2_aux"
    auxdirCompleteName = "/home/edoardospinetti/Desktop/Progetto/flower_images_2_aux/"
    
    count = 0
    
    if os.path.exists(auxdirName):
        shutil.rmtree(auxdirName) 

    shutil.copytree(working_dir, auxdirName)
    
    for root, dirs, files in os.walk(auxdirName):
        for dirname in dirs:
            fullName = os.path.join(root, dirname)
            count = 0
            for root_, dirs_, files_ in os.walk(fullName):
                for filename in files_:
                    if filename.endswith('.jpg'):       
                        count += 1
                        if count >= 100:
                            fullName_ = os.path.join(auxdirCompleteName+dirname, filename)
                            os.remove(fullName_)
    
    csv_path = createCsv(auxdirCompleteName)
    target_path = mergeAndRename(auxdirCompleteName)
    shutil.rmtree(auxdirName)
    shutil.move(csv_path, target_path) 
    return "Done"


# In[5]:


#working_dir = "/home/edoardospinetti/Desktop/Progetto/flower_images_2/"
#MakeFitDataset(working_dir)

