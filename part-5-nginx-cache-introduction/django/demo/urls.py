from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p1/', TemplateView.as_view(template_name="p1.html")),
    path('p2/', TemplateView.as_view(template_name="p2.html")),
]
