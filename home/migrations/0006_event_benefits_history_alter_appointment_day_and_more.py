# Generated by Django 4.1.3 on 2022-11-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_appointment_delete_ro'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('url', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('url', models.CharField(max_length=2000)),
                ('time', models.CharField(max_length=2000)),
                ('day', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='url',
            field=models.CharField(max_length=2000),
        ),
    ]
