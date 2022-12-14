# Generated by Django 4.1 on 2022-08-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MealName', models.CharField(max_length=200)),
                ('MealCategory', models.CharField(max_length=200)),
                ('MealPrice', models.IntegerField()),
                ('MealDescription', models.TextField()),
                ('MealImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('MealCost', models.IntegerField()),
                ('MealPoints', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=200)),
                ('UserPass', models.CharField(max_length=50)),
                ('UserEmail', models.CharField(max_length=100)),
                ('UserPhone', models.IntegerField()),
                ('UserAdress', models.TextField()),
                ('UserInnerName', models.CharField(max_length=200)),
                ('u_Admin', models.BooleanField(default=0)),
                ('Staff', models.BooleanField(default=1)),
                ('UserPoints', models.IntegerField(default=0)),
            ],
        ),
    ]
