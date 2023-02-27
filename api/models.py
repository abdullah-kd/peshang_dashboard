from django.db import models

# Create your models here.


class Team(models.Model):

    BAREWBAR = 'بەرێوبەر'
    EDRA = 'ئیدارە'
    MAMOSTA = 'مامۆستا'
    YARIDADAR = 'یاریدەدەری بەرێوبەر'
    ROLLS_IN_INSTUTE = [
        (BAREWBAR, 'بەرێوبەر'),
        (EDRA, 'ئیدارە'),
        (MAMOSTA, 'مامۆستا'),
        (YARIDADAR, "یاریدەدەری بەرێوبەر")
        
    ]
    BAKALORIS = 'بەکالۆریۆس'
    DEBLOM = 'دیبلۆم'
    MASTER = 'ماستەر'
    DCTOR = 'دکتۆرا'
    PROFESOR = 'پرۆفیسۆر'
    YEAR_IN_SCHOOL_CHOICES = [
        (BAKALORIS, 'بەکالۆریۆس'),
        (DEBLOM, 'دیبلۆم'),
        (MASTER, 'ماستەر'),
        (DCTOR, 'دکتۆرا'),
        (PROFESOR, 'پرۆفیسۆر'),
    ]
    BEREKARI = 'بیرکای'
    ENGLISH = 'ئینگلیزی'
    ARABIC = 'زمانی عەرەبی'
    KARGERE = 'کارگێری'
    IT = 'کۆمپیتەر'
    FIZYA = 'فیزیا '
    KURDISH =  'زمانی کوردی'


    BABATAKAN = [
        (BEREKARI, 'بیرکای'),
        (ENGLISH, 'زمانی ئینگلیزی'),
        (ARABIC, 'زمانی عەرەبی'),
        (KARGERE, 'کارگێری'),
        (IT, 'کۆمپیتەر'),
        (KURDISH, 'زمانی کوردی'),
        (FIZYA, 'فیزیا'),
    ]
    rolle = models.CharField(
        max_length=100,
        choices=ROLLS_IN_INSTUTE,
        default=MAMOSTA,
    )

   
    name = models.CharField(max_length=200)
    certificate = models.CharField(max_length=100, choices=YEAR_IN_SCHOOL_CHOICES, default=DEBLOM)
    specialty = models.CharField(max_length=100, choices=BABATAKAN)
    image = models.ImageField(blank=True, upload_to='blog_images')

    def __str__(self):
        return self.name
    

class Activity(models.Model):

    title =  models.CharField(max_length=200)
 
    discreption = models.TextField()
    date = models.DateField()
    imageTitle = models.ImageField(blank=True,upload_to='blog_images')
    imageOne = models.ImageField(blank=True, upload_to='blog_images')
    imageTwo = models.ImageField(blank=True, upload_to='blog_images')
    imageThree= models.ImageField(blank=True, upload_to='blog_images')
    imageFour = models.ImageField(blank=True, upload_to='blog_images')

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    name =  models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name