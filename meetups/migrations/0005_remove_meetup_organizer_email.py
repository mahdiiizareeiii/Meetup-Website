# Generated by Django 4.0 on 2022-01-10 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participant_meetup_date_meetup_organizer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='organizer_email',
        ),
    ]
