from django.contrib import admin
from .models import (
    Crop,
    Disease,
    Prediction,
    FarmerProfile,
    UploadedLeafImage
)


admin.site.register(Crop)
admin.site.register(Disease)
admin.site.register(Prediction)
admin.site.register(FarmerProfile)
admin.site.register(UploadedLeafImage)