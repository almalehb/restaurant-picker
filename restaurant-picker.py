import os
import json
import time
import random

while True:
    # we're waiting for the expected file to appear
    print("Waiting for file 'restaurant_microservice.json'...")
    while not os.path.exists('restaurant_microservice.json'):
        time.sleep(1)

    print("Found restaurant_microservice.json! processing...")
    # We have a file! let's read & process it
    with open('restaurant_microservice.json', 'r') as f:
        data = json.load(f)

    # the last element of the JSON array determines if we include new restaurant
    newRestaurantOnly = data.pop(); #.pop() removes the last element and returns it
    print('new restaurant only?:', newRestaurantOnly)

    #if new restaurant only, remove all visited restaurant, else the list to random is just the whole list of data
    if newRestaurantOnly == "true":
        # remove all the visited restaurants
        unvisited = [restaurant for restaurant in data if not restaurant['visited']]
    else:
        unvisited = data

    if unvisited:
        # now pick a random unvisited restaurant
        random_restaurant = random.choice(unvisited)

        # write the details to a new file
        with open('random_restaurant.json', 'w') as f:
            json.dump(random_restaurant, f)

        print(f"We picked a random restaurant", random_restaurant["name"], "and wrote it to random_restaurant.json")

    else:
        # make random_restaurant's attributes all false
        random_restaurant = {"name": "No more places to visit!", "address": "", "phone": False, "url": False, "list": False, "visited": False}

        # write the details to a new file
        with open('random_restaurant.json', 'w') as f:
            json.dump(random_restaurant, f)

        print("No unvisited restaurants found in the data!")

    time.sleep(5)
    # clean-up
    os.remove('restaurant_microservice.json')
    print("Removed restaurant_microservice.json")
