# Generated by Django 4.1.3 on 2022-11-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
            ],
        ),
    ]