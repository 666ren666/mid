# Generated by Django 4.1.3 on 2022-12-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_deckplayera'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeckPlayerB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.CharField(default='suit', max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, default='B-Red.png', null=True, upload_to='')),
            ],
        ),
    ]
