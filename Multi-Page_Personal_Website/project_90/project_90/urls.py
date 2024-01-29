
from django.contrib import admin
from django.urls import path
from project_90_app.views import home, about, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('about/', about),
    path('contacts/', contacts, name='contacts'),
    

]
