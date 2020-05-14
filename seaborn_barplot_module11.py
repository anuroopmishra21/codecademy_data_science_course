import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df=pd.read_csv('results.csv')
print(df)
sns.barplot(data = df,x='Gender',y='Mean Satisfaction')
plt.show()

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
assignment1=gradebook[gradebook.assignment_name=='Assignment 1']
print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
gradebook = pd.read_csv("gradebook.csv")
sns.barplot(data=gradebook,x='assignment_name',y='grade')
plt.show()

import codecademylib3_seaborn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns
gradebook = pd.read_csv("gradebook.csv")
sns.barplot(data=gradebook, x="name", y="grade",ci='sd')
plt.show()

import codecademylib3_seaborn
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv("survey.csv")
print(df)
sns.barplot(data=df,x='Gender',y='Response',estimator=np.median)
plt.show()

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv("survey.csv")
sns.barplot(data=df,x='Age Range',y='Response',hue='Gender')
plt.show()
