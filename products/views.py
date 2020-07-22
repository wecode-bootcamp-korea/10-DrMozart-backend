from django.views import View
from django.http import JsonResponse

from . import models


class MainView(View):
    def get(self, request):
        data = models.Product.objects.filter(is_main=True).values(
            "name",
            "tag",
            "image_url",
            "price",
            "price_sale",
            "fleg_sale",
            "fleg_gift",
            "fleg_new",
            "fleg_best",
            "product_detail_url",
        )
        return JsonResponse({"data": list(data)}, status=200)


class AllView(View):
    def get(self, request):
        data = models.Product.objects.all().values(
            "name",
            "tag",
            "image_url",
            "price",
            "price_sale",
            "fleg_sale",
            "fleg_gift",
            "fleg_new",
            "fleg_best",
            "product_detail_url",
        )
        return JsonResponse({"data": list(data)}, status=200)
