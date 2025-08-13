import geocoder
import webbrowser

def track_and_open_location():
    try:
        # Get the location based on IP
        g = geocoder.ip('me')
        if g.ok:
            lat, lng = g.latlng
            print(f"Current Location: Latitude = {lat}, Longitude = {lng}")
            
            # Open Google Maps with the location
            url = f"https://www.google.com/maps?q={lat},{lng}"
            webbrowser.open(url)
        else:
            print("Unable to retrieve location.")
    except Exception as e:
        print(f"Could not get location: {e}")

# Call the function
track_and_open_location()
