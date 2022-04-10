from django.contrib import admin
from .models import (
    Packages, Rank, CompensationPlan, Product, 
    RetailCommission, ActivationCommission, 
    ReferralCommission, TokenCreationHelper, Epins
)

# Register your models here.



class PackagesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'package_name',
        'personal_volume',
        'dollar_amount',
        'cedis_amount',
        'naira_amount',
        'products_quantity',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = Packages

admin.site.register(Packages, PackagesAdmin)


class RankAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'rank_name',
        'pv',
        'lesser_team_volume',
        'sponsor_team_volume',
        'max_cummulative_leg',
        'earning_in_cedis',
        'prizes',
        # 'date_created',
        # 'date_updated',
    ]

    class Meta:
        model = Rank

admin.site.register(Rank, RankAdmin)




class CompensationPlanAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'percentage',
        'condition',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = CompensationPlan

admin.site.register(CompensationPlan, CompensationPlanAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_name',
        'wholesale_price',
        'retail_price',
        'available_quantity',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)




class RetailCommissionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'retail_name',
        'bonus_type',
        'product_quantity',
        'percentage',
        'condition', 
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = RetailCommission

admin.site.register(RetailCommission, RetailCommissionAdmin)




class ActivationCommissionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'activation_name',
        'bonus_type',
        'package',
        'product_quantity', 
        'percentage',
        'condition', 
        'reward', 
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = ActivationCommission

admin.site.register(ActivationCommission, ActivationCommissionAdmin)




class ReferralCommissionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ref_name',
        'bonus_type',
        'package', 
        'percentage',
        'condition', 
        'reward', 
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = ReferralCommission

admin.site.register(ReferralCommission, ReferralCommissionAdmin)




class TokenCreationHelperAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'number',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = TokenCreationHelper

admin.site.register(TokenCreationHelper, TokenCreationHelperAdmin)




class EpinsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'e_pin',
        'country',
        'package',
        'payement_transaction_proof',
        'created_by',
        'for_subadmin',
        'used_by',
        'used_for',
        'status',
        'date_created',
        'date_updated',
    ]

    class Meta:
        model = Epins

admin.site.register(Epins, EpinsAdmin)























