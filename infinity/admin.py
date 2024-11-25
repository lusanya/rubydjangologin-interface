from django.contrib import admin

from .models import Reset, Login, Register

# Register your models here.
admin.site.register(Reset)
admin.site.register(Login)
admin.site.register(Register)