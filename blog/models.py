from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def summary(self):
        return self.text[:300]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%-H:%M, %e %B')

    def __str__(self):
        return self.title
