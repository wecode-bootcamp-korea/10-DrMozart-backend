from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin solution_1.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                pk = models.Skin.objects.get(pk=1).id
                if models.Product.objects.filter(name=row[1]):  # 기존 DB에 같은 제품이 존재할 경우
                    models.NoN_Product(
                        name=row[1],
                        tag=row[2],
                        image_url=row[3],
                        skin_id=pk,
                        price=row[9],
                        price_sale=row[10],
                        fleg_new=row[7],
                        fleg_gift=row[5],
                        fleg_sale=row[4],
                        fleg_best=row[6],
                    ).save()
                else:  # 기존 DB에 없는 경우
                    models.Product(
                        name=row[1],
                        tag=row[2],
                        image_url=row[3],
                        skin_id=pk,
                        price=row[9],
                        price_sale=row[10],
                        fleg_new=row[7],
                        fleg_gift=row[5],
                        fleg_sale=row[4],
                        fleg_best=row[6],
                    ).save()
