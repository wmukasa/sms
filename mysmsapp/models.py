from django.db import models
class phoneNumbers(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Sentsms(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    statusCode = models.IntegerField()
    number = models.CharField(max_length=15)
    def __str__(self):
        return '{0}-{1}-{2}'.format( self.status,self.statusCode,self.number)
