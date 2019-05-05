from django.forms import ModelForm,TextInput
from .models import City

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name']
		widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}

	# text = forms.CharField(max_length=25,
	# 	widget =forms.TextInput{
	# 	'class':'input'
	# 	'placeholder':'City Name',
	# 	}
	# )