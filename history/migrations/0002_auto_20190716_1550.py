# Generated by Django 2.2 on 2019-07-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='name_kg',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='text_kg',
            field=models.TextField(null=True),
        ),
    ]
