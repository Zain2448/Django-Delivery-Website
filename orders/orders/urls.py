"""
URL configuration for orders project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# My imports
from django.conf.urls.static import static
from customer import views as customer
from staff import views as staff

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),

    # customer urls
    path("",customer.Index.as_view(), name="index"),
    path("about/",customer.About.as_view(),name="about"),
    path("order/",customer.Order.as_view(),name="order"),

    # staff urls
    path("login",staff.Login.as_view(),name="login"),
    path('overview/',staff.Overview.as_view(),name="overview"),
    path('order_details/<int:my_id>/',staff.OrderDetail.as_view(),name="order_details"),
    path('add_item/',staff.AddItem.as_view(),name="add_item"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

