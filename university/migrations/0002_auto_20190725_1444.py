# Generated by Django 2.2 on 2019-07-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_kg',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name_kg',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name_kg',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='preuniversity',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='preuniversity',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='preuniversity',
            name='name_kg',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='preuniversity',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
    ]
