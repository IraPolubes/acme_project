from django.contrib import admin

#ira, pwd 1234

from .models import Birthday, Tag

class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday',)
    list_editable = ('birthday',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_editable = ('tag',)
    list_display_links = None  


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)