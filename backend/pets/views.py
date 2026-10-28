from django.db.models.manager import BaseManager
from rest_framework import viewsets

from .models import Pet
from .serializers import PetSerializer


class PetView(viewsets.ModelViewSet):
    """API endpoint that allows pets to be viewed or edited."""

    serializer_class = PetSerializer
    queryset: BaseManager = Pet.objects.all()
