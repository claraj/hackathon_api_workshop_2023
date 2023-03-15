import requests
from pprint import pprint

def main():
    bored_url = 'https://www.boredapi.com/api/activity/'

    how_much_money = input('How much money do you have available today? Enter "none", "some" or "lots" ')

    if how_much_money == 'none':
        query_parameters = {'price': 0}  # Create query parameter for free activity

    elif how_much_money == 'some':
        min_price = number_input('What is the minimum relative price (between 0 and 1)? ')
        max_price = number_input('What is the maximum relative price (between 0 and 1)? ')
        query_parameters = {'minprice': min_price, 'maxprice': max_price}  # Create query parameters for a range

    elif how_much_money == 'lots':
        query_parameters = {'minprice': 0, 'maxprice': 1}
        # If we decide we only want expensive activities, this would be easy to change

    else:  # A default option if the user enters something else
        print('Sorry, not a valid input. Requesting a random activity')
        query_parameters = {}   # no query parameters - so the URL will not be changed

    try:
        activity_response = requests.get(bored_url, params=query_parameters)
        activity_json = activity_response.json()

        # does the response contain data, or an error message?
        error = activity_json.get('error')

        if error:
            print('Sorry, cannot fetch an activity because ' + error)

        else:
            activity_description = activity_json.get('activity')
            activity_price = activity_json.get('price')

            print('Here is your activity: ' + activity_description)

            if activity_price == 0:
                print('This activity is free!')
            else:
                print('This activity has a relative price on a scale 0-1 of ' + str(activity_price))  # Or, use format string

    except Exception as e:
        print('Sorry, something went wrong fetching your activity. '
              'Are you connected to the internet? If you are, please try again later.')
        print('Here is some information for developers: ', e)


def number_input(question):
    while True:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print('Please enter a number')


main()
