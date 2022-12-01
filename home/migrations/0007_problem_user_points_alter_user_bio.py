# Generated by Django 4.1.1 on 2022-11-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemName', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField()),
                ('points', models.IntegerField(default=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='Hello Codedee User'),
        ),
    ]
