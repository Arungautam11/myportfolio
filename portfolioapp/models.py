from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    logo_name = models.CharField(max_length=100, null= True, blank=True)
    profile_image = models.ImageField(upload_to='images/',
    null=True, blank=True,
    help_text="<h1 style='font-size: 12px; margin-left: 12rem; color: #ce8c95;'>width:500px height:500px</h1>")
    profile_image2 = models.ImageField(upload_to='images/',
    null=True, blank=True,
    help_text="<h1 style='font-size: 12px; margin-left: 12rem; color: #ce8c95;'>width:500px height:500px</h1>")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Arun Portfolio"
        verbose_name_plural = "Arun Portfolio"


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name