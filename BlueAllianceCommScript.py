import requests
import json


year = 2013
complete_match_list = []
def how_many_matches(datain):
    cracked_data = returned_data.split(',')
    for i in cracked_data:
        print(i)
        print()


for year in range(2013, 2019):
    auth = {'X-TBA-Auth-Key': 'Sw8UAmxSFvOgQPblLyvgMCOqzZzm2cCvXdJp1qo1xM8AWHG12WhfUR29MHZW3rLI'}
    id_header = 'frc4469:api_testing_app:v01'
    response = requests.get('https://www.thebluealliance.com/api/v3/team/frc4469/matches/' + str(year), headers = auth)
    returned_data = str(response.content).split('match_number')
    del returned_data[0]
    match_list = [x[3:x.index(',')] for x in returned_data]
    print(year)
    print(match_list)
    complete_match_list.extend(match_list)

print()
print('Matches Played: {}'.format(len(complete_match_list)))
print()


"""
for i in complete_match_list:
    print(i)
    print()


#for key, value in converted_data:
 #   print('Key: {} | Value: {}'.format(key, value))
  #  print()

#how_many_matches(returned_data)
"""