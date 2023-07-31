import os
import json
import time
import random

# we're waiting for the expected file to appear
print("Waiting for file 'restaurant_data.json'...")
while not os.path.exists('restaurant_data.json'):
    time.sleep(1)

print("Found restaurant_data.json! processing...")
# We have a file! let's read & process it
with open('restaurant_data.json', 'r') as f:
    data = json.load(f)

# remove all the visited restaurants
unvisited = [restaurant for restaurant in data if not restaurant['visited']]

if unvisited:
    # now pick a random unvisited restaurant
    random_restaurant = random.choice(unvisited)
    

    # write the details to a new file
    with open('random_restaurant.json', 'w') as f:
        json.dump(random_restaurant, f)
    
    print(f"We picked a random restaurant and wrote it to random_restaurant.json")
    
else:
    print("No unvisited restaurants found in the data!")

# clean-up
os.remove('restaurant_data.json')
