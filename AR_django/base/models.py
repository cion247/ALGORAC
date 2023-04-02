from django.db import models

# Create your models here.


class Gallery(models.Model):
    topic = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        return ''


class Notice(models.Model):
    topic = models.CharField(max_length=255)
    Slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.topic


class pojects(models.Model):

    def __str__(self):
        pass


class Massges(models.Model):

    def __str__(self):
        pass
