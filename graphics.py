from dataset import *

# Create column with Age Group
newDfDrivers['ageGroup'] = pd.cut(
    newDfDrivers['age'], bins=bins, labels=labels, right=False)
newDfDrivers['ageGroup'] = pd.cut(
    newDfDrivers['age'], bins=bins, labels=labels, right=False)

ageGroupCounts = newDfDrivers.groupby('ageGroup').size()
