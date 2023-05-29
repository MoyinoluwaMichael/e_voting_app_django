from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from e_voter.models import Voter
from e_voter.serializer import VoterSerializer


class VotersRoute(ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer