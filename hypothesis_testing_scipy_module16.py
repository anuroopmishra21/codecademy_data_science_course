from scipy.stats import ttest_1samp
import numpy as np
ages = np.genfromtxt("ages.csv")
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tstat , pval = ttest_1samp(ages,30)
print(pval)

from scipy.stats import ttest_1samp
import numpy as np
correct_results = 0 # Start the counter at 0
daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")
for i in range(1000): # 1000 experiments
   #your ttest here:
   tstat, pval = ttest_1samp(daily_visitors[i],30)
   #print the pvalue here:
   print pval
   if pval < 0.05:
     correct_results +=1
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."

from scipy.stats import ttest_ind
import numpy as np
week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
print week1_mean,week2_mean
week1_std = np.std(week1)
week2_std = np.std(week2)
print week1_std,week2_std
tstat, pval = ttest_ind(week1,week2)
print(pval)

from scipy.stats import ttest_ind
import numpy as np
a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)
print a_mean,b_mean,c_mean
print a_std,b_std,c_std
abtstat,a_b_pval = ttest_ind(a,b)
actstat,a_c_pval = ttest_ind(a,c)
bcstat,b_c_pval = ttest_ind(b,c)
print a_b_pval,a_c_pval,b_c_pval
error_prob = (1-0.95**3)
print error_prob

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np
a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b_new.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
tstat,pval = f_oneway(a,b,c)
print pval

import codecademylib
import numpy as np
import matplotlib.pyplot as plt
dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")
dist_3 = np.genfromtxt("3.csv",  delimiter=",")
dist_4 = np.genfromtxt("4.csv",  delimiter=",")
#plot your histogram here
plt.hist(dist_1)
plt.show()
plt.close('all')
plt.hist(dist_2)
plt.show()
plt.close('all')
plt.hist(dist_3)
plt.show()
plt.close('all')
plt.hist(dist_4)
plt.show()
not_normal = 4
ratio = (np.std(dist_2))/(np.std(dist_3))
print(ratio)

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import numpy as np
a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
stat, pval = f_oneway(a, b, c)
print pval
# Using our data from ANOVA, we create v and l
v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)
tukey_results = pairwise_tukeyhsd(v,labels,0.05)
print tukey_results

from scipy.stats import binom_test
pval = binom_test(510, n=10000, p=0.06)
print pval
pval2 = binom_test(590, n=10000, p=0.06)
print pval2

from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20,20]]
chi2, pval, dof, expected = chi2_contingency(X)
print pval
