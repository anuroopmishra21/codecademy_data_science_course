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

