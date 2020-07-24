from django.db import models


class Users(models.Model):
    userid = models.CharField(max_length=255),
    name = models.CharField(max_length=50),
    password = models.CharField(max_length=200),
    email = models.CharField(max_length=200,null=True,blank=True),
    phonenumber = models.IntegerField(null=True,blank=True),
    address = models.CharField(max_length=255,null=True,blank=True),
    genderid = models.ForeignKey('Genders',on_delete = models.CASCADE, null = True),
    skinworry = models.ForeignKey('SkinWorries',on_delete = models.CASCADE, null = True),
    skintype = models.ForeignKey('SkinTypes',on_delete = models.CASCADE, null = True),
    emailagree = models.BooleanField(db_index=True, default=False)
    class Meta:
        db_table = 'users_info'

class Genders(models.Model):
    gender = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'genders'

class SkinWorries(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'skinworries'

class SkinTypes(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)

    class Meta:
        db_table = 'skintypes'
