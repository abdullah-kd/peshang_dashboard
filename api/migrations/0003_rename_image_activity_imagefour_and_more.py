# Generated by Django 4.1.2 on 2023-02-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_team_certificate_alter_team_rolle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='image',
            new_name='imageFour',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='person',
        ),
        migrations.AddField(
            model_name='activity',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='activity',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='activity',
            name='imageTitle',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='activity',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
    ]