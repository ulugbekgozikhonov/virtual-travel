from django.urls import path
from .views import home_view, about_view, service_view, package_view, blog_view

urlpatterns = [
	path('', home_view, name='home'),
	path('about/', about_view, name='about'),
	path('service/', service_view, name='service'),
	path('packege/', package_view, name='package'),
	path('blog/', blog_view, name='blog'),
]
