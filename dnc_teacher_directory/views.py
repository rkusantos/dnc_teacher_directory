from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from django.contrib.auth.models import Group 
from django.shortcuts import render
import os

register = template.Library()

# print(query)
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #         if request.user.is_authenticated:
    #             return HttpResponseRedirect(reverse("home"))
    #         return super().get(request, *args, **kwargs)



     
    #optional for testing
    #for future use
    #standard for prodiction
    @register.filter(name='is_group') 
    def is_group(user, group_name):
        group =  Group.objects.get(name=group_name) 
        return group in user.groups.all() 


    login_url = 'accounts/login/'

    # def get(self, request):

    #     files = os.listdir('D:/KN/knportal/media/HomePage/Carousel')
    #     print(files)
    #     args = {'files': files}

    #     return render(request, self.template_name, args)

 
