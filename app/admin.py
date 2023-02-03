from django.contrib import admin
from app.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone']
    list_display_links = ['email', 'first_name', 'last_name', 'phone']
    list_filter = ['email', 'first_name', 'last_name']
    readonly_fields = ['id']

    fieldsets = (
        ('Profile Info', {'fields': ('id', 'first_name', 'last_name', 'email', 'phone', 'address'),}),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Profile, ProfileAdmin)
