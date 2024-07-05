# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bukus.models import Bukus
from bukus.serializers import BukusSerializer

# @csrf_exempt
@api_view(['GET','POST'])
def bukus_list(request):
    if request.method == 'GET':
        buku = Bukus.objects.all()
        serializer = BukusSerializer(buku, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BukusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def bukus_detail(request,id):
    try:
        buku = Bukus.objects.get(id=id)
    except Bukus.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = BukusSerializer(buku)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BukusSerializer(buku, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        buku.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)