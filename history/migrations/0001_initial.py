# Generated by Django 2.2 on 2019-07-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('text_kg', models.TextField(null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
    ]
