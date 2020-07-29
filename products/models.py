from django.db import models

from core import models as core_models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "menus"

    def __str__(self):
        return self.name


class SkinCategory(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "skin_category"

    def __str__(self):
        return self.name


class Genreategory(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genre_category"

    def __str__(self):
        return self.name


class LineCategory(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "line_category"

    def __str__(self):
        return self.name


class OnlineCategory(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "online_category"

    def __str__(self):
        return self.name


class ProductFlag(models.Model):
    flag_sale = models.CharField(max_length=10)
    flag_gift = models.CharField(max_length=10)
    flag_new  = models.CharField(max_length=10)
    flag_best = models.CharField(max_length=10)

    class Meta:
        db_table = "product_flag"

    def __str__(self):
        return self.name


class Image(models.Model):
    image_url = models.TextField(max_length=1000)

    class Meta:
        db_table = "image"


class ProductDetailImage(models.Model):
    product_detail = models.ForeignKey("ProductDetail", on_delete=models.CASCADE, null=True)
    image          = models.ForeignKey("Image", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "product_detail_image"

    def __str__(self):
        return f"{self.product_detail}-{self.image}"


class Product(core_models.TempDate):
    skin           = models.ForeignKey("SkinCategory", on_delete=models.CASCADE, null=True)
    genre          = models.ForeignKey("GenreCategory", on_delete=models.CASCADE, null=True)
    line           = models.ForeignKey("LineCategory", on_delete=models.CASCADE, null=True)
    online         = models.ForeignKey("OnlineCategory", on_delete=models.CASCADE, null=True)
    flag           = models.ForeignKey("ProductFlag", on_delete=models.CASCADE, null=True)
    product_detail = models.ForeignKey("ProductDetail", on_delete=models.CASCADE, null=True)
    star_average   = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    name           = models.CharField(max_length=100)
    main_image_url = models.CharField(max_length=1000, default="")
    is_main        = models.BooleanField(default=False)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class DistinctProduct(core_models.TempDate):
    skin   = models.ForeignKey("SkinCategory", on_delete=models.CASCADE, null=True)
    genre  = models.ForeignKey("GenreCategory", on_delete=models.CASCADE, null=True)
    line   = models.ForeignKey("LineCategory", on_delete=models.CASCADE, null=True)
    online = models.ForeignKey("OnlineCategory", on_delete=models.CASCADE, null=True)
    flag   = models.ForeignKey("ProductFlag", on_delete=models.CASCADE, null=True)
    name   = models.CharField(max_length=100)

    class Meta:
        db_table = "non_products"

    def __str__(self):
        return self.name


class ProductDetail(core_models.TempDate):
    tag         = models.CharField(max_length=100)
    price       = models.IntegerField()
    price_sale  = models.IntegerField()
    detail_html = models.TextField(max_length=1000)

    class Meta:
        db_table = "product_detail"

    def __str__(self):
        return self.tag
