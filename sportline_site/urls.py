from django.contrib import admin
from django.urls import path
from catalogo.views import landing_catalogo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_catalogo, name="landing_catalogo"),  
]