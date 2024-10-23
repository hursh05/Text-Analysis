# Import necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ensure the TitleText directory exists
os.makedirs('TitleText', exist_ok=True)

# Read the URL file into a pandas DataFrame
df = pd.read_excel('Input.xlsx')

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']

    # Make a request to the URL
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=header)
    except:
        print("Can't get response of {}".format(url_id))
        continue

    # Create a BeautifulSoup object
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
    except:
        print("Can't get page of {}".format(url_id))
        continue

    # Find the title
    try:
        title = soup.find('h1').get_text()
    except:
        print("Can't get title of {}".format(url_id))
        continue

    # Find the text
    article = ""
    try:
        for p in soup.find_all('p'):
            article += p.get_text()
    except:
        print("Can't get text of {}".format(url_id))

    # Write title and text to a file
    file_name = f'TitleText/{url_id}.txt'
    with open(file_name, 'w', encoding='utf-8') as file:  # Specify encoding here
        file.write(title + '\n' + article)

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Directories
text_dir = "TitleText"
stopwords_dir = "StopWords"
sentiment_dir = "MasterDictionary"

# Load all stop words from the stopwords directory and store in a set
stop_words = set()
for files in os.listdir(stopwords_dir):
    with open(os.path.join(stopwords_dir, files), 'r', encoding='utf-8', errors='ignore') as f:
        stop_words.update(set(f.read().splitlines()))

# Load all text files from the directory and store in a list (docs)
docs = []
for text_file in os.listdir(text_dir):
    with open(os.path.join(text_dir, text_file), 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        # Tokenize the given text file
        words = word_tokenize(text)
        # Remove the stop words from the tokens
        filtered_text = [word for word in words if word.lower() not in stop_words]
        # Add each filtered tokens of each file into a list
        docs.append(filtered_text)

# Store positive and negative words from the directory
pos = set()
neg = set()

for files in os.listdir(sentiment_dir):
    if files == 'positive-words.txt':
        with open(os.path.join(sentiment_dir, files), 'r', encoding='utf-8', errors='ignore') as f:
            pos.update(f.read().splitlines())
    else:
        with open(os.path.join(sentiment_dir, files), 'r', encoding='utf-8', errors='ignore') as f:
            neg.update(f.read().splitlines())

# Now collect the positive and negative words from each file and calculate the scores
positive_words = []
negative_words = []
positive_score = []
negative_score = []
polarity_score = []
subjectivity_score = []

# Iterate through the list of docs
for i in range(len(docs)):
    positive_words.append([word for word in docs[i] if word.lower() in pos])
    negative_words.append([word for word in docs[i] if word.lower() in neg])
    positive_score.append(len(positive_words[i]))
    negative_score.append(len(negative_words[i]))
    polarity_score.append((positive_score[i] - negative_score[i]) / ((positive_score[i] + negative_score[i]) + 0.000001))
    subjectivity_score.append((positive_score[i] + negative_score[i]) / ((len(docs[i])) + 0.000001))


import os
import re
from nltk.corpus import stopwords

# Directories
text_dir = "TitleText"
stopwords_set = set(stopwords.words('english'))

# Average Sentence Length, Percentage of Complex words, and Fog Index
avg_sentence_length = []
percentage_of_complex_words = []
fog_index = []
complex_word_count = []
avg_syllable_word_count = []

def measure(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        # Remove punctuations
        text = re.sub(r'[^\w\s.]', '', text)
        # Split the given text file into sentences
        sentences = text.split('.')
        # Total number of sentences in a file
        num_sentences = len(sentences)
        # Total words in the file
        words = [word for word in text.split() if word.lower() not in stopwords_set]
        num_words = len(words)

        # Complex words having syllable count greater than 2
        complex_words = []
        for word in words:
            vowels = 'aeiou'
            syllable_count_word = sum(1 for letter in word if letter.lower() in vowels)
            if syllable_count_word > 2:
                complex_words.append(word)

        # Syllable Count Per Word
        syllable_count = 0
        syllable_words = []
        for word in words:
            if word.endswith('es'):
                word = word[:-2]
            elif word.endswith('ed'):
                word = word[:-2]
            vowels = 'aeiou'
            syllable_count_word = sum(1 for letter in word if letter.lower() in vowels)
            if syllable_count_word >= 1:
                syllable_words.append(word)
                syllable_count += syllable_count_word

        avg_sentence_len = num_words / num_sentences if num_sentences != 0 else 0
        avg_syllable_word_count = syllable_count / len(syllable_words) if len(syllable_words) != 0 else 0
        percent_complex_words = len(complex_words) / num_words if num_words != 0 else 0
        fog_index = 0.4 * (avg_sentence_len + percent_complex_words)

        return avg_sentence_len, percent_complex_words, fog_index, len(complex_words), avg_syllable_word_count

# Iterate through each file or doc
for file in os.listdir(text_dir):
    x, y, z, a, b = measure(file)
    avg_sentence_length.append(x)
    percentage_of_complex_words.append(y)
    fog_index.append(z)
    complex_word_count.append(a)
    avg_syllable_word_count.append(b)


import os
import re
from nltk.corpus import stopwords

# Directories
text_dir = "TitleText"
stopwords_set = set(stopwords.words('english'))

# Word Count and Average Word Length
def cleaned_words(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        text = re.sub(r'[^\w\s]', '', text)
        words = [word for word in text.split() if word.lower() not in stopwords_set]
        length = sum(len(word) for word in words)
        average_word_length = length / len(words) if len(words) != 0 else 0
    return len(words), average_word_length

word_count = []
average_word_length = []
for file in os.listdir(text_dir):
    x, y = cleaned_words(file)
    word_count.append(x)
    average_word_length.append(y)

# Count Personal Pronouns
def count_personal_pronouns(file):
    with open(os.path.join(text_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        personal_pronouns = ["I", "we", "my", "ours", "us"]
        count = 0
        for pronoun in personal_pronouns:
            count += len(re.findall(r"\b" + pronoun + r"\b", text))  # \b is used to match word boundaries
    return count

pp_count = []
for file in os.listdir(text_dir):
    x = count_personal_pronouns(file)
    pp_count.append(x)


# Read the output data structure template
output_df = pd.read_excel('Output Data Structure.xlsx')

# URL_ID 44, 57, 144 do not exist, i.e., page does not exist, throws 404 error
# So we are going to drop these rows from the table
output_df.drop([44-37, 57-37, 144-37], axis=0, inplace=True)

# These are the required parameters
variables = [positive_score,
             negative_score,
             polarity_score,
             subjectivity_score,
             avg_sentence_length,
             percentage_of_complex_words,
             fog_index,
             avg_sentence_length,
             complex_word_count,
             word_count,
             avg_syllable_word_count,
             pp_count,
             average_word_length]

for i, var in enumerate(variables):
    output_df.iloc[:, i+2] = var

output_df.to_csv('Output_Data.csv', index=False)