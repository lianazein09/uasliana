from django.contrib import admin
from .models import Berita, Kategori, klinik
from .models import Member

# Register your models here.
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "isi_berita",)



admin.site.register(Berita, BeritaAdmin)
admin.site.register(Kategori)
admin.site.register(klinik)


class MemberAdmin(admin.ModelAdmin):
    list_display="nama","alamat","usia"

admin.site.register(Member,MemberAdmin)


