from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here
def berita(request):
    mem=Member.objects.all()
    return render(request,'berita.html',{'mem':mem})

def add(request):
    return render (request,'add.html')

def addrec(request):
    x=request.POST['nama']
    y=request.POST['alamat']
    z=request.POST['usia']
    mem=Member(nama=x,alamat=y,usia=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})


def uprec(request,id):
    x=request.POST['nama']
    y=request.POST['alamat']
    z=request.POST['usia']
    mem=Member.objects.get(id=id)
    mem.nama=x
    mem.alamat=y
    mem.usia=z
    mem.save()
    return redirect("/")

def detailberita(request):
    template = loader.get_template('detailberita.html')
    return HttpResponse (template.render())

def isiberita(request):
    template = loader.get_template('isiberita.html')
    return HttpResponse (template.render())

def done(request):
    template = loader.get_template('done.html')
    return HttpResponse (template.render())

def formberita(request):
    template = loader.get_template('formberita.html')
    return render (request,'formberita.html')


