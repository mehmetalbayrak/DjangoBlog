from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=255,null=True)
    urlSlug = models.CharField(max_length=50,null=True)
    metaTitle = models.CharField(max_length=150,null=True)
    metaDescription = models.TextField(null=True)
    keywords = models.CharField(max_length=255,null=True)
    createdDate = models.DateField(null=True)
    def __str__(self) -> str:
        return f"Başlık : {self.title} | Image : {self.image}"