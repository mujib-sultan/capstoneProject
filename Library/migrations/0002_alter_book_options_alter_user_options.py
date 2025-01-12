# Generated by Django 5.1.4 on 2025-01-11 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_manage_books', 'Can manage books')]},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_manage_users', 'Can manage users'), ('can_manage_books', 'Can manage books')]},
        ),
    ]
