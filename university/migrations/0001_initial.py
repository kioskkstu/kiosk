# Generated by Django 2.2 on 2019-07-17 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('floor', models.PositiveIntegerField(verbose_name='Floor')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('about_ru', models.TextField(null=True, verbose_name='About')),
                ('about_en', models.TextField(null=True, verbose_name='About')),
                ('about_kg', models.TextField(null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('about_ru', models.TextField(null=True, verbose_name='About')),
                ('about_en', models.TextField(null=True, verbose_name='About')),
                ('about_kg', models.TextField(null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('about_ru', models.TextField(null=True, verbose_name='About')),
                ('about_en', models.TextField(null=True, verbose_name='About')),
                ('about_kg', models.TextField(null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Institute',
                'verbose_name_plural': 'Institutes',
            },
        ),
        migrations.CreateModel(
            name='PreUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=40, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=40, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=40, null=True, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('about_ru', models.TextField(null=True, verbose_name='About')),
                ('about_en', models.TextField(null=True, verbose_name='About')),
                ('about_kg', models.TextField(null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Pre-university preparation',
                'verbose_name_plural': 'Pre-university preparations',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('status_ru', models.CharField(max_length=50, null=True, verbose_name='Status')),
                ('status_en', models.CharField(max_length=50, null=True, verbose_name='Status')),
                ('status_kg', models.CharField(max_length=50, null=True, verbose_name='Status')),
                ('contact', models.CharField(max_length=50, verbose_name='Contact')),
                ('contact_ru', models.CharField(max_length=50, null=True, verbose_name='Contact')),
                ('contact_en', models.CharField(max_length=50, null=True, verbose_name='Contact')),
                ('contact_kg', models.CharField(max_length=50, null=True, verbose_name='Contact')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='university.Department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('grade', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, verbose_name='Grade')),
                ('grade_ru', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, null=True, verbose_name='Grade')),
                ('grade_en', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, null=True, verbose_name='Grade')),
                ('grade_kg', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, null=True, verbose_name='Grade')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='university.Department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments_of_faculty', to='university.Faculty', verbose_name='Faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments_of_institute', to='university.Institute', verbose_name='Institute'),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=20, null=True, verbose_name='Name')),
                ('floor', models.PositiveIntegerField(verbose_name='Floor')),
                ('about', models.CharField(max_length=50, null=True, verbose_name='About')),
                ('about_ru', models.CharField(max_length=50, null=True, verbose_name='About')),
                ('about_en', models.CharField(max_length=50, null=True, verbose_name='About')),
                ('about_kg', models.CharField(max_length=50, null=True, verbose_name='About')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='university.Building', verbose_name='Building')),
            ],
            options={
                'verbose_name': 'Classroom',
                'verbose_name_plural': 'Classrooms',
            },
        ),
    ]
