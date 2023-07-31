# restaurant-picker

This microservice searches for the file restaurant_data.json then picks a random **unvisited** restaurant out of that list, and outputs it to random_restaurant.json.

The JSON will contain an array of restaurants. Each restaurant will have the following properties: 
-	name: \<String\>
-	address: \<String\>
-	phone: \<Number\>
-	url: \<String\>
-	list: \<String\>
-	visited: \<Boolean\>

[Full Contract](/files/CS361-Assignment-9-Besher-Al-Maleh.pdf)

[JSON Example](/json-examples/restaurant_data.json)

![Sequence Diagram](/images/Restaurant-Picker.png)