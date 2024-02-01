from django.shortcuts import render


def news_home(requst):
    return render(requst, "news/news_home.html")
