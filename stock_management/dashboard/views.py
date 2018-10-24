from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import Item
from django.utils import timezone
from dashboard.forms import AddItemForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from .forms import UserCreateForm
from django.db.models import Q
from django.views.generic.edit import ModelFormMixin


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("dashboard:login")
    template_name = "dashboard/signup.html"



class HomePage(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'dashboard/mainpage.html'
    model = Item
    def get_queryset(self):
        return Item.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class AboutView(TemplateView):
    template_name = 'about.html'



class ItemListView(LoginRequiredMixin,ListView):
     login_url = '/login/'
     redirect_field_name = 'dashboard/item_list.html'
     model = Item
     def get_queryset(self):
         return Item.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')



     def get_queryset(self):
         return Item.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')



class ItemDetailView(LoginRequiredMixin,DetailView):
    login_url='/login/'
    redirect_field_name = 'dashboard/item_detail.html'
    model = Item


class CreateItemView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'dashboard/item_new.html'

    form_class = AddItemForm

    model = Item
    success_url=reverse_lazy('dashboard:item_list')


class ItemUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'dashboard/item_list.html'
    success_url = reverse_lazy('dashboard:item_list')

    form_class = AddItemForm

    model = Item

class ItemDeleteView(LoginRequiredMixin,DeleteView):
    model = Item
    success_url = reverse_lazy('dashboard:item_list')

class SellItem(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'dashboard/item_sell.html'
    template_name='dashboard/item_sell.html'

    # def post(self,request,*args,**kwargs):
    #     print(request.POST.get("name"))

class AddItem(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'dashboard/item_add.html'
    template_name='dashboard/item_add.html'


class LowItem(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'dashboard/item_low.html'
    template_name='dashboard/item_low.html'


def search(request):

    items = Item.objects.all()
    search_term = ''

    search_term = request.GET['search']
    items = items.filter(name__icontains=search_term)
    context = {"items": items, "search_term":search_term}
    return render(request,'dashboard/item_search.html', context)
