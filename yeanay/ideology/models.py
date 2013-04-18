from django.db import models

class ideology(models.Model):
    congress = models.IntegerField()
    icpsr_id = models.IntegerField()
    first_dimension = models.FloatField()
    second_dimension = models.FloatField()
    state_id = models.IntegerField()
    party_code = models.IntegerField()
    name = models.TextField()
