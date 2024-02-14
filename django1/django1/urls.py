from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('freelancer/', views.freelancer, name='freelancer'),
    path('job/', views.job, name='job'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/<slug:verifyID>', views.verification, name="verification")
    
    # 'about/<int/str/slug:historyID>' or we can leave empty if we don't know about our data
    # path('about/<int:historyID>', views.about_histrory, name='about_history'), # dynamic routing/urls
]
