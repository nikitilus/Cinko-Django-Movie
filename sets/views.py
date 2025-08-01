from django.shortcuts import render, redirect
from .models import Set, Film
from .forms import SetForm, FilmForm

def set_create (request):
    error = ""
    if request.method == "POST":
        form = SetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            error = "Форма была неверной"
    form = SetForm()
    data = {
        "form": form,
        "error": error,}
    
    return render(request, "sets/set_create.html", data)



def film_create (request):
    error = ""
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            error = "Форма была неверной"
    form = FilmForm()
    data = {
        "form": form,
        "error": error,}
    return render(request, "sets/film_create.html", data)
    
def films(request):
    films = Film.objects.all()
    data = {
        "films": films,
    }

    return render(request, "sets/films.html", data)



