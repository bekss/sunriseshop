# Generated by Django 3.1.6 on 2021-02-14 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='status_many',
        ),
        migrations.AddField(
            model_name='vazir',
            name='many',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rab',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rab',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rysar',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rysar',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='soldat',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='soldat',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='soldat',
            name='rab',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.rab'),
        ),
        migrations.AlterField(
            model_name='sultan',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sultan',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vazir',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vazir',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vazir',
            name='status',
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(
            name='Many',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
