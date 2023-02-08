from django.contrib import admin
from app.models import Profile, Education


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone']
    list_display_links = ['email', 'first_name', 'last_name', 'phone']
    list_filter = ['email', 'first_name', 'last_name']
    readonly_fields = ['id', 'updated_at', 'created_at']

    fieldsets = (
        ('Profile Info', {'fields': ('id', 'first_name', 'last_name', 'email', 'phone', 'address',),}),
        ('Other Info', {'fields': ('updated_at', 'created_at',)}),
    )

    def has_delete_permission(self, request, obj=None):
        return False


class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'start_date', 'end_date', 'is_pursuing']
    list_display_links = ['degree', 'school', 'start_date', 'end_date', 'is_pursuing']
    list_filter = ['degree']
    readonly_fields = ['id', 'updated_at', 'created_at']

    fieldsets = (
        ('Profile Info', {'fields': ('id', 'degree', 'school', 'start_date', 'end_date', 'is_pursuing'),}),
        ('Other Info', {'fields': ('updated_at', 'created_at')}),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education, EducationAdmin)
