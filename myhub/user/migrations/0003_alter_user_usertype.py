# Generated by Django 4.2.7 on 2023-12-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.CharField(choices=[('User', 'User'), ('Instructor', 'Instructor')], default='User', max_length=15),
        ),
    ]