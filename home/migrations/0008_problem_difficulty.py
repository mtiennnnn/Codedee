# Generated by Django 4.1.1 on 2022-11-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_problem_user_points_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficulty',
            field=models.CharField(max_length=15, null=True),
        ),
    ]