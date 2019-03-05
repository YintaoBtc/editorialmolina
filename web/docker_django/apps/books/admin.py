from django.contrib import admin
from .models import Book, Writer

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "modified")

class WriterAdmin(admin.ModelAdmin):
    readonly_fields = ("created_date", "modified_date")


admin.site.register(Book, BookAdmin)
admin.site.register(Writer, WriterAdmin)
