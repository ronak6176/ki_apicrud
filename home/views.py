from urllib import response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from home.serializers import PersonSerializer,SpeciesSerializer,RoSerializer
from home.models  import user
from home.models  import appointment,event_benefits
from rest_framework import status
from django.shortcuts import render
import pyrebase


# {
#         "id": 4,
#         "name": "ronak",
#         "city": "rajkot",
#         "number": "232232323",
#         "age": "12"
#     }
    
# config={
# 	"apiKey": "AIzaSyDwDQEJL4pbWPwmBJJ3pY0lvLqEa1NkWJw",
# 	"authDomain": "kivy-api.firebaseapp.com",
# 	"databaseURL": "https://kivy-api-default-rtdb.firebaseio.com",
#   	"projectId": "kivy-api",
#   	"storageBucket": "kivy-api.appspot.com",
#   	"messagingSenderId": "1001736236107",
#   	"appId": "1:1001736236107:web:f4372b2285be4b105031ce",
  
# }
# firebase=pyrebase.initialize_app(config)
# auth=firebase.auth()
# database=firebase.database()

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/all/user',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create/user',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer     

# {
#         "id": 4,
#         "name": "ronak",
#         "city": "rajkot",
#         "number": "232232323",
#         "age": "12"
#     }


@api_view(['POST'])
def add_items(request):
	item = PersonSerializer(data=request.data)


	if user.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer 



@api_view(['GET'])
def view_items(request):
    if request.method == 'GET':
        tutorials = user.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = PersonSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

@api_view(['POST'])
def update_items(request, pk):
	item = user.objects.get(pk=pk)
	data = PersonSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(user, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)



# **********************************************appointment*******************************************************

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/all/user',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create/user',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer     

# {
#         "id": 4,
#         "name": "ronak",
#         "city": "rajkot",
#         "number": "232232323",
#         "age": "12"
#     }


@api_view(['POST'])
def add_items(request):
	item = SpeciesSerializer(data=request.data)


	if appointment.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer 



@api_view(['GET'])
def view_items(request):
    if request.method == 'GET':
        tutorials = appointment.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = SpeciesSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

@api_view(['POST'])
def update_items(request, pk):
	item = appointment.objects.get(pk=pk)
	data = SpeciesSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(appointment, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)


# **********************************************event_benefits*******************************************************


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/all/user',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create/user',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer     

# {
#         "id": 4,
#         "name": "ronak",
#         "city": "rajkot",
#         "number": "232232323",
#         "age": "12"
#     }


@api_view(['POST'])
def add_items(request):
	item = RoSerializer(data=request.data)


	if event_benefits.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = user.objects.all()
#    serializer_class = PersonSerializer 



@api_view(['GET'])
def view_items(request):
    if request.method == 'GET':
        tutorials = event_benefits.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = RoSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
		# return Response(status=status.HTTP_404_NOT_FOUND)


        

@api_view(['POST'])
def update_items(request, pk):
	item = event_benefits.objects.get(pk=pk)
	data = RoSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(event_benefits, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)



















