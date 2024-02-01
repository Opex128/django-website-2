from django.shortcuts import render
from .models import Articles


def news_home(requst):
    news = Articles.objects.order_by("-date")
    return render(requst, "news/news_home.html", {"news": news})
