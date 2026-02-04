# CHPC Summer School 2026
# Probability & Statistics: Categorical Data & Probability
# Example: Jerusalema

#%%
# Import packages and functions

import numpy as np
from scipy.stats import chi2_contingency

#%%
# Give the contingency table with observed counts			

ctJerusalema = np.array([[28, 12], [16, 24]])

#%%
# Do the test for independence

chi2_statistic, p_value, degrees_of_freedom, expected_frequencies = chi2_contingency(ctJerusalema)

#%%
# Print the results

print("Pearson's chi-square test for independence")
print(f"Observed frequencies: \n{ctJerusalema}")
print(f"Expected frequencies: \n{expected_frequencies}")
print(f"Chi-square statistic: {chi2_statistic:.5f}") 
print(f"p-value:              {p_value:.5f}")
print(f"Degrees of freedom:   {degrees_of_freedom}")
