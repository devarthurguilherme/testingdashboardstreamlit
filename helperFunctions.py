from datetime import datetime
import csv
import json

# Age Function


def calculateAge(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Lê o arquivo CSV
with open('myData/drivers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Converte e escreve o arquivo JSON
with open('myData/drivers.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)
