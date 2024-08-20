from django.shortcuts import render
import json 
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c863366c3cca06281d4c874a2b46c392').read()
        json_data = json.loads(res)
        
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',  # Note: Temperature should be in Kelvin
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

        return render(request, 'index.html', {'data': data})  # Pass the data to the template

    else:
        data = {}
    
    return render(request, 'index.html', data)  # Return an empty data dictionary if no POST request
