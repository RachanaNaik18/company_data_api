from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Company
from rest_framework import viewsets
from .serializers import Company_S

# Create your views here.


class Company_view(viewsets.ModelViewSet):
    queryset  = Company.objects.all()
    serializer_class  = Company_S
