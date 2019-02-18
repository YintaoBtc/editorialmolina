from django.contrib import admin

# Register your models here.
from .models import Book, Writer

#class BookAdmin(admin.ModelAdmin):
#    readonly_fields = ("created", "updated")

#class WriterAdmin(admin.ModelAdmin):
#    readonly_fields = ("created", "updated")


admin.site.register(Book)
admin.site.register(Writer)
