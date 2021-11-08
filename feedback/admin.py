from django.contrib import admin
from .models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'email')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'content')


admin.site.register(FeedBack, FeedBackAdmin)
