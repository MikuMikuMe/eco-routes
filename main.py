Creating a Python program to optimize vehicle navigation for eco-routes requires various components, such as obtaining real-time traffic and environmental data, calculating optimal routes, and potentially interfacing with a mapping service. While a complete implementation would require access to specific APIs (for traffic data, maps, and so forth), I'll provide a basic structure to get you started. This code will include comments and error handling but note that you will need to add your own API keys and any additional logic based on the APIs you choose to use.

Below is an example program structure using hypothetical functions:

```python
import requests

# Constants for the mapping and traffic data services
MAPS_API_URL = "https://maps.example.com/routing"
TRAFFIC_API_URL = "https://traffic.example.com/data"
ENVIRONMENT_API_URL = "https://environment.example.com/emissions"
API_KEY = 'your_api_key_here'  # Replace with your actual API key

def get_traffic_data(origin, destination):
    """
    Fetch real-time traffic data from the traffic API.
    """
    try:
        # Construct the request URL for the traffic data
        params = {
            'origin': origin,
            'destination': destination,
            'key': API_KEY
        }
        response = requests.get(TRAFFIC_API_URL, params=params)
        response.raise_for_status()
        traffic_data = response.json()
        return traffic_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching traffic data: {e}")
        return None

def get_environmental_data(route):
    """
    Fetch environmental data related to emissions for the given route.
    """
    try:
        # Construct the request URL for the environmental data
        params = {
            'route': route,
            'key': API_KEY
        }
        response = requests.get(ENVIRONMENT_API_URL, params=params)
        response.raise_for_status()
        environmental_data = response.json()
        return environmental_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching environmental data: {e}")
        return None

def calculate_eco_route(origin, destination):
    """
    Calculate the optimal eco-route from origin to destination.
    """
    traffic_data = get_traffic_data(origin, destination)
    if not traffic_data:
        print("Unable to retrieve traffic data. Returning default route.")
        return None

    possible_routes = traffic_data.get('routes', [])
    best_route = None
    lowest_emissions = float('inf')

    for route in possible_routes:
        environmental_data = get_environmental_data(route)
        if not environmental_data:
            continue
        
        emissions = environmental_data.get('emissions', float('inf'))
        if emissions < lowest_emissions:
            lowest_emissions = emissions
            best_route = route

    return best_route

def main():
    # Example origin and destination coordinates
    origin = "12.9715987,77.594566"  # Bangalore
    destination = "28.6139391,77.2090212"  # Delhi

    print(f"Calculating eco-route from {origin} to {destination}...")
    eco_route = calculate_eco_route(origin, destination)
    
    if eco_route is not None:
        print("Eco-route calculated successfully:")
        print(eco_route)
    else:
        print("Failed to calculate eco-route.")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **API Interaction**: The example uses `requests` to interact with two fictional APIs, one for traffic data and another for environmental data.
   
2. **Error Handling**: The `try-except` block ensures that network-related errors are caught and reported without crashing the program.

3. **Environmental and Traffic Data Usage**: The program first gets real-time traffic data, then iterates over potential routes to find the one with the lowest emissions, using environmental data to decide.

4. **Main Function**: The `main` function simulates the entire process, initiating a request for eco-route calculation.

5. **Placeholder and Simplification**: The API endpoints, parameters, and keys are placeholders and need to be updated to match actual services. The logic for determining the best route is also simplified, as a full implementation would rely on more extensive data analysis and criteria.

In practice, you might use Google Maps, Mapbox, or other similar APIs for real-time and routing data, possibly supplemented by specialized emission estimation APIs or models.