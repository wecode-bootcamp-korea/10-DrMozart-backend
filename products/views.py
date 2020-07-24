from django.views import View
from django.http import JsonResponse

from . import models


class MainView(View):
    def get(self, request):
        data = models.Product.objects.filter(is_main=True).values(
            "id",
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
            "id",
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


class DetailView(View):
    def get(self, request, pk):
        pk = models.Product_Detail.objects.filter(product_id=pk)
        images = pk.values("image_url1", "image_url2", "image_url3", "image_url4",)
        data = pk.values("detail_html")
        return JsonResponse({"images": list(images), "data": list(data)}, status=200)
