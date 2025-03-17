import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Problem 2 Part A)
data = pd.read_csv("CustomerProfiles_Q2.csv")
data.columns = ['Average Monthly Spending', 'Total Purchases']

plt.figure(figsize = (10, 6))
plt.scatter(data['Average Monthly Spending'], data['Total Purchases'], color = 'blue', alpha = 0.7, edgecolors = 'black', s = 100)
plt.xlabel('Feature 1: Average Monthly Spending', fontsize = 12)
plt.ylabel('Feature 2: Total Purchases', fontsize = 12)
plt.title('Customer Distribution Based on Spending and Purchase Frequency', fontsize = 14)

plt.grid(True, linestyle = '--', alpha = 0.7)
plt.tight_layout()
plt.show()
