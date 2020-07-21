import numpy as np
p_knows_material = 0.6
p_correct_given_knows_material = 0.85
p_correct = (0.85*0.6)+(0.20*0.40)
p_knows_material_given_correct = (p_correct_given_knows_material * p_knows_material) / p_correct
print(p_knows_material_given_correct)
