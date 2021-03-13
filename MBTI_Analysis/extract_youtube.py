'''
this file produce list of youtube links in all the posts
'''

import pandas as pd
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import re
#link_regex = re.compile('(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\'.,<>?«»“”‘’]))')   
data = pd.read_csv('mbti_1.csv')
def cleaning(posts):
    posts = posts.replace('|||',' ')
    posts = re.findall('(https?://[^\s]+)', posts)
    #youtube_ls.append(links)
    return posts

data['clean'] = data['posts'].apply(cleaning) 
data = data[data.clean.str.len() != 0]
lst_col = 'clean'
df = pd.DataFrame({col:np.repeat(data[col].values, data[lst_col].str.len())
    for col in data.columns.difference([lst_col])}).assign(**{lst_col:np.concatenate(data[lst_col].values)})[data.columns.tolist()]
df = df[df.clean.str.contains('youtu')]

df[['type','clean']].to_csv('youtube_links.csv')

print('Cleaned')