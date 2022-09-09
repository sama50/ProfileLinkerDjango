from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views
from app.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('imgupload/',views.uploadurl,name='imgupload'),
    path('addlink/',views.addsocialLink,name='addlink'),
    path('delete/<int:id>/',views.DeletebyId,name='delete'),
    path('logout/',views.logoutby,name='logout'),

    path('profile/',views.profileget,name='profile'),
    path('profile/<slug:id>/',views.showprofile,name='showprofile'),
    path('login/', auth_views.LoginView.as_view(template_name='./login.html', authentication_form=LoginForm), name='login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
