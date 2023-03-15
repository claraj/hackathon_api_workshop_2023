import requests
from pprint import pprint

bored_url = 'https://www.boredapi.com/api/activity/'

how_much_money = input('How much money do yu have available today? Enter "none", "some" or "lots" ')

if how_much_money == 'none':
    query_parameters = {'price': 0}  # Create query parameter for free activity

elif how_much_money == 'some':
    query_parameters = {'minprice': 0, 'maxprice': 0.1}  # Create query parameters for a range

elif how_much_money == 'lots':
    query_parameters = {'minprice': 0, 'maxprice': 1}
    # If we decide we only want expensive activities, this would be easy to change

else:  # A default option if the user enters something else
    print('Sorry, not a valid input. Requesting a random activity')
    query_parameters = {}   # no query parameters - so the URL will not be changed

activity_response = requests.get(bored_url, params=query_parameters)
activity_json = activity_response.json()
activity_description = activity_json['activity']
activity_price = activity_json['price']
print('Here is your activity: ' + activity_description)

if activity_price == 0:
    print('This activity is free!')
else:
    print('This activity has a relative price on a scale 0-1 of ' + str(activity_price))  # Or, use format string

