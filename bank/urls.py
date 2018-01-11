from django.conf.urls import url

from . import views

app_name = "bank"

urlpatterns = [
	url(r'^$', views.all_accounts, name="bank_accounts"),
	url(r'^new-account$', views.new_account, name="add_account"),
	url(r'^edit-account/(?P<account_pk>\d+)/$', views.edit_account, name="edit_account"),
	url(r'^update-account/(?P<account_pk>\d+)/$', views.update_account, name="update_account"),
	url(r'^delete-account/(?P<account_pk>\d+)/$', views.delete_account, name="delete_account"),

	url(r'^bank-transactions/$', views.all_transactions, name="bank_transactions"),
	url(r'^add-transaction/$', views.new_transaction, name="add_transaction"),
	url(r'^edit-transaction/(?P<transaction_pk>\d+)/$', views.edit_transaction, name="edit_transaction"),
	url(r'^update-transaction/(?P<transaction_pk>\d+)/$', views.update_transaction, name="update_transaction"),
	url(r'^delete-transaction/(?P<transaction_pk>\d+)/$', views.delete_transaction, name="delete_transaction"),

	url(r'^fetch-account/(?P<account_pk>\d+)/$', views.fetch_account, name="fetch_account"),
	
]