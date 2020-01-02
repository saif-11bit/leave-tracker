from django.shortcuts import render
from rest_framework import viewsets
from .models import LeaveType, Leave, Staff, Holiday
from .serializers import LeaveSerializer, LeaveTypeSerializer, StaffSerializer, HolidaySerializer
from django_filters.rest_framework import DjangoFilterBackend



class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['staff',]

class LeaveViewset(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    filterset_fields = ['staff','leave_type', 'from_date', 'to_date', ]


class LeaveTypeViewset(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    filterset_fields = ['leave_type',]


class HolidayViewset(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    filterset_fields = ['name', 'from_date', 'to_date']
