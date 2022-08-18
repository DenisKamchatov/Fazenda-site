from django.contrib import admin
from .models import Cottage, Gallery, Contacts, Photogallery

class CottageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class CottageInline(admin.TabularInline):
    fk_name = 'cottage'
    model = Gallery


class GalleryAdmin(admin.ModelAdmin):
    inlines = [CottageInline,]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')


class PhotogalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')

admin.site.register(Photogallery, PhotogalleryAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Gallery, PhotoAdmin)
admin.site.register(Cottage, CottageAdmin)