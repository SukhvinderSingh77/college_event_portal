from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('', RedirectView.as_view(url='events/', permanent=True)),  # Redirect root URL to events
]