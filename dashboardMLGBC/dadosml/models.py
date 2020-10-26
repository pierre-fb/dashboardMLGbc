from django.db import models

# Create your models here.

class Dadosml (models.Model):
    LABEL_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9')
    )

    modelml = models.CharField(max_length=20)
    accuracy = models.FloatField()
    prediction = models.FloatField()
    label = models.CharField(max_length=2,choices=LABEL_CHOICES)
    features = models.CharField(max_length=900)



    def __str__(self):
        return self.modelml, self.accuracy, self.prediction, self.label




