from django.db import models

# Create your models here.


class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_kategori}"


class Berita(models.Model):
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100)
    isi_berita = models.TextField()

    def __str__(self):
        return f"{self.judul}"
    
class klinik(models.Model):
    nama_klinik = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_klinik}"

class Member(models.Model):
    nama=models.CharField(max_length=100)
    alamat=models.CharField(max_length=100)
    usia=models.CharField(max_length=100)
