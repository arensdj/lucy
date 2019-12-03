"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import jobs.views
from django.conf import settings  # this needed to access static folder.  Needed to show static files.
from django.conf.urls.static import static  # this needed to access static folder.  Needed to show static files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),  # when someone navigates to this website, an integer can be entered and saved into job_id variable(e.g. localhost:8000/jobs/1)
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
# The static url and static root from settings.py which is needed to show static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
