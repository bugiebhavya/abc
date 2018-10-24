from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User



class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

MyUser=get_user_model()
class Item(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    total_price= models.IntegerField(default=0)



    def publish(self):
        self.user=self.request.get('User')
        self.save()


    def get_absolute_url(self):
        return reverse("item_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.name
