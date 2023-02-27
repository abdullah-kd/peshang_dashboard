# Generated by Django 4.1.2 on 2023-02-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='certificate',
            field=models.CharField(choices=[('بەکالۆریۆس', 'بەکالۆریۆس'), ('دیبلۆم', 'دیبلۆم'), ('ماستەر', 'ماستەر'), ('دکتۆرا', 'دکتۆرا'), ('پرۆفیسۆر', 'پرۆفیسۆر')], default='دیبلۆم', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='rolle',
            field=models.CharField(choices=[('بەرێوبەر', 'بەرێوبەر'), ('ئیدارە', 'ئیدارە'), ('مامۆستا', 'مامۆستا')], default='مامۆستا', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='specialty',
            field=models.CharField(choices=[('بیرکای', 'بیرکای'), ('ئینگلیزی', 'زمانی ئینگلیزی'), ('زمانی عەرەبی', 'زمانی عەرەبی'), ('کارگێری', 'کارگێری'), ('کۆمپیتەر', 'کۆمپیتەر'), ('زمانی کوردی', 'زمانی کوردی'), ('فیزیا ', 'فیزیا')], max_length=100),
        ),
    ]