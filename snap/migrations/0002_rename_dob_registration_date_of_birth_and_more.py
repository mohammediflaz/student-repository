# Generated by Django 4.2.3 on 2023-08-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='remark',
            new_name='remarks',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='contact_no',
        ),
        migrations.AddField(
            model_name='registration',
            name='class_field',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='registration',
            name='contact_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
