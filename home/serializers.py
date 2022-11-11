
from rest_framework import serializers
from .models import user,appointment,event_benefits

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('id','name', 'city', 'number', 'age')

class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = appointment
       fields = ('name', 'url', 'time','day')


class RoSerializer(serializers.ModelSerializer):
   class Meta:
       model = event_benefits
       fields = ('name', 'url')



































