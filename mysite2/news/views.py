from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DeleteView


def news_home(requst):
    news = Articles.objects.order_by("-date")
    return render(requst, "news/news_home.html", {"news": news})


class NewsDetailView(DeleteView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"


def create(requst):
    error = ""
    if requst.method == "POST":
        form = ArticlesForm(requst.POST)
        if form.is_valid:
            form.save()
            return redirect("news_home")
        else:
            error = "Форма была неверной"

    form = ArticlesForm()
    data = {"form": form, "error": error}
    return render(requst, "news/create.html", data)
