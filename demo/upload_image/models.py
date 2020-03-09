from django.db import models

# Create your models here.

class Img(models.Model):

    img_name = models.CharField(max_length=30)

    img_con = models.ImageField(upload_to='image/')
    
    def __str__(self):
        return self.img_name