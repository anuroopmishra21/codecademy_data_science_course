from preprocessing import preprocess_text
# Define text_to_bow() below:
def text_to_bow(some_text):
  bow_dictionary = {}
  tokens = preprocess_text(some_text)
  for token in tokens:
    if token in bow_dictionary:
      bow_dictionary[token] +=1
    else:
      bow_dictionary[token] = 1
  return bow_dictionary
print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))

from preprocessing import preprocess_text
# Define create_features_dictionary() below:
def create_features_dictionary(documents):
  features_dictionary = {}
  merged = " ".join(documents)
  tokens = preprocess_text(merged)
  index = 0
  for token in tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary, tokens
training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]
print(create_features_dictionary(training_documents)[0])

from preprocessing import preprocess_text
# Define text_to_bow_vector() below:
def text_to_bow_vector(some_text, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  tokens = preprocess_text(some_text)
  for token in tokens:
    feature_index = features_dictionary[token]
    bow_vector[feature_index] += 1
  return bow_vector, tokens
features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}
text = "Another five fish find another faraway fish."
print(text_to_bow_vector(text, features_dictionary)[0])

from spam_data import training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, training_docs, test_docs
from sklearn.naive_bayes import MultinomialNB
def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary
def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector
# Define bow_sms_dictionary:
bow_sms_dictionary = create_features_dictionary(training_doc_tokens)
# Define training_vectors:
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]
# Define test_vectors:
test_vectors = [tokens_to_bow_vector(test_doc, bow_sms_dictionary) for test_doc in test_spam_docs]
spam_classifier = MultinomialNB()
def spam_or_not(label):
  return "spam" if label else "not spam"
# Uncomment the code below when you're done:
spam_classifier.fit(training_vectors, training_labels)
predictions = spam_classifier.score(test_vectors, test_labels)
print("The predictions for the test data were {0}% accurate.\n\nFor example, '{1}' was classified as {2}.\n\nMeanwhile, '{3}' was classified as {4}.".format(predictions * 100, test_docs[0], spam_or_not(test_labels[0]), test_docs[10], spam_or_not(test_labels[10])))

from spam_data import training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, training_docs, test_docs
from sklearn.naive_bayes import MultinomialNB
# Import CountVectorizer from sklearn:
from sklearn.feature_extraction.text import CountVectorizer
# Define bow_vectorizer:
bow_vectorizer = CountVectorizer()
# Define training_vectors:
training_vectors = bow_vectorizer.fit_transform(training_docs)
# Define test_vectors:
test_vectors = bow_vectorizer.transform(test_docs)
spam_classifier = MultinomialNB()
def spam_or_not(label):
  return "spam" if label else "not spam"
spam_classifier.fit(training_vectors, training_labels)
predictions = spam_classifier.score(test_vectors, test_labels)
print("The predictions for the test data were {0}% accurate.\n\nFor example, '{1}' was classified as {2}.\n\nMeanwhile, '{3}' was classified as {4}.".format(predictions * 100, test_docs[7], spam_or_not(test_labels[7]), test_docs[15], spam_or_not(test_labels[15])))

from preprocessing import preprocess_text
from nltk.util import ngrams
from collections import Counter
text = "It's exciting to watch flying fish after a hard day's work. I don't know why some fish prefer flying and other fish would rather swim. It seems like the fish just woke up one day and decided, 'hey, today is the day to fly away.'"
tokens = preprocess_text(text)
# Bigram approach:
bigrams_prepped = ngrams(tokens, 2)
bigrams = Counter(bigrams_prepped)
print("Three most frequent word sequences and the number of occurrences according to Bigrams:")
print(bigrams.most_common(3))
# Bag-of-Words approach:
# Define bag_of_words here:
bag_of_words = Counter(tokens)
print("\nThree most frequent words and number of occurrences according to Bag-of-Words:")
most_common_three = Counter.most_common(bag_of_words,3)
print(most_common_three)
