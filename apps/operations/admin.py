from django.contrib import admin
from .models import ActivationCommissionTransaction, ReferralCommissionTransaction

# Register your models here.



class ActivationCommissionTransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'trans_token_id',
        'activation_epin',
        'activ_commission',
        'iba',
        'package',
        'country', 
        'activation_profit', 
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = ActivationCommissionTransaction

admin.site.register(ActivationCommissionTransaction, ActivationCommissionTransactionAdmin)



class ReferralCommissionTransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'trans_token_id',
        'iba',
        'downliner',
        'package',
        'referral_commission',
        'pv_assigned_to_upliner', 
        'activation_profit', 
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = ReferralCommissionTransaction

admin.site.register(ReferralCommissionTransaction, ReferralCommissionTransactionAdmin)