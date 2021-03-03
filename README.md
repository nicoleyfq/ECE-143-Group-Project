# UCSD ECE 143 Group Project - Team 14
This project is about Myer Briggs Personality Type(MBTI) data analysis and prediction using Python

## About Github Organization
1. **MBTI_Analysis** : this folder contains python program for analysis
2. **MBTI_Data** : this folder contains raw data
3. **Group Assignment** : validation test for Assignment #5
4. **environment.yml**: environment and dependencies file

## About Dataset: 
The original dataset contains over 8600 rows of data, on each row is a person’s:
Type (This persons 4 letter MBTI code/type)
A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))

## Data Cleaning (cleaned_raw.csv):

1. lower case the posts
1. replace ||| with double space
3. replace youtube website address with “youtube” and all other website with nothing
4. substitute punctuations, newline character, digits with nothing
5. apply word_tokenize, convert the text to list of words
6. remove **Stop Words**: Stop words are those words that do not contribute to the deeper meaning of the phrase.They are the most common words such as: “the“, “a“, and “is“.
 certain words are used to formulate sentences but do not add any semantic meaning to the text. For example, the most commonly used word in the english language is the which represents 7% of all words written or spoken. You couldn’t make deduce anything about a text given the fact that it contains the word the. On the other hand, words like good and awesome could be used to determine whether a rating was positive or not.

## Directory Guide:
.
├── Group\ Assignment
│   └── Group14_Assignment5.ipynb
├── MBTI_Analysis
│   ├── CalculateLenght.py
│   ├── Data_Process.py
│   ├── MBTI.ipynb      "jupyternote book for visualization"
│   ├── clean_data.py   "cleaned for modeling purpose"
│   ├── environment.yml
│   ├── extract_youtube.py
│   ├── keyword_analysis.py
│   └── library_requirement.py
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
└── tree.txt

4 directories, 35 files
.
├── Group\ Assignment
│   └── Group14_Assignment5.ipynb
├── MBTI_Analysis
│   ├── CalculateLenght.py
│   ├── Data_Process.py
│   ├── MBTI.ipynb
│   ├── clean_data.py
│   ├── environment.yml
│   ├── extract_youtube.py
│   ├── keyword_analysis.py
│   └── library_requirement.py
├── MBTI_Data
│   ├── Length_count.csv
│   ├── cleaned_raw.csv
│   ├── eng_stopwords.txt
│   ├── eng_stopwords1.txt
│   ├── mbti_1.csv
│   ├── processed_docs.csv
│   ├── raw_sentiment.csv
│   ├── seperated\ txt
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
│   └── youtube_links.csv
├── README.md
└── tree.txt

4 directories, 35 files

