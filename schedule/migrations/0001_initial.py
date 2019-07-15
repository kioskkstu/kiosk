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
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(choices=[(1, '8:00-9:20'), (2, '9:30-10:50'), (3, '11:00-12:20'), (4, '13:00-14:20'), (5, '14:30-15:50'), (6, '16:00-17:20')], default=1)),
                ('day_of_week', models.IntegerField(choices=[(1, 'ПН'), (2, 'ВТ'), (3, 'СР'), (4, 'ЧТ'), (5, 'ПТ'), (6, 'СБ')], default=1)),
                ('week', models.IntegerField(choices=[(1, 'Числ'), (2, 'Знам')], default=1)),
                ('type', models.IntegerField(choices=[(1, 'Лк'), (2, 'Пр'), (3, 'Лб')], default=1)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='university.Teacher')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='university.Teacher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='university.Teacher')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='university.Teacher')),
            ],
        ),
    ]
