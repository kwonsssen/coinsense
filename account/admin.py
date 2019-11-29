from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import notify

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'is_staff','code')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'password','code')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'date_joined', 'password1', 'password2')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(get_user_model(), UserAdmin)

@admin.register(notify)
class notifyAdmin(admin.ModelAdmin):
    list_display = ['user','board','post','content','created_at']

