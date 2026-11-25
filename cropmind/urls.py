from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import home, register, user_login, farmer_dashboard, user_logout, upload_image, prediction_history, delete_prediction, weather_dashboard, farmer_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', farmer_dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('upload-image/', upload_image, name='upload_image'),
    path('prediction-history/', prediction_history, name='prediction_history'),
    path('delete-prediction/<int:prediction_id>/', delete_prediction, name='delete_prediction'),
    path('weather/', weather_dashboard, name='weather_dashboard'),
    path('farmer-profile/', farmer_profile, name='farmer_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)