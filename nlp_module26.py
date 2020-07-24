import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech
text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."
cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)
stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]
print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)

import spacy
from nltk import Tree
from squids import squids_text
dependency_parser = spacy.load('en')
parsed_squids = dependency_parser(squids_text)
# Assign my_sentence a new value:
my_sentence = "The world is a crazy place to live in"
my_parsed_sentence = dependency_parser(my_sentence)
def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_
for sent in parsed_squids.sents:
  to_nltk_tree(sent.root).pretty_print()
for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()

# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech
# Change text to another string:
text = looking_glass_text
cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)
stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]
normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
# Comment out the print statement below
#print(normalized)
bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)

import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter
from looking_glass import looking_glass_full_text
cleaned = re.sub('\W+', ' ', looking_glass_full_text).lower()
tokenized = word_tokenize(cleaned)
# Change the n value to 2:
looking_glass_bigrams = ngrams(tokenized, 2)
looking_glass_bigrams_frequency = Counter(looking_glass_bigrams)
# Change the n value to 3:
looking_glass_trigrams = ngrams(tokenized, 3)
looking_glass_trigrams_frequency = Counter(looking_glass_trigrams)
# Change the n value to a number greater than 3:
looking_glass_ngrams = ngrams(tokenized, 5)
looking_glass_ngrams_frequency = Counter(looking_glass_ngrams)
print("Looking Glass Bigrams:")
print(looking_glass_bigrams_frequency.most_common(10))
print("\nLooking Glass Trigrams:")
print(looking_glass_trigrams_frequency.most_common(10))
print("\nLooking Glass n-grams:")
print(looking_glass_ngrams_frequency.most_common(10))

import nltk, re
from sherlock_holmes import bohemia_ch1, bohemia_ch2, bohemia_ch3, boscombe_ch1, boscombe_ch2, boscombe_ch3
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
# preparing the text
corpus = [bohemia_ch1, bohemia_ch2, bohemia_ch3, boscombe_ch1, boscombe_ch2, boscombe_ch3]
preprocessed_corpus = [preprocess_text(chapter) for chapter in corpus]
# Update stop_list:
stop_list = ["see", 'say','one','upon','know','may', 'man', 'come', 'could', 'would']
# filtering topics for stop words
def filter_out_stop_words(corpus):
  no_stops_corpus = []
  for chapter in corpus:
    no_stops_chapter = " ".join([word for word in chapter.split(" ") if word not in stop_list])
    no_stops_corpus.append(no_stops_chapter)
  return no_stops_corpus
filtered_for_stops = filter_out_stop_words(preprocessed_corpus)
# creating the bag of words model
bag_of_words_creator = CountVectorizer()
bag_of_words = bag_of_words_creator.fit_transform(filtered_for_stops)
# creating the tf-idf model
tfidf_creator = TfidfVectorizer(min_df = 0.2)
tfidf = tfidf_creator.fit_transform(preprocessed_corpus)
# creating the bag of words LDA model
lda_bag_of_words_creator = LatentDirichletAllocation(learning_method='online', n_components=10)
lda_bag_of_words = lda_bag_of_words_creator.fit_transform(bag_of_words)
# creating the tf-idf LDA model
lda_tfidf_creator = LatentDirichletAllocation(learning_method='online', n_components=10)
lda_tfidf = lda_tfidf_creator.fit_transform(tfidf)
print("~~~ Topics found by bag of words LDA ~~~")
for topic_id, topic in enumerate(lda_bag_of_words_creator.components_):
  message = "Topic #{}: ".format(topic_id + 1)
  message += " ".join([bag_of_words_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
  print(message)
print("\n\n~~~ Topics found by tf-idf LDA ~~~")
for topic_id, topic in enumerate(lda_tfidf_creator.components_):
  message = "Topic #{}: ".format(topic_id + 1)
  message += " ".join([tfidf_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
  print(message)
