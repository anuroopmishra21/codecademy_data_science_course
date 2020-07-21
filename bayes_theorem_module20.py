third_child = "independent"

import numpy as np
p_rain_and_gym = 0.30 * 0.60

import numpy as np
p_disease_and_correct = 0.00001 * 0.99
p_no_disease_and_incorrect = 0.99999 * 0.01
print(p_disease_and_correct)
print(p_no_disease_and_incorrect)

import numpy as np
p_positive_given_disease = 0.99
p_disease = 0.00001
p_positive = (0.00001 * 0.99) + (0.01 * 0.99999)
p_disease_given_positive = (p_positive_given_disease * p_disease) / (p_positive)
print(p_disease_given_positive)

import numpy as np
a = "spam"
b = "enhancement"
p_spam = 0.20
p_enhancement_given_spam = 0.05
p_enhancement = (0.05*0.2)+(0.001*0.8)
p_spam_enhancement = (p_enhancement_given_spam*p_spam)/p_enhancement
print(p_spam_enhancement)
