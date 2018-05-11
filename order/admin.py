from django.contrib import admin
from order.models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','location','created_date']


admin.site.register(Article,ArticleAdmin)