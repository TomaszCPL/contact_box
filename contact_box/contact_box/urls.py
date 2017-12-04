from django.conf.urls import url
from django.contrib import admin
from contact_list.views.landing_view import LandingView
from contact_list.views.contact_list_view import ContactListView
from contact_list.views.contact_add_view import ContactAddView
from contact_list.views.contact_modify_view import ContactModifyView
from contact_list.views.contact_delete_view import ContactDeleteView
from contact_list.views.contact_show_view import ContactShowView
from contact_list.views.contact_addAddress_view import ContactAddAddressView
from contact_list.views.contact_addPhone_view import ContactAddPhoneView
from contact_list.views.contact_addEmail_view import ContactAddEmailView
from contact_list.views.groups_list_view import GroupsListView
from contact_list.views.groups_add_view import GroupsAddView
from contact_list.views.groups_show_view import GroupsShowView
from contact_list.views.groups_delete_view import GroupsDeleteView
from contact_list.views.groups_search_view import GroupsSearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^/?$', LandingView.as_view()),
    url(r'^contact/list$', ContactListView.as_view()),
    url(r'^contact/add$', ContactAddView.as_view()),
    url(r'^contact/modify/(?P<my_id>(\d)+)$', ContactModifyView.as_view()),
    url(r'^contact/delete/(?P<my_id>(\d)+)$', ContactDeleteView.as_view()),
    url(r'^contact/show/(?P<my_id>(\d)+)$', ContactShowView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addAddress$', ContactAddAddressView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addPhone$', ContactAddPhoneView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addEmail$', ContactAddEmailView.as_view()),
    url(r'^groups/list$', GroupsListView.as_view()),
    url(r'^groups/add$', GroupsAddView.as_view()),
    url(r'^groups/show/(?P<my_id>(\d)+)$', GroupsShowView.as_view()),
    url(r'^groups/delete/(?P<my_id>(\d)+)$', GroupsDeleteView.as_view()),
    url(r'^groups/search$', GroupsSearchView.as_view()),
]