import requests
from pprint import pprint

"""Use the bored API to get any random activity, and print the activity description and price."""

bored_url = 'https://www.boredapi.com/api/activity/'

activity_response = requests.get(bored_url)
activity_json = activity_response.json()
pprint(activity_json)

activity_description = activity_json['activity']
activity_price = activity_json['price']

print(activity_description)
print(activity_price)

if activity_price == 0:
    print('This activity is free!')

