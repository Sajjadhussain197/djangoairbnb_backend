# from django.contrib import admin

# # Register your models here.
# from .models import Property

# admin.site.register(Property)

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Property

# Custom admin class to disable logging
class NoLogModelAdmin(ModelAdmin):
    def log_addition(self, request, object, message):
        pass  # Disables logging of additions

    def log_change(self, request, object, message):
        pass  # Disables logging of changes

    def log_deletion(self, request, object, object_repr):
        pass  # Disables logging of deletions

# Register Property with the custom admin class
admin.site.register(Property, NoLogModelAdmin)
