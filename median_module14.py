import numpy as nps
five_author_ages = np.array([29, 49, 42, 43, 32])
sorted_author_ages = np.array([29, 32, 42, 43, 49])
median_age = 42
print("The sorted array is: " + str(sorted_author_ages))
print("The median of the array is: " + str(median_age))

import numpy as np
import pandas as pd
greatest_books = pd.read_csv("top-hundred-books.csv")
author_ages = greatest_books['Ages']
median_age = np.median(author_ages)
print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))
