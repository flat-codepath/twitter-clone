# Generated by Django 5.1.1 on 2024-10-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='meep',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]
