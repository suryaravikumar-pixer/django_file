"""djangoapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from course import views #>>>>>this is also one of the way to add module ,even we follow another method (#1)

#from course import views as cv #1  
# we have another method also follow (#2)
from course.views import learn_python
from course.views import learn_django
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('learndj/', views.learn_django),(#1rel)
    #path('learnpy/', cv.learn_python),(#2 rel)
    path('learnpy/', learn_python),
    path('learndj/', learn_django)

]
