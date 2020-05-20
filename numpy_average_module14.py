import numpy as np
import pandas as pd
greatest_books = pd.read_csv("top-hundred-books.csv")
author_ages = greatest_books['Ages']
average_age = np.average(author_ages)
print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))

import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
greatest_books = pd.read_csv("top-hundred-books.csv")
author_ages = greatest_books['Ages']
average_age = np.average(author_ages)
print("The average age of the 100 greatest authors, according to Le Monde is: " + str(average_age))
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.legend()
plt.show()
