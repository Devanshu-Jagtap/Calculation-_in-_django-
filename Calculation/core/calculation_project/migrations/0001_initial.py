# Generated by Django 4.2.7 on 2023-11-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value1', models.IntegerField()),
                ('Value2', models.IntegerField()),
            ],
        ),
    ]