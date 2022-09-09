from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView,FormView
from .models import GeeksModel
 
class GeeksCreate(CreateView):
 
    # specify the model for create view
    model = GeeksModel
    template_name= "create_view.html"
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']
    
    def get_success_url(self): # new
        return reverse('geeksmodel_list')
 
class GeeksList(ListView):
 
    # specify the model for list view
    model = GeeksModel
    template_name ="geeksmodel_list.html"
 
class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel
    template_name= "geeksmodel_detail.html"
    
from django.urls import reverse
class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel
    template_name="geeksmodel_form.html"
 
    # specify the fields
    fields = [
        "title",
        "description"
    ]
    def get_success_url(self): # new
        return reverse('geeksmodel_list')
from .models import GeeksModel
 
class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
    template_name= "geeksmodel_confirm_delete.html"
    
    def get_success_url(self):
        return reverse('geeksmodel_list') 
