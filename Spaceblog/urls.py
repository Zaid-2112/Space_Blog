from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import index, about, post, contact, search, view_all, registerPage, loginPage, logoutUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'home'),
    path('about/', about, name = 'about'),
    path('post/<int:id>/<slug:slug>', post, name = 'post'),
    path('contact/', contact, name= 'contact'),
    path('search/', search, name= 'search'),
    path('view_all/<str:query>', view_all, name = 'view_all'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),

    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),
	path('logout/', logoutUser, name="logout"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
