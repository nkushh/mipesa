from django.conf.urls import url 

from . import views

app_name = "debts"

urlpatterns = [
	url(r'^$', views.debt_list, name="debts_list"),
	url(r'^new-debt/$', views.new_debt, name="add_debt"),
	url(r'^make-payment/(?P<debt_pk>\d+)/$', views.make_payment, name="make_payment"),
	url(r'^update-debt/(?P<debt_pk>\d+)/$', views.update_debt, name="update_debt"),
	url(r'^delete-debt/(?P<debt_pk>\d+)/$', views.delete_debt, name="delete_debt"),
]