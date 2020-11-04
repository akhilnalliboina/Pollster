from django.contrib import admin

from .models import Question

admin.site.register(Question)
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Pollster Admin"
