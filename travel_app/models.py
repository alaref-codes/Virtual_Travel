from django.db import models

# Create your models here.

class Country(models.Model):

    name =  models.CharField(max_length=20)
    info = models.TextField(default='')
    pic = models.ImageField(null=True,blank=True)
    languag = models.CharField(default='' , max_length=30)
    languageUrl = models.TextField(default='')


    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class Trafood(models.Model):

    name =  models.CharField(max_length=20)
    info = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pic = models.ImageField(null=True,blank=True)
    url = models.TextField(default='')
    
    def __str__(self):
        return self.name

class bestPlace(models.Model):

    name =  models.CharField(max_length=20) 
    info = models.TextField(default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    position = models.CharField(default='',max_length=30)
    city = models.CharField(default='',max_length=50)
    pic = models.ImageField(null=True,blank=True)
    url = models.TextField(default='')

    def __str__(self):
        return self.name

class Language(models.Model):
    
    name = models.CharField(default='',max_length=20)
    info = models.TextField(default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name