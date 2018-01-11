from django.conf.urls import url

from . import views

app_name = "income"

urlpatterns = [
	url(r'^$', views.categories, name="income_categories"),
	url(r'^new-category/$', views.new_category, name="new_category"),
	url(r'^fetch-category/(?P<category_pk>\d+)/$', views.edit_category, name="edit_category"),
	url(r'^update-category/(?P<category_pk>\d+)/$', views.update_category, name="update_category"),
	url(r'^delete-category/(?P<category_pk>\d+)/$', views.delete_category, name="delete_category"),

	url(r'^income-transactions/$', views.all_transactions, name="income_transactions"),
	url(r'^add-transaction/$', views.new_transaction, name="add_transaction"),
	url(r'^edit-transaction/(?P<transaction_pk>\d+)/$', views.edit_transaction, name="edit_transaction"),
	url(r'^update-transaction/(?P<transaction_pk>\d+)/$', views.update_transaction, name="update_transaction"),
	url(r'^delete-transaction/(?P<transaction_pk>\d+)/$', views.delete_transaction, name="delete_transaction"),
]