# Generated by Django 3.1.1 on 2020-09-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('contact_info', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=500)),
            ],
        ),
    ]
