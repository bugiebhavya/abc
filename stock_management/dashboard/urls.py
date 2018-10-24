from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'dashboard'


urlpatterns = [
    path('',views.HomePage.as_view(),name = 'homepage'),
    url(r'^items$',views.ItemListView.as_view(),name='item_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item_detail'),
    url(r'^item/new/$', views.CreateItemView.as_view(), name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.ItemUpdateView.as_view(), name='item_edit'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.ItemDeleteView.as_view(), name='item_remove'),
    url(r"login/$", auth_views.LoginView.as_view(template_name="dashboard/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    path('results/',views.search, name='search'),
    path('item/sell/',views.SellItem.as_view(),name = 'item_sell'),
    path('item/add/',views.AddItem.as_view(),name = 'item_add'),
    path('item/low/',views.LowItem.as_view(),name = 'item_low')

    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
