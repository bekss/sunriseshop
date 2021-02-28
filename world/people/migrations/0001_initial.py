# Generated by Django 3.1.6 on 2021-02-14 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Many',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('many_month', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'Деньги',
                'verbose_name_plural': 'Деньги',
            },
        ),
        migrations.CreateModel(
            name='Rab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lname', models.CharField(max_length=50, unique=True)),
                ('age', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Раб',
                'verbose_name_plural': 'Рабы',
            },
        ),
        migrations.CreateModel(
            name='Rysar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lname', models.CharField(max_length=50, unique=True)),
                ('age', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Рыцарь',
                'verbose_name_plural': 'Рыцари',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=2)),
                ('status_many', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.many')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Sultan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lname', models.CharField(max_length=50, unique=True)),
                ('age', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Султан',
                'verbose_name_plural': 'Султаны',
            },
        ),
        migrations.CreateModel(
            name='Vazir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lname', models.CharField(max_length=50, unique=True)),
                ('age', models.CharField(max_length=3)),
                ('Sultan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.sultan')),
                ('rysar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.rysar')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.status')),
            ],
            options={
                'verbose_name': 'Вазир',
                'verbose_name_plural': 'Вазиры',
            },
        ),
        migrations.CreateModel(
            name='Soldat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lname', models.CharField(max_length=50, unique=True)),
                ('age', models.CharField(max_length=3)),
                ('rab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.rab')),
            ],
            options={
                'verbose_name': 'Солдат',
                'verbose_name_plural': 'Солдаты',
            },
        ),
        migrations.AddField(
            model_name='rysar',
            name='soldat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.soldat'),
        ),
    ]
