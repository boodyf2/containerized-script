import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# download ntlk stopwords list
nltk.download('stopwords')
nltk.download('punkt')

# a function to remove stopwords
def remove_stopwords(text, stopwords):
    words = nltk.word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() not in stopwords and word.lower().strip(string.punctuation)]
    return cleaned_words

# a function to count the words
def count_words(words_list):
   word_counts = Counter(words_list)
   return word_counts 

# read paragraphs from the file
with open(r"./random_paragraphs.txt", "r") as file:
    paragraphs = file.read()

# get stopwords
stop_words = set(stopwords.words('english'))

# remove stopwords
cleaned_text = remove_stopwords(paragraphs, stop_words)
words_count = count_words(cleaned_text)

# print the frequency of each word
for word, count in words_count.items():
    print(f"{word}: {count}")