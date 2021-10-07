from django.contrib import admin
from .models import Social


class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

    #extender readonly_fields para q determinado usuario no pueda modificar algo
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ("created","updated","key","name")
        else:
            ("created","updated")


admin.site.register(Social, SocialAdmin)