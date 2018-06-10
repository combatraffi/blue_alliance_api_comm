import requests
import json

auth = {'X-TBA-Auth-Key': 'Sw8UAmxSFvOgQPblLyvgMCOqzZzm2cCvXdJp1qo1xM8AWHG12WhfUR29MHZW3rLI'}
id_header = 'frc4469:api_testing_app:v01'
response = requests.get('https://www.thebluealliance.com/api/v3/team/frc4469/matches/2018', headers = auth)
print(response.content)
