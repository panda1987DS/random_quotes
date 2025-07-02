from django.contrib import admin
from .models import Quote

# Register the Quote model with the Django admin site
# This allows administrators to add, edit, and delete quotes via the admin interface.
admin.site.register(Quote)
