from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import serializers

from .models import *
from .serializers import *


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
    
#     def post(self, request):
#         serializers = WomenSerializer(data = request.data)
#         serializers.is_valid(raise_exception = True)
#         serializers.save()
        
#         return Response({'msg': serializers.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "method PUT not allowed"})
        
#         try:
#             instance = Women.objects.get(pk = pk)
#         except:
#             return Response({'error': 'object does not exists'})
        
#         serializer = WomenSerializer(data=request.data, instance = instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "method PUT not allowed"})
        
#         Women.objects.get(pk = pk).delete()
        
#         return Response({'delete': f'post f{pk} deletd'})