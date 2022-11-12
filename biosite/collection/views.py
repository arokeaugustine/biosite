from django.shortcuts import render, get_object_or_404
from .models import Category, Specimen


def collection(request):
    category = Category.objects.all()
    return render(request, 'collections.html', {'category':category} )

def specimenspage(request, slug):
    category = get_object_or_404(Category, slug=slug)
    # specimen=Specimen.objects.all()
    specimen = Specimen.objects.filter(category=category)
    # specimen = get_object_or_404(Specimen, category=category)

    return render(request, 'specimen.html', {'category':category, 'specimen':specimen})
