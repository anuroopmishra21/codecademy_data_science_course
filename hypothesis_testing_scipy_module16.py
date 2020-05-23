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
