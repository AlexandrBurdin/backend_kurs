from rest_framework import viewsets
from .models import Employee, BusinessTrip
from .serializers import EmployeeSerializer, BusinessTripSerializer
from django.shortcuts import render


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class BusinessTripViewSet(viewsets.ModelViewSet):
    queryset = BusinessTrip.objects.all()
    serializer_class = BusinessTripSerializer


def frontend_view(request):
    return render(request, 'index.html')
