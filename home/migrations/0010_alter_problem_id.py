# Generated by Django 4.1.1 on 2022-11-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_problem_short_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
