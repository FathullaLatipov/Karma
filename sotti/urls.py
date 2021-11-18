from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.template.backends import django
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include(django.conf.urls.i18n)),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

urlpatterns += i18n_patterns(
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('profile/', include('users.urls', namespace='profile')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('pages.urls', namespace='contact')),
)
# hny$pz4Ve263K-T
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)