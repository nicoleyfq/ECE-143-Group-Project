# ECE-143-Team-14
Myer Briggs Personality Type

Dataset: 
The Myers Briggs Type Indicator (or MBTI for short) is a personality type system that divides everyone into 16 distinct personality types across 4 axis:
Introversion (I) – Extroversion (E)
Intuition (N) – Sensing (S)
Thinking (T) – Feeling (F)
Judging (J) – Perceiving (P)
So for example, someone who prefers introversion, intuition, thinking and perceiving would be labelled an INTP in the MBTI system, and there are lots of personality based components that would model or describe this person’s preferences or behaviour based on the label.
 
This dataset contains over 8600 rows of data, on each row is a person’s:
Type (This persons 4 letter MBTI code/type)
A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))


Data Cleaning for Posts:
1. lower case the posts
2. replace ||| with double space
3. replace youtube website address with “youtube” and all other website with nothing
4. substitute punctuations, newline character, digits with nothing
5. apply word_tokenize, convert the text to list of words
6. remove stop words: Stop words are those words that do not contribute to the deeper meaning of the phrase.They are the most common words such as: “the“, “a“, and “is“.
