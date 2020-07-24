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


class Product_Star(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    star_5 = models.IntegerField(default=0)
    star_4 = models.IntegerField(default=0)
    star_3 = models.IntegerField(default=0)
    star_2 = models.IntegerField(default=0)
    star_1 = models.IntegerField(default=0)

    class Meta:
        db_table = "product_star"

    def __str__(self):
        return self.name


class Product_Plag(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    flag_sale = models.CharField(max_length=10)
    flag_gift = models.CharField(max_length=10)
    flag_new = models.CharField(max_length=10)
    flag_best = models.CharField(max_length=10)

    class Meta:
        db_table = "product_flag"

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
    product_detail_url = models.TextField(max_length=200)
    product_review_url = models.TextField(max_length=200, default="")
    star = models.ForeignKey(
        "Product_Star", on_delete=models.CASCADE, null=True, related_name="star"
    )

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


class Product_Detail(core_models.TempDate):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image_url1 = models.CharField(max_length=1000)
    image_url2 = models.CharField(max_length=1000)
    image_url3 = models.CharField(max_length=1000)
    image_url4 = models.CharField(max_length=1000)
    detail_html = models.TextField(max_length=10000)

    class Meta:
        db_table = "product_detail"

    def __str__(self):
        return self.name
