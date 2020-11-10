from django.contrib.auth.views import PasswordResetView
from django.contrib import admin

# your_app/context_processors.py
def admin_header_processor(request):
    site_header = 'DNC Teacher Directory - Accounts Settings'  # get site header text. For django 2.X it should be 
    return {"site_header": site_header}