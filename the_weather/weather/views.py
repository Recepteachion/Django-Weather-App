import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=d9c78dff8533149c45f7b8cf6985bfef'
	city = 'İzmir'

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	
	cities = City.objects.all()
	weather_data = []
	form = CityForm()
	for city in cities:	
		r = requests.get(url.format(city)).json()	
		city_weather = {
			'city':city.name,
			'tempreture':r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon':r['weather'][0]['icon'], 

		}
		weather_data.append(city_weather)
	
	
	context = {'weather_data':weather_data,'form':form}
	return render(request,'weather/weather.html',context)