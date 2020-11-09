
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.utils import timezone
from django.db.models import Sum, F, FloatField, Case, When, Max, FloatField
from django.db.models.functions import Cast
from django.urls import resolve
from django.db import connections
import io
import xlsxwriter

from .models import *
# from .forms import *

from datetime import datetime, timedelta
import re
from django.http import HttpResponse
from django.http import JsonResponse

import pandas as pd
import time



class TeacherSubjectListView(ListView):

    model = Subjects

    def get_queryset(self):

        return Subjects.objects.all().order_by('teacher')
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
