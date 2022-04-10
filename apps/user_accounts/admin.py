from django.contrib import admin
from .models import SubadminTable, ClientsTable

# Register your models here.



class SubadminTableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'username',
        'password',
        'created_by',
        'admin_password',
        'email',
        'country',
        # 'date_created',
        # 'date_updated',
    ]

    class Meta:
        model = SubadminTable

admin.site.register(SubadminTable, SubadminTableAdmin)



class ClientsTableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'my_subadmin',
        'subadmin_password',
        'created_by',
        'admin_password',
        'sponsortID',
        'uplinerID',
        'user_type',
        'my_position',
        'my_left_child',
        'my_right_child',
        'email',
        'phone',
        'tel_fixe',
        'address',
        'city',
        'country',
        'national_id_card_number',
        'bank_name',
        'bank_branch_name',
        'account_name',
        'account_number',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = ClientsTable

admin.site.register(ClientsTable, ClientsTableAdmin)