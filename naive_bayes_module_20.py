from reviews import neg_list, pos_list, neg_counter, pos_counter
print(pos_list[0])
print(neg_list[0])
print(pos_counter['no'])

from reviews import neg_counter, pos_counter
review = "This crib was amazing"
percent_pos = 0.5
percent_neg = 0.5
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())
pos_probability = 1
neg_probability = 1
review_words = review.split()
for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  pos_probability *= word_in_pos / total_pos
  neg_probability *= word_in_neg / total_neg

from reviews import neg_counter, pos_counter
review = "This cribb was amazing"
percent_pos = 0.5
percent_neg = 0.5
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())
pos_probability = 1
neg_probability = 1
review_words = review.split()
for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  pos_probability *= (word_in_pos+1) / (total_pos+len(pos_counter))
  neg_probability *= (word_in_neg+1) / (total_neg+len(neg_counter))
print(pos_probability)
print(neg_probability)

from reviews import neg_counter, pos_counter
review = "The product is terrible"
percent_pos = 0.5
percent_neg = 0.5
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())
pos_probability = 1
neg_probability = 1
review_words = review.split()
for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))
final_pos = pos_probability * percent_pos
final_neg = neg_probability * percent_neg
print(final_pos)
print(final_neg)
if final_pos > final_neg:
  print("The review is positive")
else:
  print("The review is negative")

from reviews import neg_list, pos_list
from sklearn.feature_extraction.text import CountVectorizer
review = "This crib was amazing"
counter = CountVectorizer()
counter.fit(neg_list + pos_list)
print(counter.vocabulary_)
review_counts = counter.transform([review])
training_counts = counter.transform(neg_list + pos_list)
print(review_counts.toarray())

from reviews import counter, training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
review = "This crib was great terrific amazing and wonderful"
review_counts = counter.transform([review])
classifier = MultinomialNB()
training_labels = [0]*1000 + [1]*1000
classifier.fit(training_counts, training_labels)
print(classifier.predict(review_counts))
print(classifier.predict_proba(review_counts))
