from django.db import models


class Product(models.Model):
    name_en = models.CharField(max_length=100, blank=False, null=False)
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name_en


class Expert(models.Model):
    name_en = models.CharField(max_length=100, blank=False, null=False)
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "expert"

    def __str__(self):
        return self.name_en


class Testimonial(models.Model):
    name_en = models.CharField(max_length=100, blank=False, null=False)
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    description_en = models.CharField(max_length=500, blank=False, null=False)
    description_uz = models.CharField(max_length=500, blank=True, null=True)
    description_ru = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return self.name_en


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.name
