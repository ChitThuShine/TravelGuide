from django.contrib import admin
from imagekit.admin import AdminThumbnail
import datetime
import csv
from django.http import HttpResponse
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin

admin.site.site_header = (u"Administration de Travel Guide")
admin.site.index_title = (u"Travel Guide")

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'

class AppUserAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

class PhotoLieuInline(admin.TabularInline):
    model = PhotoLieu
    raw_id_fields = ['refLieu']
    max_num = 2

class LieuAdmin(OSMGeoAdmin):
    list_display = ('name','refCategory','street','zipCode','city','country','photo_thumbnail','location','valide')
    list_filter = ('country','valide',)
    search_fields = ('name','city')
    date_hierarchy = 'updatedAt'
    ordering = ['valide','updatedAt']
    raw_id_fields = ('refCategory',)
    inlines = [PhotoLieuInline]
    fieldsets = (
        # Fieldset 1 : meta-info
        ('Infos', {
            'fields': ('name', 'refCategory', 'mainPhoto', 'valide')
        }),
        # Fieldset 2 : adresse
        ('Adresse', {
            'classes': ['collapse', ],
            'description': 'Vous pouvez utiliser la carte pour geolocaliser le lieu',
            'fields': ('street','zipCode','city','country','location',)
        }),
    )
    photo_thumbnail = AdminThumbnail(image_field='mainPhoto')
    photo_thumbnail.short_description = 'Photo principale'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail','valide',)
    admin_thumbnail = AdminThumbnail(image_field='picture')
    admin_thumbnail.short_description = 'La photo'

class PhotoLieuAdmin(admin.ModelAdmin):
    list_display = ['refLieu','refPhoto','valide']
    list_filter = ['valide']

admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Lieu,LieuAdmin)
admin.site.register(PhotoLieu,PhotoLieuAdmin)
admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Favori)


