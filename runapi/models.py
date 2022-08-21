from pickle import TRUE
from django.db import models


class Users(models.Model):
    UserName = models.CharField(max_length=200, null=False, blank=False)
    UserPass = models.CharField(max_length=50, blank=False)
    UserEmail = models.CharField(max_length=100, null=False, blank=False)
    UserPhone = models.IntegerField(null=True, blank=TRUE)
    UserAdress = models.TextField(null=True, blank=TRUE)
    UserInnerName = models.CharField(max_length=200, null=True, blank=TRUE)
    u_Admin = models.BooleanField(blank=TRUE, default=0)
    Staff = models.BooleanField(blank=TRUE, default=1)
    UserPoints = models.IntegerField(default=0)

    def __str__(self):
        return self.UserName


class Meals(models.Model):
    mealname = models.CharField(max_length=200, null=False, blank=False)
    mealcategory = models.CharField(max_length=200, null=False, blank=False)
    mealprice = models.IntegerField(null=True, blank=TRUE)
    mealdescription = models.TextField(null=True, blank=TRUE)
    mealimage = models.ImageField(null=True, blank=True)
    mealcost = models.IntegerField(null=True, blank=TRUE)
    mealpoints = models.IntegerField(default=0)

    def __str__(self):
        return self.mealname
