from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EmailSerializers
from .models import Email

URL = "http://localhost:8000/api"

@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/email-list/',
        'Detail View':URL + '/email-detail/<str:pk>',
        'Create':URL + '/email-create/',
        'Update':URL + '/email-updates/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def emailList(request):
    emails = Email.objects.all()
    serializer = EmailSerializers(emails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def emailDetail(request, pk):
    emails = Email.objects.get(id=pk)
    serializer = EmailSerializers(emails, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def emailCreate(request):
    serializer = EmailSerializers(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

