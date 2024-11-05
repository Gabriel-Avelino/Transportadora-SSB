"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from sao_sebastiao.views import index, transparencia, contato, noticias, sobreNos, noticia, servicos


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^summernote/', include('django_summernote.urls')),
    path('', index, name='home'),
    path('sobre-nos', sobreNos, name='sobre-nos'),
    path('servicos', servicos, name='servicos'),
    path('transparencia', transparencia, name='transparencia'),
    path('contato', contato, name='contato'),
    path('noticias', noticias, name='noticias'),
    path('noticia/<int:id>', noticia, name='noticia'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
