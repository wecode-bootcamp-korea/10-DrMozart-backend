# Generated by Django 3.0.7 on 2020-07-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'genre_category',
            },
        ),
        migrations.CreateModel(
            name='Line_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'line_category',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Online_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu')),
            ],
            options={
                'db_table': 'online_category',
            },
        ),
        migrations.CreateModel(
            name='Skin_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu')),
            ],
            options={
                'db_table': 'skin_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('price_sale', models.IntegerField()),
                ('fleg_sale', models.CharField(max_length=10)),
                ('fleg_gift', models.CharField(max_length=10)),
                ('fleg_new', models.CharField(max_length=10)),
                ('fleg_best', models.CharField(max_length=10)),
                ('is_main', models.BooleanField(default=False)),
                ('product_detail_url', models.CharField(max_length=200)),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Genre_Category')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Line_Category')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu')),
                ('online_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Online_Category')),
                ('skin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Skin_Category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='line_category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu'),
        ),
        migrations.AddField(
            model_name='genre_category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu'),
        ),
        migrations.CreateModel(
            name='Distinct_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('price_sale', models.IntegerField()),
                ('fleg_sale', models.CharField(max_length=10)),
                ('fleg_gift', models.CharField(max_length=10)),
                ('fleg_new', models.CharField(max_length=10)),
                ('fleg_best', models.CharField(max_length=10)),
                ('is_main', models.BooleanField(default=False)),
                ('product_detail_url', models.CharField(max_length=200)),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Genre_Category')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Line_Category')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Menu')),
                ('online_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Online_Category')),
                ('skin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Skin_Category')),
            ],
            options={
                'db_table': 'non_products',
            },
        ),
    ]