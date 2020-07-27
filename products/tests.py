from django.test import TestCase

from django.test import TestCase
from django.test import Client


class ProductAllTest(TestCase):
    def test_product_all_get_success(self):
        client = Client()
        response = client.get("/product/all")

        self.assertEqual(response.status_code, 200)


class ProductMainTest(TestCase):
    def test_product_main_get_success(self):
        client = Client()
        response = client.get("/product/main")

        self.assertEqual(response.status_code, 200)


class ProductDetailTest(TestCase):
    def test_product_detail_get_success(self):
        client = Client()
        response = client.get("/product/detail/1")

        self.assertEqual(response.status_code, 200)

    def test_product_detail_get_fail(self):
        client = Client()
        response = client.get("/product/detail/strng")

        self.assertEqual(response.status_code, 404)
