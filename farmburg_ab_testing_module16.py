import codecademylib
import pandas as pd
df = pd.read_csv('clicks.csv')
print df.head()

import codecademylib
import pandas as pd
df = pd.read_csv('clicks.csv')
df['is_purchase'] = df.click_day.apply(lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase')
purchase_counts = df.groupby(['group','is_purchase']).user_id.count().reset_index()
print purchase_counts

from scipy.stats import chi2_contingency
contingency = [[316, 1350],
           [183, 1483],
           [83, 1583]]
stat, pval, dof, expected = chi2_contingency(contingency)
print pvalue
is_significant = True

import codecademylib
import pandas as pd
from scipy.stats import binom_test
df = pd.read_csv('clicks.csv')
num_visits = len(df)
p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits
pvalueA = binom_test(316,1350+316,p_clicks_099)
pvalueB = binom_test(183,1483+183,p_clicks_199)
pvalueC = binom_test(83,1586+83,p_clicks_499)
print pvalueA,pvalueB,pvalueC
final_answer = 4.99
