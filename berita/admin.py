from django.contrib import admin
from .models import Berita, Kategori

# Register your models here.
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "isi_berita",)



admin.site.register(Berita, BeritaAdmin)
admin.site.register(Kategori)