"""BinBank_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BinBank.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signin$', signin),  # POST
    url(r'^request_balance',request_balance)
    #url(r'^signup$', signup),  # POST
    #url(r'^edit_user$', edit_user),  # POST
    #url(r'^add_vehicle$', add_vehicle),  # POST
    #url(r'^edit_vehicle$', edit_vehicle),  # POST
    #url(r'^get_list_of_actual_crashes$', get_list_of_actual_crashes),  # GET
    #url(r'^get_list_of_history_crashes$', get_list_of_history_crashes),  # GET
    #url(r'^get_list_of_offers$', get_list_of_offers),  # GET
    #url(r'^get_list_of_vehicles$', get_list_of_vehicles),  # GET
    #url(r'^get_service$', get_service),  # GET
    #url(r'^get_service_reviews$', get_service_reviews),  # GET
]

