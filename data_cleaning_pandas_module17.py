import codecademylib3_seaborn
import pandas as pd
df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")
print(df1.head())
print(df2.head())
clean = 2

import codecademylib3_seaborn
import pandas as pd
import glob
student_files = glob.glob('exams*.csv')
df_list=[]
for exam in student_files:
  data = pd.read_csv(exam)
  df_list.append(data)
students = pd.concat(df_list)
print(students)
print(len(students))

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students.columns)
students = pd.melt(frame=students,id_vars = ['full_name','gender_age','grade'],value_vars = ['fractions','probability'],value_name = 'score',var_name = 'exam')
print(students.head())
print(students.columns)
print(students['exam'].value_counts())

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students)
duplicates = students.duplicated()
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students.columns)
print(students.head())
students['gender']=students.gender_age.str[0]
students['age']=students.gender_age.str[1:]
print(students.head())
print(students[['full_name','grade','exam','score','gender','age']])

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students)
name_split = students.full_name.str.split(' ')
students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)
print(students.head())

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students.head())
print(students.dtypes)
print(students['score'].mean())

import codecademylib3_seaborn
import pandas as pd
from students import students
students.score = students['score'].replace('%','',regex=True)
students.score=pd.to_numeric(students.score)

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students.grade.head())
students.grade = students.grade.str.split('(\d+)', expand=True)[1]
print(students.dtypes)
students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()
print(avg_grade)

import codecademylib3_seaborn
import pandas as pd
from students import students
print(students)
score_mean =students.score.mean()
print(score_mean)
students = students.fillna({'score':0})
score_mean_2 = students.score.mean()
print(score_mean_2)
