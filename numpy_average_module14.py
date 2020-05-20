import numpy as np
import pandas as pd
greatest_books = pd.read_csv("top-hundred-books.csv")
author_ages = greatest_books['Ages']
average_age = np.average(author_ages)
print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))
