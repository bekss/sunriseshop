# Generated by Django 3.1.6 on 2021-02-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0002_auto_20210214_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rysar',
            name='soldat',
        ),
        migrations.RemoveField(
            model_name='soldat',
            name='rab',
        ),
        migrations.RemoveField(
            model_name='status',
            name='status_many',
        ),
        migrations.RemoveField(
            model_name='vazir',
            name='Sultan',
        ),
        migrations.RemoveField(
            model_name='vazir',
            name='rysar',
        ),
        migrations.RemoveField(
            model_name='vazir',
            name='status',
        ),
        migrations.DeleteModel(
            name='Many',
        ),
        migrations.DeleteModel(
            name='Rab',
        ),
        migrations.DeleteModel(
            name='Rysar',
        ),
        migrations.DeleteModel(
            name='Soldat',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Sultan',
        ),
        migrations.DeleteModel(
            name='Vazir',
        ),
    ]
