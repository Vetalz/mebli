from django.contrib import admin
from .models import Gallery, Clients


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('title',)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_phone', 'name', 'phone_ring', 'measuring', 'order', 'created_at')
    list_display_links = ('number_phone',)
    search_fields = ('number_phone',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Clients, ClientsAdmin)

admin.site.site_header = 'Мебельная мастерская'
