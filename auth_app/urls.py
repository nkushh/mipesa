from django.conf.urls import url

from . import views

app_name = "auth_app"

urlpatterns = [
	url(r'^create-account/$', views.create_account, name="create_account"),
]