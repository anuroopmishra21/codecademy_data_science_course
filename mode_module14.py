import numpy as np
first_ten_authors = np.array([29, 49, 42, 43, 32, 38, 37, 41, 27, 27])
mode_age = 27
mode_count = 2
print("The ages of the first ten authors is: " + str(first_ten_authors))
print("The mode of the first ten authors is: " + str(mode_age))
print("The number of authors who were " + str(mode_age) + " when their book was published is " + str(mode_count))

import numpy as np
import pandas as pd
from scipy import stats
greatest_books = pd.read_csv("top-hundred-books.csv")
author_ages = greatest_books['Ages']
mode_age = stats.mode(author_ages)
print("The mode age and its frequency of authors from Le Monde's 100 greatest books is: " + str(mode_age[0][0]) + " and " + str(mode_age[1][0]))
