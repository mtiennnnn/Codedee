# Generated by Django 4.1.3 on 2022-12-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='language',
            field=models.CharField(max_length=20, null=True),
        ),
    ]