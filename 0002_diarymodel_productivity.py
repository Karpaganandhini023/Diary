# Generated by Django 2.2.6 on 2019-10-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarymodel',
            name='productivity',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
