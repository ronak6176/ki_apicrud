# Generated by Django 4.1.3 on 2022-11-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_ro'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='ro',
        ),
    ]
