import requests

colors_url = ''  # TODO we'll share the API URL in the workshop

favorite_color = input('Please enter your favorite color: ')

# Example JSON to send to API server
json_data = {'color': favorite_color}
add_color_response = requests.post(colors_url, json=json_data)
add_color_json = add_color_response.json()

# Optional, information for developers for debugging
print(add_color_response.json())  # Hopefully this will be {"result":"Success - color submitted"}
print(add_color_response.status_code)  # 201

# Print a message for the user
try:
    message = add_color_json.get('result')
    print(message)
except AttributeError:
    print("Error: 'result' key not found in JSON object")
except Exception as e:
    print(f"Error: {e}")

# TODO - error handling


# Get all the favorite colors submitted so far

all_colors_response = requests.get(colors_url)
all_colors_json = all_colors_response.json()

print(all_colors_json)  # For debugging, a list of objects
# For example [{"name":"purple"},{"name":"orange"}]

# Display the names of all the colors to the user
for color in all_colors_json:
    print(color['name'])

# TODO error handling
