# Generated by Django 2.2 on 2019-07-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]