import random

from django.views import View
from django.http import JsonResponse

from products.models import Product,ProductDetailImage
from reviews.models import Review



class ProductMainView(View):
    def get(self, request):
        data = Product.objects.filter(is_main=True).values(
            "id",
            "name",
            "product_detail__tag",
            "main_image_url",
            "product_detail__price",
            "product_detail__price_sale",
            "flag__flag_sale",
            "flag__flag_gift",
            "flag__flag_new",
            "flag__flag_best",
            "star_average",
        )
        reviews = (
            reviews_Review.objects.exclude(image_url="")
            .filter(star_point=5)
            .order_by("?")
            .values(
                "star_point", "worry__name", "skintype__name", "content", "image_url"
            )
        )[:4]
        return JsonResponse({"data": list(data), "reviews": list(reviews)}, status=200)


class ProductAllView(View):
    def get(self, request):
        data = Product.objects.prefetch_related("flag","product_detail").values(
            "id",
            "name",
            "product_detail__tag",
            "main_image_url",
            "product_detail__price",
            "product_detail__price_sale",
            "flag__flag_sale",
            "flag__flag_gift",
            "flag__flag_new",
            "flag__flag_best",
            "star_average",
            "created",
        )
        return JsonResponse({"data": list(data)}, status=200)


class ProductDetailView(View):
    def get(self, request, pk):
        review_list = []
        detail_pk = Product.objects.filter(id=pk)
        image_pk = ProductDetailImage.objects.filter(product_detail_id=pk)
        images = image_pk.values("image__image_url")
        data = detail_pk.values("product_detail__detail_html")
        reviews = (
            reviews_Review.objects.select_related("worry", "skintype")
            .filter(product_id=pk)
            .values(
                "star_point", "worry__name", "skintype__name", "content", "image_url"
            )
        )
        return JsonResponse(
            {"images": list(images), "data": list(data), "reviews": list(reviews)},
            status=200,
        )
