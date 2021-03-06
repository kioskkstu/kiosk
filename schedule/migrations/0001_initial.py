# Generated by Django 2.2 on 2019-07-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_kg', models.CharField(max_length=50, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(choices=[(1, '8:00-9:20'), (2, '9:30-10:50'), (3, '11:00-12:20'), (4, '13:00-14:20'), (5, '14:30-15:50'), (6, '16:00-17:20')], default=1, verbose_name='Time')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Mon'), (2, 'Tue'), (3, 'Wed'), (4, 'Thu'), (5, 'Fri'), (6, 'Sat')], default=1, verbose_name='Day of the week')),
                ('week', models.IntegerField(choices=[(1, 'Числ'), (2, 'Знам')], default=1, verbose_name='Week')),
                ('type_of_lecture', models.IntegerField(choices=[(1, 'Лк'), (2, 'Пр'), (3, 'Лб')], default=1, verbose_name='Type of lecture')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='university.Classroom', verbose_name='Classroom')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='university.Group', verbose_name='Group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='schedule.Subject', verbose_name='Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='university.Teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
    ]
