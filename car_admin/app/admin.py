from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'review_count']
    list_filter = ['brand', 'model']
    ordering = ['-id']
    search_fields = ['brand', 'model']

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ['car', 'title']
    list_filter = ['car', 'title']
    ordering = ['-id']
    search_fields = ['car', 'title']

# # @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     ordering = ['-pk']
#     list_display = ['brand', 'model', 'review_count']
#     list_filter = ['model']
#     search_fields = ['brand', 'model']
#
# # @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     ordering = ['-pk']
#     form = ReviewAdminForm
#     list_display = ['car', 'title']
#     list_filter = ['car']
#     search_fields = ['car', 'title']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
