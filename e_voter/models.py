from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Voter(AbstractUser):
    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return f"""
        Full Name: {self.first_name} {self.last_name}
        DOB: {self.date_of_birth}
        """


class Party(models.Model):
    acronym = models.CharField(max_length=10, blank=False)
    full_name = models.CharField(max_length=100, blank=False)
    candidate = models.ForeignKey(Voter, on_delete=models.PROTECT)

    def __str__(self):
        return f"""
        Party Name: {self.full_name}({self.acronym})
        Candidate: {self.candidate}
        """


class Poll(models.Model):
    voter: Voter = models.ForeignKey(Voter, on_delete=models.PROTECT)
    party: Party = models.ForeignKey(Party, on_delete=models.PROTECT)

    def __str__(self):
        return f"""
        Voter Name: {self.voter.first_name} {self.voter.last_name}
        Choice: {self.party.acronym}
        """
