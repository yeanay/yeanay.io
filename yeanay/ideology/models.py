from django.db import models

class Legislator(models.Model):
    govtrackid = models.IntegerField()
    lastname = models.TextField()
    firstname = models.TextField()
    namemodifier = models.TextField()
    birthday = models.DateField(null=True, blank=True)
    gender = models.TextField()
    pvsid = models.TextField()
    bioguideid = models.TextField()
    youtubeid = models.TextField()
    twitterid = models.TextField()
    facebookid = models.TextField()
    thomasid = models.TextField()
    icpsrid = models.TextField()

class LegislatorSession(models.Model):
    govtrackid = models.IntegerField()
    legislator = models.ForeignKey(Legislator)
    chamber = models.TextField()
    district = models.IntegerField()
    state = models.TextField()
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    party = models.TextField()
    session = models.IntegerField()

class Ideology(models.Model):
    legislator = models.ForeignKey(Legislator)
    congress = models.IntegerField()
    icpsrid = models.IntegerField()
    first_dimension = models.FloatField()
    second_dimension = models.FloatField()
    state_id = models.IntegerField()
    party_id = models.IntegerField()
    name = models.TextField()
    district = models.IntegerField()
    chamber = models.CharField(max_length=6)