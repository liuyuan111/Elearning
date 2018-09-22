from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(StarStudent)
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(BlogCategory)
admin.site.register(Org)
admin.site.register(Section)
admin.site.register(Video)
admin.site.register(Comment)

class CourseAdmin(admin.ModelAdmin):
    fields = ['category', 'level', 'title', 'body', 'cover', 'attachment', 'is_free', 'teacher', 'star', 'price', 'recommend', 'published']

admin.site.register(Course, CourseAdmin)