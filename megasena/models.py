from django.db import models


class Draw(models.Model):
    date = models.DateField('Data')
    ball1 = models.IntegerField('Bola1')
    ball2 = models.IntegerField('Bola2')
    ball3 = models.IntegerField('Bola3')
    ball4 = models.IntegerField('Bola4')
    ball5 = models.IntegerField('Bola5')
    ball6 = models.IntegerField('Bola6')

    def __str__(self):
        return f'Draw<{self.date}{self.ball1}, {self.ball2}, {self.ball3}, {self.ball4}, {self.ball5}, {self.ball6}>'
