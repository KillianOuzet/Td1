from django.shortcuts import render
from django.views.generic import *
from .models import Product

# Create your views here.

from django.http import Http404, HttpResponse

def home(request,name):
  return HttpResponse("Bonjour depuis Django  " + name)

class HomeView(TemplateView):
  template_name = "lesTaches/home.html"

  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    context['titreh1'] = "Hello DJANGO"
    return context
  
class HomeView(TemplateView):
  template_name = "lesTaches/home.html"

  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    context['titreh1'] = "Hello DJANGO"
    return context
  
class AboutView(TemplateView):
  template_name = "lesTaches/home.html"

  def get_context_data(self, **kwargs):
    context = super(AboutView, self).get_context_data(**kwargs)
    context['titreh1'] = "About us..."
    return context
  
  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
class ContactView(TemplateView):
  template_name = "lesTaches/home.html"

  def get_context_data(self, **kwargs):
    context = super(ContactView, self).get_context_data(**kwargs)
    context['titreh1'] = "Contact us..."
    return context
  
  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
def contact(request):
  return HttpResponse("<h1>Contact us!</h1>")

def list_products(request):
    prdcts = Product.objects.all()
    return render(request, 'lesTaches/list_products.html',{'prdcts': prdcts})

def product_by_Id(request,id):
    prdct = Product.objects.get(pk=id)
    return render(request, 'lesTaches/product.html',{'prdct': prdct})