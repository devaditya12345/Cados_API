from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import AdvocateSerializer,CompanySerializer
from django.db.models import Q 

# Create your views here.
#Richardson Matuarity Model bhi dekh lena

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','/advocates/:username']
    # return JsonResponse(data,safe=False)
    return Response(data)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated]) #Abhi ye Authenticate ho gya hai,so Without Token Acces Denied hojaega iss view ke liye
def advocate_list(request):
    # data = ['Dennis','Tadas','Max']
    #TO MAKE THE OBJECT SEARCHABLE
    #http://127.0.0.1:8000/advocates?query=dennis (Query is look like this)

    if request.method == 'GET' : 
        query = request.GET.get('query')

        if query is None :
            query = ''

        # advocates = Advocate.objects.all()
        # advocates = Advocate.objects.filter(username__icontains = query)
        advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates,many=True) #many = True ,means serializing multiple objects at once.
        return Response(serializer.data) #serializer.data --> serializer is a class instance & we have to ruturn serialized data in response
    
    if request.method == 'POST' : # POST FORM ME HMM JO LIKHTE HAI,WO JSON OBJECT HOTA HAI
        
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate,many=False) #many = True ,means serializing multiple objects at once.
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def advocate_detail(request,username):
    # data = username
    advocate = Advocate.objects.get(username = username)

    if request.method == "GET" :

        # advocate = Advocate.objects.get(username = username)
        serializer = AdvocateSerializer(advocate,many=False) #many=False --> Serialize only one object not the list of object
        return Response(serializer.data) 
    
    if request.method == "PUT" :
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']

        advocate.save()

        serializer = AdvocateSerializer(advocate,many=False) #many=False --> Serialize only one object not the list of object
        return Response(serializer.data) 
    
    if request.method == "DELETE" :
        advocate.delete()
        # return Response(username"is deleted.")
        return Response("User is deleted.")
    
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,many=True)
    return Response(serializer.data)