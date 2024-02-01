from django.contrib import admin

from .models import Articles


class ChoiceInline(admin.TabularInline):
    model = Articles
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    fields = ("title", "date", "anons", "full_text")

    list_display = ("title", "date", "anons", "was_published_recently")
    list_filter = ["date"]
    search_fields = ["title"]


admin.site.register(Articles, AuthorAdmin)
