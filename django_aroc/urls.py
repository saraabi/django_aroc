from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('idara/', admin.site.urls),
    path('', include('aroc.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]