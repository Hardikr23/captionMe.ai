#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import text2emotion as te
import pandas as pd
import json

# In[11]:


def generate_celeb_vector(celebrity):
    Text = celebrity.content.reset_index(drop=True)
    n=len(Text)
    empty =[]
    Happycount =0
    Angrycount=0
    Surprisecount=0
    Sadcount=0
    fearcount = 0
    for i in range(len(Text)):
        sccore = te.get_emotion(Text[i])
        empty.append(sccore)
        keys =list(sccore.keys())
        values = list(sccore.values())
        max_idx =  values.index(max(values))
        max_key = keys[max_idx]
        #print(max_key)
        if max_key == 'Happy':
            Happycount += 1
        elif max_key == 'Angry':
            Angrycount += 1
        elif max_key == 'Surprise':
            Surprisecount += 1
        elif max_key == 'Sad':
            Sadcount += 1
        else:
            fearcount += 1
    arr = np.array([Happycount/n,Angrycount/n,Surprisecount/n,Sadcount/n,fearcount/n])
    return arr


# In[12]:


def read_celeb_csv(celeb_file_path):
    dataframe = pd.read_csv(celeb_file_path)
    ellen=dataframe.query('author == "TheEllenShow"')
    barack=dataframe.query('author == "BarackObama"')
    rihanna=dataframe.query('author == "rihanna"')
    cristiano=dataframe.query('author == "Cristiano"')
    justinbieber=dataframe.query('author == "justinbieber"')
    celeb_dict = {
        "ellen": ellen,
        "barack": barack,
        "rihanna": rihanna,
        "cristiano": cristiano,
        "JB": justinbieber
    }
    celeb_emotion_dict={}
    for celeb in celeb_dict.keys():
        celeb_emotion_dict[celeb]=generate_celeb_vector(celeb_dict[celeb])
    outfile_path = "celeb_emotion_dict.json"
    outfile_id = open(outfile_path,"w")
    outfile_id.write(json.dumps(celeb_emotion_dict))
    outfile_id.close()
    return celeb_emotion_dict


# In[ ]:




