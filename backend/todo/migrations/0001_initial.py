# Generated by Django 5.2.1 on 2025-06-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('discription', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
