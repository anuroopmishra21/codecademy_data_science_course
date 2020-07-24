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
