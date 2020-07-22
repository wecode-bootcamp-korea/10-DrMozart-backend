from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/Python/crawling/python/dr_product_main.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            pk = models.Skin.objects.get(pk=13).id
            for row in data_reader:
                if models.Product.objects.filter(name=row[0]):  # 기존 DB에 같은 제품이 존재할 경우
                    print(row[0])
                    models.NoN_Product(
                        name=row[0],
                        tag=row[1],
                        image_url=row[2],
                        is_main=True,
                        skin_id=pk,
                        price=row[8].replace(",", ""),
                        price_sale=row[9].replace(",", ""),
                        fleg_new=row[6],
                        fleg_gift=row[4],
                        fleg_sale=row[3],
                        fleg_best=row[5],
                    ).save()
                else:  # 기존 DB에 없는 경우
                    models.Product(
                        name=row[0],
                        tag=row[1],
                        image_url=row[2],
                        is_main=True,
                        skin_id=pk,
                        price=row[8].replace(",", ""),
                        price_sale=row[9].replace(",", ""),
                        fleg_new=row[6],
                        fleg_gift=row[4],
                        fleg_sale=row[3],
                        fleg_best=row[5],
                    ).save()
