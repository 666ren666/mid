# Generated by Django 4.1.3 on 2022-12-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_alter_userprofile_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='prof (6).jpg', null=True, upload_to=''),
        ),
    ]
