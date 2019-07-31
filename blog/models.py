from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:3]

class portfolio(models.Model):
    title= models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    #이미지를 다룰때에는 명령어 pip install pillow가 필요함
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title

# Create your models here.
