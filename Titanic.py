# The survival rate is associated to the class of passenger

import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = pd.read_csv("titanic.csv")

# Group the data by Pclass and calculate the mean of Survived for each class
survival_by_class = titanic.groupby('Pclass')['Survived'].mean()

print(survival_by_class)

# bar plot of survival rate by class
plt.bar(survival_by_class.index, survival_by_class.values)
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()
