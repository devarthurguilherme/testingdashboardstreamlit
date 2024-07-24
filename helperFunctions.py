from datetime import datetime


# Age Function
def calculateAge(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
