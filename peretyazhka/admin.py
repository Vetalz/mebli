from django.contrib import admin
from .models import Gallery_peretyazhka, Clients_peretyazhka


class Gallery_peretyazhkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('title',)


class Clients_peretyazhkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_phone', 'name', 'created_at')
    list_display_links = ('number_phone',)
    search_fields = ('number_phone',)


admin.site.register(Gallery_peretyazhka, Gallery_peretyazhkaAdmin)
admin.site.register(Clients_peretyazhka, Clients_peretyazhkaAdmin)




