import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
vein_pack_lifespans = familiar.lifespans(package='vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans,71)
if vein_pack_test.pvalue < 0.05:
  print 'The Vein Pack Is Proven To Make You Live Longer!'
else:
  print 'The Vein Pack Is Probably Good For You Somehow!'
artery_pack_lifespans = familiar.lifespans(package='artery')
package_comparison_results = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
if package_comparison_results < 0.05:
  print 'the Artery Package gaurantees even stronger results!'
else:
  print 'the Artery Package is also a great product!'
iron_contingency_table = familiar.iron_counts_for_package()
tstat,iron_pvalue,ndeg,freq = chi2_contingency(iron_contingency_table)
if iron_pvalue < 0.05:
  print 'The Artery Package Is Proven To Make You Healthier!'
else:
  print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"
