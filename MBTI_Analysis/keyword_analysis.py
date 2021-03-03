'''
for data exploration only, no output produced
this program anlyze key words for posts
'''
from ipywidgets import widgets,interact,interactive,fixed
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from string import digits 
import spacy
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
from gensim import corpora, models

def cal_words_importance(corpus,n,tf):
    tfidf_matrix = (tf.transform(corpus)).sum(axis=0) 
    score = [(w,tfidf_matrix[0,i]) for w,i in tf.vocabulary_.items()]
    score_n =sorted(score, key = lambda x: x[1], reverse=True)[:n]
    return score_n

top_words = {}
tf = TfidfVectorizer().fit(data['final']) #Learn vocabulary and idf from training set.
ls = data['type'].unique()
for personality in tqdm(ls):
    sub_data = data[data['type'] == personality]
    res = cal_words_importance(sub_data['final'],10,tf)
    top_words[personality] = res
all_docs = []
for s in tqdm('EI'):
    sub_data = data[data['type'].str.contains(s)]
    str_ls = "".join(sub_data['final'])
    all_docs.append(str_ls)
vec = TfidfVectorizer(max_features=2000)
transformed = vec.fit_transform(all_docs) 

words_score = {}
transformed_documents_as_array = transformed.toarray()
for counter, doc in enumerate(transformed_documents_as_array):
    # construct a dataframe
    tf_idf_tuples = list(zip(vec.get_feature_names(), doc))
    one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['term', 'score']).sort_values(by='score', ascending=False).reset_index(drop=True)
    words_score[ls[counter]] = one_doc_as_df[:20]


def plot_bar(personality):
    
    importance = [top_words[personality][i][1] for i in range(10)]
    words = [top_words[personality][i][0] for i in range(10)]
    plt.figure(figsize=[16,5])

    sns.barplot(y = words,x = importance,palette ="Set2")
    plt.title('Important Words')
    plt.xlabel('TF-IDF Score')

#interact(plot_bar,Category=top_words.keys(),mytitle=fixed('Words Importance'),personality = top_words.keys())

###funtion for cloud that Im going to call with interact  ######  
stop_words = stopwords.words('english')
stop_words.extend(['im','like','dont','think','people','know','would','one',
                   'thing','get','well','really','ive','type','time',
                   'INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP', 
                   'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ',
                   'ISTPS','ISFPS','ESFJS'])
def load_mask_image(path):
    mask = np.array(Image.open(path))
    #mask[mask > 200] = 255
    #mask[mask <= 200] = 0
    return mask

#mask = load_mask_image('mask.png')
def makingclouds(personality,maximum):
    personality_data = data[data['type'] == personality]
    text = " ".join(personality_data['final'].tolist())
    wc = WordCloud(background_color="white", max_words=maximum, mask=mask,
                   stopwords=stop_words, contour_width=3)

    # Generate a wordcloud
    wc.generate(text)

    # show
    plt.figure(figsize=[20,6])
    plt.subplot(121)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")

#interact(makingclouds, Category=ls, personality = ls, maximum=[20,50,100,150])


cv = CountVectorizer(max_features=2000, strip_accents='ascii')
result = cv.fit_transform(data['final'])

tf_vec=TfidfVectorizer(use_idf=True,max_features=2000)
result = tf_vec.fit_transform(data['final'])


m_new = pd.concat([m, pd.DataFrame(result.toarray(), columns=['__' + k for k in cv.vocabulary_.keys()])],axis=1)
words_col = [col for col in m_new.columns if col.startswith('__') and len(col) > 5]
tf = m_new[words_col]#.T[m_new[words_col].mean() >= 0.5].T

def unique_words_plot(personality1, personality2):
    a = personality1
    b = personality2
    a_avg = tf[m_new[a] == 1].sum() 
    b_avg = tf[m_new[b] == 1].sum()
    ratio = a_avg / b_avg
    bar_plot = ratio.sort_values().rename(lambda x: x[2:]).tail(10)
    plt.figure(figsize=[16,4])
    sns.barplot(x=bar_plot.values,y=bar_plot.index,palette ="Set2")
    plt.title(mapping[a] + ' vs ' + mapping[b])
    plt.xlabel('Importance Ratio')
    

#interact(unique_words_plot,mytitle=fixed('Words Importance'),personality1 = mapping.keys(),personality2 = mapping.keys())

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(token)
    return result

# data['processed'] = data['final'].map(preprocess)
# data['processed'][:20]

dictionary = gensim.corpora.Dictionary(data['processed'])
count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 12:
        break
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

def radar_plot(personality1, personality2,ls):
    a = personality1
    b = personality2
    a_avg = tf[m_new[a] == 1].sum() 
    b_avg = tf[m_new[b] == 1].sum()
    res_a = []
    res_b = []
    for i in ls:
        res_a.append(a_avg['__'+i])
        res_b.append(b_avg['__'+i])
    return res_a,res_b
#ls = ['good','great','fine','fantasy','excellent']
#res_a,res_b = radar_plot("J","P",ls)
#print(res_a,res_b)
def count_phrase(p1, p2,phrase):
    freq = data.groupby(['type'])['final'].apply(lambda x: x[x.str.contains(phrase)].count())
    freq = freq.to_frame()
    freq.reset_index(inplace=True)
    joined = pd.merge(freq,type_count,on='type')
    joined['type']= joined['type'].apply(lambda x: p1 if p1 in x else p2)
    freq_by_c = joined.groupby(['type']).sum().eval('ratio = final / count')

    return freq_by_c

def cal_phrase(p1,p2,ls):
    p1_res = []
    p2_res = []
    for i in ls:
        res = count_phrase(p1,p2,i)
        res.reset_index(inplace=True)
        temp1 = res.loc[res['type']==p1].ratio.item()*100
        temp2 = res.loc[res['type']==p2].ratio.item()*100
        p1_res.append(round(temp1,2))
        p2_res.append(round(temp2,2))
    
    return p1_res,p2_res
