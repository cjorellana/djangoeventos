from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from eventos import views

from eventos.forms import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', include('eventos.urls')),
    path('login/', CustomLoginView.as_view(template_name='usuarios/login.html'), name='login'),
    #path('login/', LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)