
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.urls import resolve
from django.db import connections
import csv,io
import xlsxwriter

from .models import *
from .forms import *


import pandas as pd
import openpyxl



class TeacherSubjectListView(ListView):

    model = Subjects

    def get_queryset(self):

        queryset = {
            'subjects': Subjects.objects.all().order_by('teacher'),
            'teacher': Teacher.objects.all(),
        }

        return queryset
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ImportDataView(LoginRequiredMixin, TemplateView):


    template_name = 'teacher_directory/input_data_view.html'
    success_message = ''
    error_message = ''

    def get(self, request, *args, **kwargs):

        form = InputDataForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = InputDataForm(request.POST or None, request.FILES)
        

        if form.is_valid():
            if request.FILES['teachers']:

                df = pd.read_csv(request.FILES['teachers'])

                #checking for more than 5 subjects
                #possible stopping point though model will not allow more than 5 subjects per teacher in insert
                for subs in df['Subjects taught'].dropna():
                    if subs.split(",") > 5:
                        self.error_message = 'ERROR: uploading more than 5 subjects'
                        return render(request, self.template_name, {'form': form, 'error_message':self.error_message})
                    else:
                        for x in subs.split(",")
                            Subjects.objects.create(
                                
                            )
                

                Teacher.objects.bulk_create([Teacher(first_name=row['First Name'],
                                                                 last_name=row['Last Name'],
                                                                 profile_picture=row['Profile picture'],
                                                                 email_address=row['Email Address'],
                                                                 phone_number=row['Phone Number'],
                                                                 room_number=row['Room Number'],
                                                                 
                                                                 ) for index, row in dataframe.iterrows()])

                                    
                



            
            if 'pictures' in request.FILES:
                pass
        
        return render(request, self.template_name, {'form': form, 'success_message':self.success_message})