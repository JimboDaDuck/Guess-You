import subprocess
import requests

try:
    import pycountry
except ImportError:
    subprocess.check_call(['pip', 'install', "pycountry"])
    import pycountry

Genderize = "https://api.genderize.io"
Agify = "https://api.agify.io"
Nationalize = "https://api.nationalize.io"

name = input("Enter your name: ")
params = {"name": name}

genderResponse = requests.get(Genderize, params=params)

if genderResponse.status_code == 200:
    print(f"Gender: {genderResponse.json()['gender']}")
else:
    print(f"Failed to retrieve gender data. Status code: {genderResponse.status_code}")

ageResponse = requests.get(Agify, params=params)

if ageResponse.status_code == 200:
    print(f"Age: {ageResponse.json()['age']}")
else:
    print(f"Failed to retrieve age data. Status code: {ageResponse.status_code}")

nationalityResponse = requests.get(Nationalize, params=params)

if nationalityResponse.status_code == 200:
    countries = nationalityResponse.json()['country']
    highest_prob_country = max(countries, key=lambda x: x['probability'])
    country_name = pycountry.countries.get(alpha_2=highest_prob_country['country_id']).name
    
    if country_name:
        print(f"Nationality: {country_name} (Probability: {highest_prob_country['probability']})")
    else:
        print(f"Nationality: {highest_prob_country['country_id']} (Probability: {highest_prob_country['probability']})")
else:
    print(f"Failed to retrieve nationality data. Status code: {nationalityResponse.status_code}")

input("Enter Anything To Exit: ")
