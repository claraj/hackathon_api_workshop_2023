import requests
from pprint import pprint

# The base URL for the business search endpoint
url = "https://api.yelp.com/v3/businesses/search"

# The user could be allowed to change this
price_category = 1

# Easier to see and modify as a dictionary vs. a long URL
query_parameters = {
    "location": "Minneapolis",
    "term": "Restaurants",
    "price": price_category,
    "sort_by": "best_match",
    "limit": 20
}

headers = {
    "accept": "application/json",
    "Authorization": "Bearer VbisR32cjrHVH23534edftgkLHxDzlcSZHYx"  # TODO replace this with your own key
}

response = requests.get(url, params=query_parameters, headers=headers)
response_json = response.json()

pprint(response_json)   # Useful for developers, but not customers

businesses = response_json['businesses']  # A list

print(f'Restaurants in price category {price_category} are:')

for restaurant in businesses:
    name = restaurant['name']
    location = restaurant['location']
    address = location['display_address']
    formatted_address = ', '.join(address)
    print(f'{name} at {formatted_address}')

# TODO error handling
