from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "manager", "start_date", "end_date")
    list_filter = ("start_date", "end_date")
    search_fields = ("name", "manager__email", "manager__name")
    filter_horizontal = ("employees",)  # Makes ManyToMany field easier to manage

    fieldsets = (
        ("Project Info", {
            "fields": ("name", "manager", "employees"),
        }),
        ("Timeline", {
            "fields": ("start_date", "end_date"),
        }),
    )
