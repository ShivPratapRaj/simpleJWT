from django.shortcuts import render
from .models import Ceo
from .serializers import CeoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CeoModelViewSet(viewsets.ModelViewSet):
    queryset = Ceo.objects.all()
    serializer_class = CeoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]