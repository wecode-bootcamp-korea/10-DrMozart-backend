from django.db import models
from core import models as core_models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "menus"

    def __str__(self):
        return self.name


class Skin_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "skin_category"

    def __str__(self):
        return self.name


class Genre_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genre_category"

    def __str__(self):
        return self.name


class Line_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "line_category"

    def __str__(self):
        return self.name


class Online_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "online_category"

    def __str__(self):
        return self.name


class Product(core_models.TempDate):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, null=True)
    skin = models.ForeignKey("Skin_Category", on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey("Genre_Category", on_delete=models.CASCADE, null=True)
    line = models.ForeignKey("Line_Category", on_delete=models.CASCADE, null=True)
    online = models.ForeignKey("Online_Category", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    price = models.IntegerField()
    price_sale = models.IntegerField()
    fleg_sale = models.CharField(max_length=10)
    fleg_gift = models.CharField(max_length=10)
    fleg_new = models.CharField(max_length=10)
    fleg_best = models.CharField(max_length=10)
    is_main = models.BooleanField(default=False)
    product_detail_url = models.CharField(max_length=200)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class Distinct_Product(core_models.TempDate):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, null=True)
    skin = models.ForeignKey("Skin_Category", on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey("Genre_Category", on_delete=models.CASCADE, null=True)
    line = models.ForeignKey("Line_Category", on_delete=models.CASCADE, null=True)
    online = models.ForeignKey("Online_Category", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    price = models.IntegerField()
    price_sale = models.IntegerField()
    fleg_sale = models.CharField(max_length=10)
    fleg_gift = models.CharField(max_length=10)
    fleg_new = models.CharField(max_length=10)
    fleg_best = models.CharField(max_length=10)
    is_main = models.BooleanField(default=False)
    product_detail_url = models.CharField(max_length=200)

    class Meta:
        db_table = "non_products"

    def __str__(self):
        return self.name
