from django.contrib import admin
from .models import User, UserImage
from django.contrib.auth.models import Group
from .forms import GroupAdminForm

admin.site.register(User)
admin.site.register(UserImage)
# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)