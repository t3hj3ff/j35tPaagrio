from django.contrib import admin
from news.models import News
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    prepopulated_fields = {'slug': ('title',), }
    class Meta:
        model = News()
admin.site.register(News, ProductAdmin)
