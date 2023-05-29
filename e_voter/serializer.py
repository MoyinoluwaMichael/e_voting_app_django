from rest_framework import serializers

from e_voter.models import Voter


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['first_name', 'last_name', 'date_of_birth']
