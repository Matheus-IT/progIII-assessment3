from django.db import models


class Draw(models.Model):
    date = models.DateField('Data')
    ball1 = models.IntegerField('Bola1')
    ball2 = models.IntegerField('Bola2')
    ball3 = models.IntegerField('Bola3')
    ball4 = models.IntegerField('Bola4')
    ball5 = models.IntegerField('Bola5')
    ball6 = models.IntegerField('Bola6')
