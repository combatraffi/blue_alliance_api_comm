import requests
import json

def how_many_matches(datain):
    cracked_data = returned_data.split(',')
    for i in cracked_data:
        print(i)
        print()

auth = {'X-TBA-Auth-Key': 'Sw8UAmxSFvOgQPblLyvgMCOqzZzm2cCvXdJp1qo1xM8AWHG12WhfUR29MHZW3rLI'}
id_header = 'frc4469:api_testing_app:v01'
response = requests.get('https://www.thebluealliance.com/api/v3/team/frc4469/matches/2018', headers = auth)
returned_data = str(response.content).split('match_number')
del returned_data[0]
match_list = [x[3:x.index(',')] for x in returned_data]

print()
print('Matches Played: {}'.format(len(match_list)))
print()

for i in match_list:
    print(i)
    print()


#for key, value in converted_data:
 #   print('Key: {} | Value: {}'.format(key, value))
  #  print()

#how_many_matches(returned_data)
