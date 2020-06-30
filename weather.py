import requests

# this is a sample request 
def climate(lat, lon):
    url = "https://api.climacell.co/v3/weather/realtime"
    payload = {
        "apikey": "HPbxRKzxd5rG6poQFZ9os9dSjcszBge2",
        "lat":lat, 
        "lon":lon,
        "fields": ["temp", "precipitation", "wind_gust"],
        "unit_system":"us", 

   }

    response = requests.get(url, params=payload).json()

    print(response)

# If you want to use classes
# class Place:
# would have attributes lat, long, name,
# Would be like a card in blackjack and the place_list would be like a deck

# class WeatherReport
# place, temp, precip


locations = [(48.8566, 2.3522), (41.9028, 12.4964), (41.8695, 87.6511), (33.4484, 112.0740), (40.7128, 74.0060), (45.5051, 122.6750), (47.6062, 122.3321), (39.7392, 104.9903), (51.5074, 0.1278), (52.2297, 21.0122)]
#TODO construct a list of places that are tuples lat and long
#(lat, long)
# you can use [] to retrieve items by position, like you can in list
# ex. (lat, long)[0] = lat


for location in locations:
    climate(location[0],location[1])

  # get lats and longs from tuples
  # give me temp and precip for a location, given lat and long
  # it will make a request to the 'realtime' url that we used below
  

# locations = (48.8566, 2.3522, 41.9028, 12.4964, 41.8695, 87.6511, 33.4484, 112.0740, 40.7128, 74.0060, 45.5051, 122.6750, 47.6062, 122.3321, 39.7392, 104.9903, 51.5074, 0.1278, 52.2297, 21.0122)