import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print rottweiler_tl
print np.std(rottweiler_tl)
print np.mean(rottweiler_tl)
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
pval = binom_test(num_whippet_rescues,num_whippets,0.08)
print pval
whippets_weight = fetchmaker.get_weight('whippet')
terriers_weight = fetchmaker.get_weight('terrier')
pitbulls_weight = fetchmaker.get_weight('pitbull')
tstat,pval_wt = f_oneway(whippets_weight,terriers_weight,pitbulls_weight)
print pval_wt
v = np.concatenate([whippets_weight,terriers_weight,pitbulls_weight])
labels = ['whippet']*len(whippets_weight) + ['terrier']*len(terriers_weight) + ['pitbull']*len(pitbulls_weight)
tukey_results = pairwise_tukeyhsd(v,labels,0.05)
print tukey_results
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
color_table = [
  [np.count_nonzero(poodle_colors=='black'),np.count_nonzero(shihtzu_colors=='black')],
  [np.count_nonzero(poodle_colors=='brown'),np.count_nonzero(shihtzu_colors=='brown')],
  [np.count_nonzero(poodle_colors=='gold'),np.count_nonzero(shihtzu_colors=='gold')],
  [np.count_nonzero(poodle_colors=='grey'),np.count_nonzero(shihtzu_colors=='grey')],
  [np.count_nonzero(poodle_colors=='white'),np.count_nonzero(shihtzu_colors=='white')]]
chi2,pval,dof,expected = chi2_contingency(color_table)
print pval
