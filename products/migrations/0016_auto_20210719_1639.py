# Generated by Django 3.2.5 on 2021-07-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210719_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='heightmodel',
            name='height_en',
            field=models.CharField(max_length=20, null=True, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='heightmodel',
            name='height_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='heightmodel',
            name='height_uz',
            field=models.CharField(max_length=20, null=True, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='weightmodel',
            name='weight_en',
            field=models.CharField(max_length=20, null=True, verbose_name='weight'),
        ),
        migrations.AddField(
            model_name='weightmodel',
            name='weight_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='weight'),
        ),
        migrations.AddField(
            model_name='weightmodel',
            name='weight_uz',
            field=models.CharField(max_length=20, null=True, verbose_name='weight'),
        ),
        migrations.AddField(
            model_name='widthmodel',
            name='width_en',
            field=models.CharField(max_length=20, null=True, verbose_name='width'),
        ),
        migrations.AddField(
            model_name='widthmodel',
            name='width_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='width'),
        ),
        migrations.AddField(
            model_name='widthmodel',
            name='width_uz',
            field=models.CharField(max_length=20, null=True, verbose_name='width'),
        ),
    ]
