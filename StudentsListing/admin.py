from django.contrib import admin
from StudentsListing.models import Student, Group, Logger
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'middle_name')
    list_filter = ('group', )


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    inlines = [StudentInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Logger)