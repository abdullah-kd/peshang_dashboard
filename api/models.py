from django.db import models

# Create your models here.


class Team(models.Model):

    BAREWBAR = 'BR'
    EDRA = 'ED'
    MAMOSTA = 'JR'
    ROLLS_IN_INSTUTE = [
        (BAREWBAR, 'بەرێوبەر'),
        (EDRA, 'ئیدارە'),
        (MAMOSTA, 'مامۆستا'),
        
    ]
    BAKALORIS = 'BR'
    DEBLOM = 'DB'
    MASTER = 'MA'
    DCTOR = 'DC'
    PROFESOR = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (BAKALORIS, 'بەکالۆریۆس'),
        (DEBLOM, 'دیبلۆم'),
        (MASTER, 'ماستەر'),
        (DCTOR, 'دکتۆرا'),
        (PROFESOR, 'پرۆفیسۆر'),
    ]
    rolle = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=BAKALORIS,
    )

   
    name = models.CharField(max_length=200)
    certificate = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=DEBLOM)
    specialty = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='blog_images')

    def __str__(self):
        return self.name
    

    name = models.CharField(max_length=200)
    rolle = models.CharField(max_length=200)
    certificate = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='blog_images')

    def __str__(self):
        return self.name

