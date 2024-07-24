import pandas as pd
# from helperFunctions import calculateAge
import json

file = open('myData/myVendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)
print(df)
file.close()

# csvFilePath = ".\myData\drivers.csv"


# import dataframe
# dfDrivers = pd.read_csv(csvFilePath)

# test
# file = open(
#     'myData\myVendas.json')
# data = json.load(file)

# df = pd.DataFrame.from_dict(data)

# # Format Data
# df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

# # print(df)
# file.close()

# csvFilePath = ".\myData\drivers.csv"

# # import dataframe
# dfDrivers = pd.read_csv(csvFilePath)

# # Filter
# # Complete Name
# dfDrivers['full_name'] = dfDrivers['forename'] + ' ' + dfDrivers['surname']

# # Convert 'dob' to datetime
# dfDrivers['dob'] = pd.to_datetime(dfDrivers['dob'])


# # Apply Age Function
# dfDrivers['age'] = dfDrivers['dob'].apply(calculateAge)

# # Create a new Dataframa with selected columns
# newDfDrivers = dfDrivers[['full_name', 'age', 'nationality']]

# bins = [0, 18, 30, 40, 50, 60, 100]  # Limites das faixas etárias
# labels = ['0-17', '18-29', '30-39', '40-49',
#           '50-59', '60+']  # Rótulos para as faixas
