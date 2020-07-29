from django.db import models
from django.conf import settings

class Users(models.Model):
    LOGIN_USERID = "userid"
    LOGIN_KAKAO = "kakao"
    LOGIN_GOOGLE = "google"

    LOGIN_CHOICES = (
        (LOGIN_USERID, "userid"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_KAKAO, "google"),
    )

    name = models.CharField(max_length=255,null = True)
    userid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True,blank=True)
    phonenumber = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True) 
    genderid = models.ForeignKey('Genders',on_delete = models.CASCADE, null = True)
    skinworry = models.ForeignKey('SkinWorries',on_delete = models.CASCADE, null = True)
    skintype = models.ForeignKey('SkinTypes',on_delete = models.CASCADE, null = True)
    is_active = models.BooleanField(default=False)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_USERID)
    class Meta:
        db_table = 'users'

class Genders(models.Model):
    gender = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'genders'

class SkinWorries(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)
    name = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'skinworries'

class SkinTypes(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'skintypes'



