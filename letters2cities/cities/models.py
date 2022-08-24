from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    image_file = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name_plural = "cities"
    def __str__(self):
       return self.name

    # def get_absolute_url(self):
    #     return reverse("city_detail", kwargs={"slug": self.slug})

class Letter(models.Model):
    # to establish association to a city
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return (str(self.author) + " says: " + str(self.content))
