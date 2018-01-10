from django.conf.urls import url

from . import views

app_name = "income"

urlpatterns = [
	url(r'^$', views.categories, name="income_categories"),
	url(r'^new-category/$', views.new_category, name="new_category"),
	url(r'^fetch-category/(?P<category_pk>\d+)/$', views.edit_category, name="edit_category"),
	url(r'^update-category/(?P<category_pk>\d+)/$', views.update_category, name="update_category"),
	url(r'^delete-category/(?P<category_pk>\d+)/$', views.delete_category, name="delete_category"),
]