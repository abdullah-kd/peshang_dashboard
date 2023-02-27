# Generated by Django 4.1.2 on 2023-02-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('person', models.CharField(max_length=200)),
                ('discreption', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='blog_images')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolle', models.CharField(choices=[('BR', 'بەرێوبەر'), ('ED', 'ئیدارە'), ('JR', 'مامۆستا')], default='BR', max_length=2)),
                ('name', models.CharField(max_length=200)),
                ('certificate', models.CharField(choices=[('BR', 'بەکالۆریۆس'), ('DB', 'دیبلۆم'), ('MA', 'ماستەر'), ('DC', 'دکتۆرا'), ('GR', 'پرۆفیسۆر')], default='DB', max_length=2)),
                ('specialty', models.CharField(choices=[('BR', 'بیرکای'), ('EN', 'زمانی ئینگلیزی'), ('AR', 'زمانی عەرەبی'), ('KR', 'کارگێری'), ('IT', 'کۆمپیتەر'), ('KR', 'زمانی کوردی'), ('FZ', 'فیزیا')], max_length=2)),
                ('image', models.ImageField(blank=True, upload_to='blog_images')),
            ],
        ),
    ]
