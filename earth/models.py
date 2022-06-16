from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    UserType = models.CharField(max_length = 100, default = 'admin')

class Create(models.Model):
    Title = models.CharField(max_length=100)
    Description =  models.CharField(max_length=1000)
    ItemImage =  models.ImageField(upload_to='images/',null=True)
    Owner = models.ForeignKey('User', limit_choices_to={'UserType':'Donor'},on_delete=models.CASCADE,related_name="users_item")
    Amount = models.IntegerField(default = 0)
    Benefactor = models.ForeignKey('User',limit_choices_to={'UserType':'Receiver'},on_delete=models.CASCADE,related_name='benefator',null=True)
    def __str__(self):
        return f"{self.Title}" 


class UserRequest(models.Model):
    Username =models.ForeignKey('User',limit_choices_to={'UserType':'Donee'},on_delete=models.CASCADE,related_name="users_request")
    ProofPic1 = models.ImageField(upload_to='images/',null=True)
    RequestStatus = models.BooleanField(default = False)
    About =  models.CharField(max_length = 3000)
    Donation = models.IntegerField(default = 0)
    Title =  models.CharField(max_length = 3000 ,null = True)
    Goal = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.id} {self.Username} made a request"

    
