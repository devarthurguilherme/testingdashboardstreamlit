from datetime import datetime
import csv
import json

# Age Function


def calculateAge(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# # Lê o arquivo CSV
# df = pd.read_csv('myData/drivers.csv')

# # Converte o DataFrame para JSON
# df.to_json('myData/drivers.json', orient='records', lines=False)
