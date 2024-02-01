from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(requst):
    news = Articles.objects.order_by("-date")
    return render(requst, "news/news_home.html", {"news": news})


def create(requst):
    error = ""
    if requst.method == "POST":
        form = ArticlesForm(requst.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
        else:
            error = "Форма была неверной"

    form = ArticlesForm()
    data = {"form": form, "error": error}
    return render(requst, "news/create.html", data)
