# Text-Analysis

# Text Analysis Project

This project aims to perform various types of text analysis to derive insights such as sentiment scores, readability, average word count, and other linguistic metrics. The analysis methodology focuses on financial texts, but can be applied to other types of textual data as well. 

## Table of Contents
1. [Overview](#overview)
2. [Setup and Installation](#setup-and-installation)
3. [Methodology](#methodology)
   - 3.1 [Sentimental Analysis](#sentimental-analysis)
       - 3.1.1 [Cleaning using Stop Words Lists](#cleaning-using-stop-words-lists)
       - 3.1.2 [Creating a Dictionary of Positive and Negative Words](#creating-a-dictionary-of-positive-and-negative-words)
       - 3.1.3 [Extracting Derived Variables](#extracting-derived-variables)
   - 3.2 [Analysis of Readability](#analysis-of-readability)
   - 3.3 [Average Number of Words Per Sentence](#average-number-of-words-per-sentence)
   - 3.4 [Complex Word Count](#complex-word-count)
   - 3.5 [Word Count](#word-count)
   - 3.6 [Syllable Count Per Word](#syllable-count-per-word)
   - 3.7 [Personal Pronouns](#personal-pronouns)
   - 3.8 [Average Word Length](#average-word-length)
4. [Results](#results)
5. [Contributing](#contributing)
6. [License](#license)

## Overview
The objective of this project is to analyze the given text data to derive sentimental opinions, sentiment scores, readability scores, passive words usage, personal pronouns, and more. It is designed to provide insights, especially for financial texts.



## Methodology

### 3.1 Sentimental Analysis
Sentimental Analysis is performed to classify the text as positive, negative, or neutral. The methodology adopted for the analysis is described below:

#### 3.1.1 Cleaning using Stop Words Lists
- The text is cleaned using stop words lists, which are stored in the `StopWords` folder. This step removes common stop words (e.g., "the", "is", "in") to focus on meaningful words that contribute to sentiment.

#### 3.1.2 Creating a Dictionary of Positive and Negative Words
- The project uses a master dictionary located in the `MasterDictionary` folder, which contains words classified as positive or negative.
- Words from the master dictionary are only added if they are not found in the stop words lists.

#### 3.1.3 Extracting Derived Variables
After cleaning the text, the following variables are calculated:
- Positive Score: Calculated by assigning +1 for each word found in the Positive Dictionary.
- Negative Score: Calculated by assigning -1 for each word found in the Negative Dictionary. The score is then multiplied by -1 to make it positive.
- Polarity Score: Determines if the text is positive or negative, using the formula:
  

### 3.4 Complex Word Count
- Complex words are defined as words that contain more than two syllables. These words are counted in this step.

### 3.5 Word Count
- The total number of words in the text is counted after cleaning. This involves:
1. Removing stop words (using the `stopwords` list from the `nltk` package).
2. Removing punctuation marks such as "?", "!", ",", and "." before counting.

### 3.6 Syllable Count Per Word
- The number of syllables in each word is counted. Special cases such as words ending with "es" or "ed" are handled, as they are not counted as additional syllables.

### 3.7 Personal Pronouns
- Personal pronouns are counted using regular expressions. The following pronouns are included: "I", "we", "my", "ours", and "us". The algorithm ensures that the country abbreviation "US" is excluded from the count.

### 3.8 Average Word Length
- Calculated using the formula:


## Results
The results of the text analysis are saved in a structured format, such as a CSV or JSON file, containing the calculated metrics. Example output includes the sentiment scores, readability scores, word counts, and other derived variables for each analyzed text.


