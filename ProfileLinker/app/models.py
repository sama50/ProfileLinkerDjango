from django.db import models
from django.contrib.auth.models import User

# Create your models here.


EDUCATION_CHOICE = (
 ('B.TECH', 'B.TECH'),
 ('B.E', 'B.E'),
 ('Bsc', 'Bsc'),
 ('OTHER', 'OTHER'),
)

class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , unique=True)
    name = models.CharField(max_length=255)
    Education = models.CharField(choices=EDUCATION_CHOICE, max_length=50)
    email = models.EmailField(max_length=300)
    image = models.ImageField(upload_to='profile')

class LinkData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameLink = models.CharField(max_length=255)
    link = models.URLField(max_length=300)


class ShareDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameid = models.CharField(max_length=500,unique=True)