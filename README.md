# ECE 143 Group Project - Team 14
Myer Briggs Personality Type Analysis using Python

## About Github Organization
1. **MBTI_Analysis** : this folder contains python program for analysis
2. **MBTI_Data** : this folder contains raw data
3. Group14_Assignment5.ipynb : this is validation test for Assignment #5


## About Dataset: 

    The Myers Briggs Type Indicator (or MBTI for short) is a personality type system that divides everyone into 16 distinct personality types across 4 axis:
    * Introversion (I) – Extroversion (E)
    * Intuition (N) – Sensing (S)
    * Thinking (T) – Feeling (F)
    * Judging (J) – Perceiving (P) 
 
    This dataset contains over 8600 rows of data, on each row is a person’s:
    Type (This persons 4 letter MBTI code/type)
    A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))


## Data Cleaning for Posts:

1. lower case the posts
1. replace ||| with double space
3. replace youtube website address with “youtube” and all other website with nothing
4. substitute punctuations, newline character, digits with nothing
5. apply word_tokenize, convert the text to list of words
6. remove **Stop Words**: Stop words are those words that do not contribute to the deeper meaning of the phrase.They are the most common words such as: “the“, “a“, and “is“.
 certain words are used to formulate sentences but do not add any semantic meaning to the text. For example, the most commonly used word in the english language is the which represents 7% of all words written or spoken. You couldn’t make deduce anything about a text given the fact that it contains the word the. On the other hand, words like good and awesome could be used to determine whether a rating was positive or not.

## Exploratory Data Analysis

### Top words related to certain personality type
Methodology: **TF-IDF**
    Score the relative importance of wordA statistical measure that evaluates how relevant a word is to a document in a collection of documents. This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents.
