# Generated by Django 5.0.7 on 2024-07-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordcard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='word_card_images/'),
        ),
    ]
