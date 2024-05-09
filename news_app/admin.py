from django.contrib import admin
from news_app.models import Artice


@admin.register(Artice)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag', 'author', 'created')

    class Meta:
        model = Artice
