# Generated by Django 4.0 on 2022-01-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_remove_meetup_organizer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='mahdi.zareei.80@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
