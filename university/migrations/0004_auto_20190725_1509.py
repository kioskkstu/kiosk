# Generated by Django 2.2 on 2019-07-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20190725_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='grade',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1, verbose_name='Grade'),
        ),
    ]
