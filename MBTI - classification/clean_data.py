import pandas as pd
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

data = pd.read_csv('mbti_1.csv')
print(data.shape)
data.head()

def cleaning(posts):
    posts = posts.lower()
    posts = posts.replace('|||',' ')
    posts = re.sub('https?://\S+|www\.youtube\S+', 'youtube', posts)
    posts = re.sub('https?://\S+|www\.\S+', '', posts)
    posts = re.sub('\[.*?\]', '', posts)
    posts = re.sub('<.*?>+', '', posts)
    posts = re.sub('[%s]' % re.escape(string.punctuation), '', posts)
    posts = re.sub('\n', '', posts)
    posts = re.sub('\w*\d\w*', '', posts)
    return posts



data['clean'] = data['posts'].apply(cleaning) 
print('Cleaned')

data['tokenized'] = data['clean'].apply(word_tokenize) 
print('Tokenized')

stop_words = stopwords.words('english')
def remove_stop_words(post):
    return [w for w in post if not w in stop_words]
data['remove_stop'] = data['tokenized'].apply(remove_stop_words)
data['final'] = data['remove_stop'].apply(lambda w:" ".join(w)) 
print('Done')

data[['type','final']].to_csv('cleaned_raw.csv')