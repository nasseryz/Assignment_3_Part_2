
import pandas as pd
import matplotlib.pyplot as plt

## The survival rate is associated to the class of passenger

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

## the survival rate is associated to the gender
survival_by_gender = titanic.groupby('Sex')['Survived'].mean()
print(survival_by_gender)

# bar plot to visualize the survival rate by gender
plt.bar(survival_by_gender.index, survival_by_gender.values)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.show()

## the survival rate is associated to the age

# create age groups
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
titanic['AgeGroup'] = pd.cut(titanic['Age'], bins=age_bins, labels=age_labels)

# calculate survival rate for each age group
age_grouped = titanic.groupby(['AgeGroup'])['Survived'].mean()

# plot the survival rate for each age group
plt.bar(age_labels, age_grouped)
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Age Group')
plt.show()
