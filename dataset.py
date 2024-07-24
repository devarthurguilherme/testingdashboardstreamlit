import pandas as pd
from helperFunctions import calculateAge
import json

# Test
# file = open('myData/myVendas.json')
# data = json.load(file)

# df = pd.DataFrame.from_dict(data)
# # print(df)
# file.close()

file2 = open('myData/drivers.json')
data2 = json.load(file2)

dfDrivers = pd.DataFrame.from_dict(data2)
# print(dfDrivers)
file2.close()


# Filter
# Complete Name
dfDrivers['full_name'] = dfDrivers['forename'] + ' ' + dfDrivers['surname']
# print(dfDrivers['full_name'])

# Convert 'dob' to datetime
dfDrivers['dob'] = pd.to_datetime(dfDrivers['dob'])


# Just Pilots Since 1970
limiteDate = pd.to_datetime('1970-01-01')

# Create Column and Filter Since 1970
dfDrivers['since_70s'] = dfDrivers['dob'] >= limiteDate
# print(len(dfDrivers['since_70s']))


# Apply Age Function
dfDrivers['age'] = dfDrivers['dob'].apply(calculateAge)
# print(dfDrivers['age'])
newDfDrivers = dfDrivers[['full_name', 'age', 'since_70s', 'nationality']]

since1970NewDfDrivers = newDfDrivers[newDfDrivers['since_70s']]
since1970NewDfDrivers = since1970NewDfDrivers[
    ['full_name', 'age', 'nationality']]

since1970NewDfDrivers_reset = since1970NewDfDrivers.reset_index(drop=True)
since1970NewDfDrivers_reset

# # Create a new Dataframa with selected columns
# newDfDrivers = dfDrivers[['full_name', 'age', 'nationality']]

# bins = [0, 18, 30, 40, 50, 60, 100]  # Limites das faixas etárias
# labels = ['0-17', '18-29', '30-39', '40-49',
#           '50-59', '60+']  # Rótulos para as faixas
