from django.contrib import admin
from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ("application_number", "full_name", "email", "phone", "status", "submitted_at")
    list_filter = ("status", "gender", "submitted_at")
    search_fields = ("application_number", "full_name", "email", "phone", "transaction_id")
    readonly_fields = ("application_number", "submitted_at", "updated_at")
    list_per_page = 25
