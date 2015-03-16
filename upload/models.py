from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='media/%Y/%m/%d')

class batchData(models.Model):
    state = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    cases = models.IntegerField()
    days_accumulated = models.IntegerField()

    def __str__(self):
        return self.state

class insertData(models.Model):

    data_release_date = models.DateTimeField()
    state = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    case =  models.IntegerField(default = 0)
    days_accumulated = models.IntegerField(default = 0)
    date_published = models.DateTimeField('date published')

    def __str__(self):
        return self.state

class invitation(models.Model):
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

    def __str__(self):
        return u"%s %s" % (self.name, self.date)
