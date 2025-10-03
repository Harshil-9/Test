from django.contrib import admin
from .models import DailyTodo, DailyUpdate

@admin.register(DailyTodo)
class DailyTodoAdmin(admin.ModelAdmin):
    list_display = ("employee", "task", "completed", "date")
    list_filter = ("completed", "date")
    search_fields = ("task", "employee__email", "employee__name")
    ordering = ("-date",)

    fieldsets = (
        ("Task Info", {
            "fields": ("employee", "task", "completed"),
        }),
        ("Date Info", {
            "fields": ("date",),
        }),
    )
    readonly_fields = ("date",)


@admin.register(DailyUpdate)
class DailyUpdateAdmin(admin.ModelAdmin):
    list_display = ("employee", "working_hours", "date")
    list_filter = ("date",)
    search_fields = ("description", "employee__email", "employee__name")
    ordering = ("-date",)

    fieldsets = (
        ("Update Info", {
            "fields": ("employee", "description", "working_hours"),
        }),
        ("Date Info", {
            "fields": ("date",),
        }),
    )
    readonly_fields = ("date",)
