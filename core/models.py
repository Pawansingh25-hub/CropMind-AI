from django.db import models
from django.contrib.auth.models import User


class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    soil = models.CharField(max_length=200, blank=True)
    water_requirement = models.CharField(max_length=200, blank=True)
    growing_period = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=150)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    symptoms = models.TextField()
    causes = models.TextField(blank=True)
    prevention = models.TextField(blank=True)
    management = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Prediction(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='predictions/')
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop.name} - {self.disease.name}"
    

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    farm_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username    
    
    
class UploadedLeafImage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='leaf_images/'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    predicted_disease = models.CharField(max_length=150, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username} - Leaf Image"        