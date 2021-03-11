# UCSD ECE 143 Group Project - Team 14
This project is about Myer Briggs Personality Type(MBTI) data analysis and prediction using Python

# Table of Contents  
1. [Folder Organization]((#folder) ) 
2. [How to Run Code](#run)  
3. [Directory Guide](#dir) 
4. [About Dataset](#data) 
5. [Data Cleaning](#clean) 

<a name="folder"/></a>
## Folder Organization
1. **MBTI_Analysis** : contains .py files for analysis, and .ipynb for all visualization
2. **MBTI_Data** : contains datasets for this project
3. **Group Assignment** : functional and validation test for Assignment #5
4. **environment.yml**: environment and dependencies file

<a name="run"/></a>
## How to Run Code
1. Reproduce environment using ./environment.yml
2. Run ./MBTI_Analysis/MBTI.ipynb for all data analysis,visulization and classification result. All .py files were used for preprocess data, and the results will be imported to jupyter notebook automatically.

<a name="dir"/></a>
## Directory Guide:
<pre>
├── Group\ Assignment
│   └── Group14_Assignment5.ipynb
├── MBTI_Analysis
│   ├── CalculateLenght.py
│   ├── Data_Process.py
│   ├── MBTI.ipynb      "jupyternote book for visualization"
│   ├── clean_data.py   "cleaned for modeling purpose"
│   ├── extract_youtube.py
│   ├── keyword_analysis.py
│   └── library_requirement.py
│   └──lstm_process.py  "used for lstm classification"
├── MBTI_Data
│   ├── Length_count.csv   "for length of posts analysis"
│   ├── cleaned_raw.csv
│   ├── eng_stopwords.txt
│   ├── eng_stopwords1.txt
│   ├── mbti_1.csv "raw txt from Kaggle"
│   ├── processed_docs.csv
│   ├── raw_sentiment.csv
│   ├── seperated\ txt  "16 txt file for each MBTI"
│   │   ├── ENFJ.txt
│   │   ├── ENFP.txt
│   │   ├── ENTJ.txt
│   │   ├── ENTP.txt
│   │   ├── ESFJ.txt
│   │   ├── ESFP.txt
│   │   ├── ESTJ.txt
│   │   ├── ESTP.txt
│   │   ├── INFJ.txt
│   │   ├── INFP.txt
│   │   ├── INTJ.txt
│   │   ├── INTP.txt
│   │   ├── ISFJ.txt
│   │   ├── ISFP.txt
│   │   ├── ISTJ.txt
│   │   └── ISTP.txt
│   └── youtube_links.csv   "extracted youtube links "
├── README.md
└── tree.txt    "directory tree"
└── environment.yml

4 directories, 36 files
</pre>

<a name="data"/></a>
## About Dataset: 
The original dataset contains over 8600 rows of data, on each row is a person’s:
Type (This persons 4 letter MBTI code/type)
A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))

<a name="clean"/></a>
## Data Cleaning (cleaned_raw.csv):
1. lower case the posts
1. replace ||| with double space
3. replace youtube website address with “youtube” and all other website with nothing
4. substitute punctuations, newline character, digits with nothing
5. apply word_tokenize, convert the text to list of words
6. remove **Stop Words**: Stop words are those words that do not contribute to the deeper meaning of the phrase.They are the most common words such as: “the“, “a“, and “is“.
 certain words are used to formulate sentences but do not add any semantic meaning to the text. For example, the most commonly used word in the english language is the which represents 7% of all words written or spoken. You couldn’t make deduce anything about a text given the fact that it contains the word the. On the other hand, words like good and awesome could be used to determine whether a rating was positive or not.