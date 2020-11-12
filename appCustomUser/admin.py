from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


User = get_user_model()


def get_custom_user_fieldset():
    custom_personal_info_fields = tuple()

    for field in UserAdmin.fieldsets:
        if field[0] == 'Personal info':
            # add phone number to the fields in the section
            fields = field[1]['fields'] + ('phone_number', 'address',)
            # create a new field in useradmin fieldset
            _field = ('Personal info',)
            details = {}
            # define the details
            for key, val in field[1].items():
                if key == 'fields':
                    details['fields'] = fields
                else:
                    details[key] = val
            _field += (details,)
            custom_personal_info_fields += (_field,)
        else:
            custom_personal_info_fields += (field,)

    return custom_personal_info_fields


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = UserAdmin.list_display + ('phone_number',)
    fieldsets = get_custom_user_fieldset()


admin.site.register(User, CustomUserAdmin)
