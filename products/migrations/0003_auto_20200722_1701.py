# Generated by Django 3.0.7 on 2020-07-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200722_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distinct_product',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='distinct_product',
            name='line_id',
        ),
        migrations.RemoveField(
            model_name='distinct_product',
            name='online_id',
        ),
        migrations.RemoveField(
            model_name='distinct_product',
            name='skin_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='line_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='online_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='skin_id',
        ),
        migrations.AddField(
            model_name='distinct_product',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Genre_Category'),
        ),
        migrations.AddField(
            model_name='distinct_product',
            name='line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Line_Category'),
        ),
        migrations.AddField(
            model_name='distinct_product',
            name='online',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Online_Category'),
        ),
        migrations.AddField(
            model_name='distinct_product',
            name='skin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Skin_Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Genre_Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Line_Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='online',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Online_Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='skin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Skin_Category'),
        ),
    ]