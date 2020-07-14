labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guesses)):
  if labels[i]==1 and guesses[i]==1:
    true_positives +=1
  if labels[i]==0 and guesses[i]==0:
    true_negatives +=1
  if labels[i]==0 and guesses[i]==1:
    false_positives +=1
  if labels[i]==1 and guesses[i]==0:
    false_negatives +=1
accuracy = (true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)
print(accuracy)

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guesses)):
  if labels[i] == 1 and guesses[i] == 1:
    true_positives += 1
  if labels[i] == 0 and guesses[i] == 0:
    true_negatives += 1
  if labels[i] == 0 and guesses[i] == 1:
    false_positives += 1
  if labels[i] == 1 and guesses[i] == 0:
    false_negatives += 1  
accuracy = (true_positives + true_negatives) / len(guesses)
print(accuracy)
recall = true_positives/(true_positives+false_negatives)
print(recall)

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guesses)):
  if labels[i] == 1 and guesses[i] == 1:
    true_positives += 1
  if labels[i] == 0 and guesses[i] == 0:
    true_negatives += 1
  if labels[i] == 0 and guesses[i] == 1:
    false_positives += 1
  if labels[i] == 1 and guesses[i] == 0:
    false_negatives += 1
accuracy = (true_positives + true_negatives) / len(guesses)
print(accuracy)
recall = true_positives / (true_positives + false_negatives)
print(recall)
precision = true_positives / (true_positives+false_positives)
print(precision)

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
for i in range(len(guesses)):
  if labels[i] == 1 and guesses[i] == 1:
    true_positives += 1
  if labels[i] == 0 and guesses[i] == 0:
    true_negatives += 1
  if labels[i] == 0 and guesses[i] == 1:
    false_positives += 1
  if labels[i] == 1 and guesses[i] == 0:
    false_negatives += 1
accuracy = (true_positives + true_negatives) / len(guesses)
print(accuracy)
recall = true_positives / (true_positives + false_negatives)
print(recall)
precision = true_positives / (true_positives + false_positives)
print(precision)
f_1 = 2*((precision*recall)/(precision+recall))
print(f_1)

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
print(accuracy_score(labels,guesses))
print(recall_score(labels,guesses))
print(precision_score(labels,guesses))
print(f1_score(labels,guesses))
